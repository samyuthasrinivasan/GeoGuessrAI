import turtle

class Graphics():
    win = turtle.Screen()
    win.setup(800,400)
    win.bgpic("worldMap10.gif")
    win.tracer(0)

    pin = turtle.Turtle(shape = "triangle")
    pin.speed(0)
    pin.pencolor('red')
    pin.fillcolor('red')
    pin.pu()
    pin.right(90)

    locations = {
        "SPAIN" : (-60, 85),
        "SENEGAL" : (-80, 13),
        }

    def go(self, country):
        self.pin.goto(self.locations[country])
        self.goWrite(country)
        self.win.update()
        turtle.done()

    def goWrite(self, country):
        t = turtle.Turtle(shape = "blank")
        t.pu()
        t.speed(0)
        t.goto(260, 150)
        t.pd()
        t.write(f"GUESS: {country.upper()}", font=("Arial", 16, "normal"), align = "right")

    win.update()
