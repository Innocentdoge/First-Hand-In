import matplotlib.pyplot as plt
import numpy as np
from re import search
from matplotlib.widgets import TextBox, Button


#fig = plt.figure()

#prediction_text = ''
input_text = ''


def funcCheck():
    if search(r'\d+\*x|x\*\d', input_text):
        # prediction_text = '1*x'
        print("This is a Linear function.")
    elif search(r'x\*\*2', input_text):
        # prediction_text = 'x**2'
        print("This is a Square function.")
    elif search(r'x\*\*3', input_text):
        print('This is a Cube function.')
    elif search(r'\d+/x', input_text):
        print('This is a Reciprocal function.')
    elif search(r'\d+\*\*x', input_text):
        print('This is a Exponential function.')
    else:
        print('Could not predict.')


#if input_text.find('x**1'):
#    prediction_text = 'x**1'
#elif input_text.find('*x'):
#    prediction_text = '1*x'
#elif input_text.find('x**'):
#    prediction_text = 'x**2'


x = np.linspace(0, 2, 200)
y = np.exp(x)
l, = plt.plot(x, y, 'y', label=input_text, color='green')
#p, = plt.plot(x, y, 'y', label=prediction_text, color='orange')


def submit(text):
    y_data = eval(text)
    l.set_ydata(y_data)
    plt.draw()
    funcCheck()
    print(input_text)


amp = plt.axes([0.35, 0.03, 0.3, 0.04])
exInput = TextBox(amp, label='Input y=', initial=input_text)
exInput.on_submit(submit)
plt.legend(loc="upper left", bbox_to_anchor=(-.7, 20))

plt.grid()
plt.show()
