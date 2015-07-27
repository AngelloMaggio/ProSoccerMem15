__author__ = 'Angello Maggio'

"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""

from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView

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
        self.text = value


class MyPb(ProgressBar):
    def found_an_item(self, instance, value):
        self.value = value

    def new_nb_items(self, instance, value):
        self.value = value
        self.max = value


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