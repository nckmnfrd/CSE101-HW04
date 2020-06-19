#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8
#Homework 4


from turtle import *
import random
ryan = Turtle()
ryan.speed(1000)
screen = ryan.getscreen()


def clearWindow():
    ryan.penup()
    ryan.goto(-1000,1000)
    ryan.pendown()
    ryan.color("light gray", "light gray")
    ryan.begin_fill()
    ryan.goto(1000,1000)
    ryan.goto(1000,-1000)
    ryan.goto(-1000,-1000)
    ryan.goto(-1000,1000)
    ryan.end_fill()
    ryan.penup()


def getNextColorInfo(string):
    colors = ["black", 'white', 'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'purple' ]
    space = string.find(" ")
    color = colors[int (string[:space])]
    string = string[space + 1:]
    space = string.find(" ")
    if space == -1:
        return ("", color, int (string))
    quantity = string[:space]
    string = string[space + 1:]
    return (string, color, int (quantity))

def drawBox(x,y,width,height,color):
    ryan.penup()
    ryan.goto(x,y)
    ryan.pendown()
    ryan.color("black",color)
    ryan.begin_fill()
    ryan.goto(x+width,y)
    ryan.goto(x+width,y+height)
    ryan.goto(x,y+height)
    ryan.goto(x,y)
    ryan.end_fill()
    ryan.penup()

def getPictureData(name):
    myFile = open(name)
    x = 0
    y = 0
    blockSize = 30
    for line in myFile:
        line = line.strip()
        while line:
            line, color, quantity = getNextColorInfo(line)
            for i in range (0, quantity):
                drawBox(x, y, blockSize, blockSize, color)
                x += blockSize
        y -= blockSize
        x = 0
            


clearWindow()

getPictureData(textinput("Open File", "Enter File Name: "))






    




















