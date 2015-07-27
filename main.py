"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""

import kivy
kivy.require('1.0.9')
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty
from random import choice, shuffle
from os.path import sep
from kivy.core.window import Window
from game_tools import *
from labels import *

__version__ = '0.2.00'


class MemoryButton(Button):
    done = False
    playsound = True
    filenameSound = StringProperty(None)
    filenameIcon = StringProperty(None)
    sound = ObjectProperty(None)
    background = ObjectProperty(None)
    background_hide = ObjectProperty(None)
    # background_down = ObjectProperty(None)
    background_normal = ObjectProperty(None)

    def on_filenameSound(self, instance, value):
        # the first time that the filename is set, we are loading the sample
        if self.sound is None:
            self.sound = SoundLoader.load(value)

    def on_filenameIcon(self, instance, value):
        # the first time that the filename is set, we are loading the sample
        if self.background_normal is None:
            self.background_normal = value
            self.background = value
            self.background_hide = self.background_down

    @classmethod
    def toggle_sound(cls, instance):
        instance.text = ["Sound On" if instance.state == 'normal' else "Sound Off"][0]
        cls.playsound = instance.state == 'normal'

    def on_press(self):
        if self.parent.state == 'OK' and not self.done:
            if self.parent.first is None:
                self.parent.first = self
                self.background_down, self.background_normal = self.background_normal, self.background_down
            else:
                if self is self.parent.first:
                    self.parent.first = None

                elif self.parent.first.filenameIcon == self.filenameIcon:

                    self.parent.ball_position += 1
                    if self.parent.ball_position > 3:
                        self.parent.narration = "Goal Home"
                        self.parent.score = self.parent.score[0]+1, self.parent.score[1]
                        self.parent.ball_position = 0
                    else:
                        self.parent.narration = str(self.parent.ball_position)  # narrate(self.parent.ball_position)
                    self.parent.left += 1

                    if self.playsound:
                        if self.sound.status != 'stop':
                            self.sound.stop()
                        self.sound.play()

                    self.background_down, self.background_normal = self.background, self.background
                    self.parent.first.background_down, \
                        self.parent.first.background_normal = self.parent.first.background, self.parent.first.background
                    self.done = True
                    self.parent.first.done = True
                    self.parent.first = None
                    # check termination
                    if self.parent.left == self.parent.items:
                        self.parent.game_over()
                        Clock.unschedule(self.parent.elapsed_time)

                else:
                    self.parent.ball_position -= 1
                    if self.parent.ball_position < -3:
                        self.parent.score = self.parent.score[0], self.parent.score[1]+1
                        self.parent.ball_position = 0
                        self.parent.narration = "Goal Away"
                    else:
                        self.parent.narration = str(self.parent.ball_position)  # narrate(self.parent.ball_position)
                    self.parent.first.background_down, \
                        self.parent.first.background_normal = self.parent.first.background_normal,\
                        self.parent.first.background_down
                    self.parent.first = None


