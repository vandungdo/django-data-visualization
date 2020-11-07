import matplotlib.pyplot as plt
import os
import glob

baseDir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'static')
baseDir = os.path.join(baseDir,'plots')

def static_bar_plot(x,y):
    # for root, dirs, files in os.walk(baseDir):
    #     for file in files:
    #         os.remove(os.path.join(root, file))
    x = x.split(',')
    y = y.split(',')
    y = [float(i) for i in y]

    fig = plt.figure()
    plt.bar(x,y)
    plt.title('static bar plot')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.tight_layout()
    plt.savefig(os.path.join(baseDir,'tmp.png'))
    
def static_scatter_plot(x,y):
    # for root, dirs, files in os.walk(baseDir):
    #     for file in files:
    #         os.remove(os.path.join(root, file))
    x = x.split(',')
    y = y.split(',')
    y = [float(i) for i in y]

    fig = plt.figure()
    plt.scatter(x,y)
    plt.title('static scatter plot')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.tight_layout()
    plt.savefig(os.path.join(baseDir,'tmp.png'))

def static_line_plot(x,y):
    # for root, dirs, files in os.walk(baseDir):
    #     for file in files:
    #         os.remove(os.path.join(root, file))
    x = x.split(',')
    y = y.split(',')
    y = [float(i) for i in y]

    fig = plt.figure()
    plt.plot(x,y)
    plt.title('static line plot')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.tight_layout()
    plt.savefig(os.path.join(baseDir,'tmp.png'))

def static_pie_plot(x,y):
    # for root, dirs, files in os.walk(baseDir):
    #     for file in files:
    #         os.remove(os.path.join(root, file))
    x = x.split(',')
    y = y.split(',')
    y = [float(i) for i in y]

    fig = plt.figure()
    plt.pie(y, labels=x,autopct='%1.1f%%')
    plt.title('static pie plot')
    plt.tight_layout()
    plt.savefig(os.path.join(baseDir,'tmp.png'))

def delete_file():
    files = os.listdir(baseDir)
    print(baseDir)
    print(files)
    for file in files:
        os.remove(os.path.join(baseDir,file))
        print(file)