import matplotlib.pyplot as plt
import os

baseDir = os.path.join(os.path.dirname(__file__),'plots')

def bar_plot(x,y):
    x = x.split(',')
    y = y.split(',')
    y = [float(i) for i in y]

    fig = plt.figure()
    plt.bar(x,y)
    plt.savefig(os.path.join(baseDir,'tmp.png'))
    