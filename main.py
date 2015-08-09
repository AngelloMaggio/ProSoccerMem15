__author__ = 'Angello Maggio'

"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""

import kivy
kivy.require('1.0.9')
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.floatlayout import FloatLayout
from memory import *
from game_tools import *
from kivy.uix.screenmanager import ScreenManager, Screen

__version__ = '0.3.5'


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    def on_enter(self):
        g.start_game(3)


class CreditsScreen(Screen):
    def on_enter(self):
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
        close.bind(on_release=popup.dismiss)
        close.bind(on_press=lambda _: go_back(sm))
        popup.open()


class ProSoccerMemApp(App):
        
    def build(self):

        # Title and icon for program
        self.icon = 'memoIcon.png'
        self.title = 'Pro Soccer Mem 15'

        items, level = load_level()
        global g
        g = MemoryLayout(rows=4, items=items, level=level, size_hint=(1, .9))
        config = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, .1))
        narrate_box = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, .1))

        sound = ToggleButton(text='Sound On', size_hint=(0.15, 1))
        sound.bind(on_press=MemoryButton.toggle_sound)

        pb = MyPb(max=items, size_hint=(0.55, 1), ml=g)

        timing = LabelTime(text="Time:  0 s", size_hint=(0.15, 1))
        score = LabelScore(text="Score:  0 - 0", size_hint=(0.15, 1))
        narration = LabelNarrate(text="Welcome to Pro Soccer Mem 15. Loading...", size=(1, 1))

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

        # Screen manager
        sm = ScreenManager()
        global sm
        settings_screen = SettingsScreen(name='settings')
        settings_screen.add_widget(root)

        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CreditsScreen(name='credits'))

        sm.add_widget(settings_screen)

        return sm

if __name__ in ('__main__', '__android__'):
    ProSoccerMemApp().run()