class MemoryLayout(GridLayout):
    left = NumericProperty(0)   # left items to find
    items = NumericProperty(0)  # total number of items
    level = NumericProperty(0)  # seconds to count down
    countdown = NumericProperty(0)
    score = ListProperty([0, 0])  # number of missed items
    elapsed = NumericProperty(0)
    ball_position = NumericProperty(0)
    narration = StringProperty("")

    def __init__(self, **kwargs):
        super(MemoryLayout, self).__init__(**kwargs)
        self.state = ""
        self.first = None
        self.level = kwargs["level"]
        self.items = kwargs["items"]
        self.countdown = self.level

    def toggle_buttons(self, state):
        for i in self.children:
            i.background_down, i.background_normal = i.background_normal, i.background_down
        self.state = state

    def hide_buttons(self):
        for i in self.children:
            i.done = False
            i.background_down, i.background_normal = i.background_hide, i.background_hide
            
    def show_buttons(self):
        for i in self.children:
            i.background_normal = i.background
            
    def elapsed_time(self, dt):
        self.elapsed += dt

    def start_game(self, dt):
        self.reset()
        Clock.schedule_interval(self.initial_countdown, 1)
        
    def initial_countdown(self, dt):
        if self.countdown == -1:
            Clock.unschedule(self.initial_countdown)
            self.toggle_buttons("OK")
            Clock.schedule_interval(self.elapsed_time, 0.1)
        else:
            if not hasattr(self.parent.parent, 'countdown'):
                self.parent.parent.countdown = Label(text="")
                self.parent.parent.add_widget(self.parent.parent.countdown)
            popup = self.parent.parent.countdown
            popup.text = ''
            popup.font_size = 12
            popup.color = (0, 0, 0, 1)
            popup.text = str(self.countdown)
            Animation(color=(1, 1, 1, 0), font_size=150).start(popup)
            self.countdown -= 1

    def reset_time(self, instance, new_level):
        self.level = int(new_level)

    def reset_nb_item(self, instance, new_nb):
        self.items = int(new_nb)

    def reset(self):
        self.countdown = self.level
        self.first = None
        self.left = 0
        self.elapsed = 0
        self.score = [0, 0]
        self.hide_buttons()
        self.state = ''
        self.update_nb_items()
        self.ball_position = 0
 
    def restart_game(self, inst):
        
        self.reset()
        self.show_buttons()
        Clock.schedule_interval(self.initial_countdown, 1)

    def update_nb_items(self):

        if self.items != len(self.children):
            # update self.rows to keep acceptable ratio
            new_row = best_ratio(self.items*2, self.width, self.height)
            self.clear_widgets()
            self.rows = new_row
            shuffle(icons)
            iicons = icons[:self.items]
            iicons = iicons+iicons
            shuffle(iicons)
            for i in iicons:
                s = i.split(".png")[0].split(sep)[1]
                if s in sounds:
                    a_sound = choice(sounds[s])
                else:
                    a_sound = sounds['default'][0]

                btn = MemoryButton(
                    text="",
                    filenameIcon=i,
                    filenameSound=a_sound,
                    )  
                self.add_widget(btn)
        else:
            shuffle(self.children)

    def save_level(self):
        file_name = join(App.get_running_app().user_data_dir, 'level.dat')
        with open(file_name, 'w') as fd:
            user_data = {"items": self.items, "level": self.level}
            json.dump(user_data, fd)
            
    def game_over(self):
        
        # calculate score
        score = str(self.score[0]) + '-' + str(self.score[1])
        print "done!", score
        self.save_level()
        content2 = BoxLayout(orientation='vertical', spacing=10)
        # content.add_widget(Label(text='score: %d'%int(score)))
        content = BoxLayout(orientation='vertical', size_hint_y=.7)
        # change show time
        label_slider = LabelTimeSlider(text='Initial Show time: %s s'%self.level)
        content.add_widget(label_slider)
        new_level = Slider(min=1, max=30, value=self.level)
        content.add_widget(new_level)
        new_level.bind(value=label_slider.update)
        new_level.bind(value=self.reset_time)

        # change number of items
        label_nb = LabelNb(text='Number of items: %s'%self.items)
        content.add_widget(label_nb)
        nb_items = Slider(min=5, max=MAX_NBITEMS, value=self.items)
        content.add_widget(nb_items)
        nb_items.bind(value=label_nb.update)
        nb_items.bind(value=self.reset_nb_item)
       
        content2.add_widget(content)

        replay_btn = Button(text='Replay!')
        credits_btn = Button(text='Credits')
        action = BoxLayout(orientation='horizontal', size_hint_y=.3)
        action.add_widget(replay_btn)
        action.add_widget(credits_btn)
        content2.add_widget(action)

        if self.score[0] > self.score[1]:
            greeting = "Congratulations!"
        elif self.score[1] > self.score[0]:
            greeting = "Oh no! You've been defeated."
        else:
            greeting = "What a game, it was a tie!"

        popup = PopupGameOver(title=greeting + ' Your score was: %s' % str(score),
                              content=content2,
                              size_hint=(0.5, 0.5), pos_hint={'x': 0.25, 'y': 0.25},
                              auto_dismiss=False)

        replay_btn.bind(on_press=popup.replay)
        replay_btn.bind(on_press=self.restart_game)
        credits_btn.bind(on_press=popup.credits)
        
        popup.open()


