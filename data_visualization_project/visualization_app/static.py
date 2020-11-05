import matplotlib.pyplot as plt
import os

baseDir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'static')
baseDir = os.path.join(baseDir,'plots')

def bar_plot(x,y):
    x = x.split(',')
    y = y.split(',')
    y = [float(i) for i in y]

    fig = plt.figure()
    plt.bar(x,y)
    plt.title('bar plot')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.tight_layout()
    plt.savefig(os.path.join(baseDir,'tmp.png'))
    