import random
import numpy as np
from turtle import Turtle, setup, done, tracer, clear
import sys
import time

def set_axis(n: int, prob: float) -> np.ndarray:
    """
    Return array of length n with 1 at probability prob and 0 otherwise"""
    axis = np.zeros(n,dtype=int)
    random.seed()
    for i, _val in enumerate(axis):
        rand = random.random()
        if prob > rand:
            axis[i] = 1
    return axis

def draw_set(axes):
    n = axes.shape[0]
    spacing = 500./(n+1) # margin of one half spacing
    t = Turtle()
    t.hideturtle()
    setup(500,500)
    tracer(False)
    for col_num in range(axes.shape[1]):
        t.penup()
        t.setposition(-250+spacing/2,-250+spacing/2)
        t.pendown()
        ax = axes[:,col_num]
        if col_num == 0:
            # vertical axis
            for index, val in enumerate(ax):
                if index%2 == 0:
                    if val == 1:
                        for i in range(int(n/2)):
                            t.pencolor('black')
                            t.forward(spacing)
                            t.pencolor('white')
                            t.forward(spacing)
                    else:
                        for i in range(int(n/2)):
                            t.pencolor('white')
                            t.forward(spacing)
                            t.pencolor('black')
                            t.forward(spacing)
                    t.penup()
                    t.left(90)
                    t.forward(spacing)
                    t.left(90)
                    t.pendown()
                else:
                    if val == 0:
                        for i in range(int(n/2)):
                            t.pencolor('black')
                            t.forward(spacing)
                            t.pencolor('white')
                            t.forward(spacing)
                    else:
                        for i in range(int(n/2)):
                            t.pencolor('white')
                            t.forward(spacing)
                            t.pencolor('black')
                            t.forward(spacing)
                    t.penup()
                    t.right(90)
                    t.forward(spacing)
                    t.right(90)
                    t.pendown()
        if col_num == 1:
            t.left(90)
            # vertical axis
            for index, val in enumerate(ax):
                if index%2 == 0:
                    if val == 1:
                        for i in range(int(n/2)):
                            t.pencolor('black')
                            t.forward(spacing)
                            t.pencolor('white')
                            t.forward(spacing)
                    else:
                        for i in range(int(n/2)):
                            t.pencolor('white')
                            t.forward(spacing)
                            t.pencolor('black')
                            t.forward(spacing)
                    t.penup()
                    t.right(90)
                    t.forward(spacing)
                    t.right(90)
                    t.pendown()
                else:
                    if val == 0:
                        for i in range(int(n/2)):
                            t.pencolor('black')
                            t.forward(spacing)
                            t.pencolor('white')
                            t.forward(spacing)
                    else:
                        for i in range(int(n/2)):
                            t.pencolor('white')
                            t.forward(spacing)
                            t.pencolor('black')
                            t.forward(spacing)
                    t.penup()
                    t.left(90)
                    t.forward(spacing)
                    t.left(90)
                    t.pendown()
    time.sleep(0.2)
    clear

if __name__ == '__main__':
    n = int(input('Axis length: '))
    one_prob = float(input('Initial probability of \"on\" state: '))
    # for now, let's go with square axis
    dim = 2
    axes = np.zeros((n,dim),dtype=int)
    while True:
        for i in range(dim):
            axes[:,i] = set_axis(n,one_prob)
        draw_set(axes)
        one_prob = random.random()