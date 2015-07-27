__author__ = 'angellomaggio'

from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ListProperty
from random import choice, shuffle
from os.path import sep
from narrator import narrate
from kivy.uix.button import Button
from kivy.clock import Clock
from game_tools import *
from labels import *
from config import *
from kivy.uix.popup import Popup
from kivy.core.window import Window

sounds, icons = load_data()
MAX_NBITEMS = len(icons)


class MemoryButton(Button):

    filenameSound = StringProperty(None)
    filenameIcon = StringProperty(None)
    sound = ObjectProperty(None)
    background = ObjectProperty(None)
    background_hide = ObjectProperty(None)
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

                    self.parent.ball_position, self.parent.narration = narrate(self.parent.ball_position, True)

                    if self.parent.ball_position > 3:
                        self.parent.score = self.parent.score[0]+1, self.parent.score[1]
                        self.parent.ball_position = 0
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
                    self.parent.ball_position, self.parent.narration = narrate(self.parent.ball_position, False)
                    if self.parent.ball_position < -3:
                        self.parent.score = self.parent.score[0], self.parent.score[1]+1
                        self.parent.ball_position = 0
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
        Clock.schedule_once(self.start_game, 3)

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
        # Clock.schedule_interval(self.initial_countdown, 1)
        self.game_over(True)

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
        self.narration = "Game has started!"

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

    def game_over(self, game_starting=False):

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
        if game_starting:
            replay_btn = Button(text='Play!')
            self.narration = "Ready to play?"
        else:
            self.narration = "What a game!"
            replay_btn = Button(text='Replay!')
        credits_btn = Button(text='Credits')
        action = BoxLayout(orientation='horizontal', size_hint_y=.3)
        action.add_widget(replay_btn)
        action.add_widget(credits_btn)
        content2.add_widget(action)

        if game_starting:
            greeting = "Welcome to Pro Soccer Mem 15. Choose your game mode:"
        elif self.score[0] > self.score[1]:
            greeting = "Congratulations!" + ' Your score was: %s' % str(score)
        elif self.score[1] > self.score[0]:
            greeting = "Oh no! You've been defeated." + ' Your score was: %s' % str(score)
        else:
            greeting = "What a game, it was a tie!" + ' Your score was: %s' % str(score)

        popup = PopupGameOver(title=greeting,
                              content=content2,
                              size_hint=(0.5, 0.5), pos_hint={'x': 0.25, 'y': 0.25},
                              auto_dismiss=False)

        replay_btn.bind(on_press=popup.replay)
        replay_btn.bind(on_press=self.restart_game)
        credits_btn.bind(on_press=popup.credits)
        popup.open()


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

