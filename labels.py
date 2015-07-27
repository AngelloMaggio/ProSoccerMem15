__author__ = 'angellomaggio'

from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import game_tools

class LabelTime(Label):
    def update_time(self, instance, value):
        self.text = "Time: %0.2f s" % value


class LabelScore(Label):
    def update(self, instance, value):
        self.text = "Score: %d - %d" % (value[0], value[1])


class LabelTimeSlider(Label):
    def update(self, instance, value):
        self.text = "Initial Thinking time: %d s" % int(value)


class LabelNb(Label):
    def update(self, instance, value):
        self.text = "Number of players: %d" % int(value)


class LabelNarrate(Label):
    def update(self, instance, value):
        self.text = game_tools.narrate(value)


class MyPb(ProgressBar):
    def found_an_item(self, instance, value):
        self.value = value

    def new_nb_items(self, instance, value):
        self.value = value
        self.max = value