class ScrollableLabel(ScrollView):
   
    """
   use it thisly -> scrollablelabel = ScrollableLabel().build("put your big bunch of text right here")
       or
   ScrollableLabel().build() <- thusly with no argument to just get a very big bunch of text as a demo
   
   scrolls x and y default
    """
    def __init__(self):
        self.summary_label = Label(text="")

        self.sv = ScrollView(do_scroll_x=False)
        # it does not scroll the scroll view.

    def build(self, textinput, size):

        self.summary_label = Label(text="", text_size=(size, None),
                                   size_hint_y=None, size_hint_x=None)
       
        self.summary_label.bind(texture_size=self._set_summary_height)
        # remove the above bind
        self.summary_label.text = str(textinput)
       
        self.sv.add_widget(self.summary_label)
       
        return self.sv
   
    def _set_summary_height(self, instance, size):
        instance.height = size[1]
        instance.width = size[0]


class PopupGameOver(Popup):

    def replay(self, inst):
        self.dismiss()

    def credits(self, inst):
        
        with open(join(dirname(__file__), 'credits'), 'r') as f:
            ti = f.read()
        content = BoxLayout(orientation='vertical')
        close = Button(text='Close', size_hint=(1, .1))
        sv = ScrollableLabel().build(ti, Window.width-20)
        content.add_widget(sv)
        content.add_widget(close)
        popup = Popup(title='Credits:',
                      content=content, auto_dismiss=False
                      )
        close.bind(on_press=popup.dismiss)
        popup.open()


class ProSoccerMemApp(App):
        
    def build(self):

        self.icon = 'memoIcon.png'
        self.title = 'Pro Soccer Mem 15'
        global sounds, icons
        sounds, icons = load_data()
        # showmissingSounds()

        global MAX_NBITEMS
        MAX_NBITEMS = len(icons)
        items, level = load_level()
        g = MemoryLayout(rows=4, items=items, level=level, size_hint=(1,.9))
        config = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, .1))
        narrate_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, .1))
        
        sound = ToggleButton(text='Sound On', size_hint=(0.15, 1))
        sound.bind(on_press=MemoryButton.toggle_sound)

        pb = MyPb(max=items, size_hint=(0.55, 1), ml=g)
        
        timing = LabelTime(text="Time:  0 s", size_hint=(0.15, 1))
        score = LabelScore(text="Score:  0 - 0", size_hint=(0.15, 1))
        narration = LabelNarrate(text="Game has started!", size=(1, 1))

        narrate_box.add_widget(narration)
        config.add_widget(pb)
        config.add_widget(timing)
        config.add_widget(score)
        config.add_widget(sound)

        g.bind(narration=narration.update)
        g.bind(score=score.update)
        g.bind(elapsed=timing.update_time)
        g.bind(left=pb.found_an_item)
        g.bind(items=pb.new_nb_items)

        play_zone = BoxLayout(orientation='vertical')
        play_zone.add_widget(g)
        play_zone.add_widget(narrate_box)
        play_zone.add_widget(config)

        root = FloatLayout()
        root.add_widget(Image(source='court.jpg', allow_stretch=True, keep_ratio=False))
        root.add_widget(play_zone)
        # Clock.schedule_interval(g.initialCountdown,1)
        Clock.schedule_once(g.start_game, 3)

        return root

if __name__ in ('__main__', '__android__'):
    ProSoccerMemApp().run()
