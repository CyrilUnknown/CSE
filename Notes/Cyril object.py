class Projector(object):
    def __init__(self):
        self.exterior = "Buttons"
        self.cover = "Slider"
        self.lens = "Short Throw, Long Throw"
        self.interior = "Filter"
        self.vent = "Fan"
        self.isShowing = False

    def turn_on(self):
        self.isShowing = True

    def turned_off(self):
        self.isShowing = False

        print("I turn the projector on.")
        print("The projector turns on youtube by it self.")
        print("and it turn's off by it self")


projector = Projector()
projector.turn_on()
projector.turned_off()