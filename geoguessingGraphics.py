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
        "POLAND" : (-25, 108),
        "KENYA" : (15, -10),
        "SENEGAL" : (-80, 13),
        }

    def go(self, country):
        self.pin.goto(self.locations[country])
        self.win.update()


    win.update()
    turtle.done()
