
import random
from graphics import *
from math import sin, cos, radians
width = 800; height = 600
w = GraphWin("Ghost Tree - Tim Goodwin, 2013.",width,height)
w.setBackground("black")
start = width/2, 0
L = random.randrange(height/6, height/4)
theta = 90
hue = 218
end = width/2, 0 + L
trunkWidth = 8
#print stop, start
trunk = Line(Point(start[0], width-start[1]), Point(end[0], height-end[1]))
trunk.setFill(color_rgb(hue,hue,hue))
trunk.setWidth(trunkWidth)
trunk.draw(w)
    
    
def branch(w, start, Length, oldAngle, oldColor, trunkWidth, height):
    L = random.randint(Length/2, Length)
    angle = oldAngle + random.randint(-30,30)
    x = oldColor - 20
    end = int(start[0] + L * cos(radians(angle))), int(start[1] + L * sin(radians(angle)))
    stem = Line(Point(start[0], height - start[1]), Point(end[0], height - end[1]))
    stem.setFill(color_rgb(x,x,x+18))
    stem.setWidth(trunkWidth)
    stem.draw(w)
    if trunkWidth == 1:
        return
    else:
        branch(w, end, L, angle, x, trunkWidth - 1, height)
        branch(w, end, L, angle, x, trunkWidth - 1, height)
        branch(w, end, L, angle, x, trunkWidth - 1, height)        

    
def main():
    branch(w, end, L, theta, hue, trunkWidth - 1, height)
    branch(w, end, L, theta, hue, trunkWidth - 1, height)
    branch(w, end, L, theta, hue, trunkWidth - 1, height)


    pause = raw_input()
if __name__ == "__main__":
    main()  