import turtle

win = turtle.Screen()
win.setup(800,400)
win.bgpic("/Users/bartavius/Downloads/worldMap10.gif")
win.tracer(0)

pin = turtle.Turtle(shape = "triangle")
pin.speed(0)
pin.pencolor('red')
pin.fillcolor('red')
pin.pu()
pin.right(90)

locations = {
    "spain" : (-60, 85),
    "poland" : (-25, 108),
    "kenya" : (15, -10),
    "senegal" : (-80, 13),
    }

def go(country):
    pin.goto(locations[country])
    win.update()


win.update()
