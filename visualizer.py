import PySimpleGUI as sg
import turtle

"""
    Demo showing how to integrate drawing on a Canvas using  Turtle with PySimpleGUI
    The patern to follow:
        Create Window & Finalize
        Get the tkinter Canvas from the Canvas element
        Draw on the tkinter Canvas using turtle commands.
        Results are shown on the canvas immiedately after button press / drawing command
"""


layout = [[sg.Text('My layout')],
          [sg.Canvas(size=(500, 500), key='-canvas-')],
          [sg.Button('C'), sg.Button('D'), sg.Button('E'), sg.Button('F'), sg.Button('G'), sg.Button('A'), sg.Button('B')]]

window = sg.Window('My new window', layout, finalize=True)

canvas = window['-canvas-'].TKCanvas

trtl = turtle.RawTurtle(canvas)
trtl.pencolor("#ff0000")  # Red
trtl.penup()
trtl.pendown()
trtl.hideturtle();

while True:     # Event Loop
    event, values = window.read()
    if event is None:
        break

    if event == 'C':
        trtl.color('red');
    elif event == 'D':
        trtl.color('orange')
    elif event == 'E':
        trtl.color('gold')
    elif event == 'F':
        trtl.color('lawngreen')
    elif event == 'G':
        trtl.color('aqua')
    elif event == 'A':
        trtl.color('mediumblue')
    elif event == 'B':
        trtl.color('navy')
    elif event == 'C':
        trtl.color('darkorchid')
    else:
        trtl.color('black')


    trtl.speed(0)
    for i in range(50):
        trtl.circle(2 * i*.25)
        trtl.circle(-2 * i*.25)
        trtl.left(i)
window.close()