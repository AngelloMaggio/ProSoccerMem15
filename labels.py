__author__ = 'angellomaggio'

from kivy.uix.label import Label


class LabelTime(Label):
    def update_time(self, instance, value):
        self.text = "Time: %0.2f s" % value


class LabelScore(Label):
    def update(self, instance, value):
        self.text = "Score: %d - %d" % (value[0], value[1])