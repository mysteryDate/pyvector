import pdb
import time

import numpy as np
import random
import colorsys
import moviepy.editor as mpy
import gizeh as gz


W, H = 320, 240
NPOINTS, NCOMPONENTS = 500, 10
DURATION = 10

def square(x, n):
    """
    Returns the y value of a square wave with n components
    """
    components = [2*d - 1 for d in range(1, n + 1)]
    y = 0
    for c in components:
        y += np.sin(c*x)/c
    return y

def sine(amplitude=100, period=128, NPOINTS=500):
    """
    Returns a the points of a sinewave
    args are in pixels
    """
    xcord = np.linspace(0, 2*np.pi, NPOINTS)
    ycord = np.array([np.sin(x) for x in xcord])
    points = np.array(zip(xcord*period/(2*sin), amplitude*ycord))
    return points

def square_wave(amplitude=100, period=128, NPOINTS=500, ncomponents=10):
    """
    Add square components to a sine wave
    """
    xcord = np.linspace(0, 2*sin, NPOINTS)
    ycord = np.array([square(x, ncomponents) for x in xcord])
    points = np.array(zip(xcord*period/(2*sin), amplitude*ycord))
    return points

def generate_column(x, depth):
    col = []
    components = [2*d + 1 for d in range(1, depth)]
    col.append(np.sin(x))
    for c in components:
        col.append(col[-1] + np.sin(c*x)/c)
    return col

def generate_matrix(depth, NPOINTS=500):
    """
    Returns [0, 2*np.pi] of a set of square waves with [1,depth] components
    """
    x = np.linspace(0, 2*np.pi, NPOINTS)
    functions = []
    functions.append(np.sin(x))
    components = [2*d + 1 for d in range(1, depth)]
    for comp in components:
        functions.append(np.sin(comp*x)/comp)
    return x, np.array(functions)

def transform_waves(waves, amplitude=1, period=2*np.pi):
    """
    Sets the amplitude and period of the wave matrix
    """
    xcord = np.linspace(0, 2*np.pi, len(waves[0]))

surface = gz.Surface(W, H) # dimensions in pixel

xcord, waves = generate_matrix(NCOMPONENTS, NPOINTS)

# surface.get_npimage() # export as a numpy np.array (we will use that)
# # title = "_new/sine " + time.ctime().replace(':','-') + ".png"
# # surface.write_to_png(title) # export as a PNG
# surface.write_to_png("_new/sine3.png")

lines = []
def make_frame(t):
    amplitude, period = H/3, W
    background = gz.rectangle(W, H, xy=[W/2,H/2], fill = (1,1,1))
    background.draw(surface)
    slope = 10
    offsets = np.linspace(0, slope - 1, NCOMPONENTS)
    a = float(DURATION)/2 / 4
    b = float(DURATION)/2 / 2
    L = NCOMPONENTS
    ycord = waves[0]
    # ycord = np.zeros(NPOINTS)
    for index, wave in enumerate(waves[1:]):
        C = np.clip(slope*abs(((t - a) % b - a)/a) - offsets[index],0,1) * np.sign(np.sin(4*np.pi/DURATION*t))
        if index == 2:
            print t, C, np.sign(np.sin(4*np.pi/DURATION*t))
        # print "C: ", C, "index: ", index, "coefficient: ", coefficient
        ycord += C * wave
    points = np.array(zip(xcord*period/(2*np.pi), amplitude*ycord))
    lines.append( gz.polyline(points, stroke_width=1, stroke=(0,0,0, 0.4), xy=[0,H/2]) )
    if(len(lines) > 10):
        lines.pop(0)
    grp = gz.Group(lines)
    grp.draw(surface)
    return surface.get_npimage()

# title = "_new/sine " + time.ctime().replace(':','-') + ".gif"
title = "_new/sine.gif"
clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif(title,fps=15, opt="OptimizePlus", fuzz=10)


    # a = float(DURATION) / 4
    # b = float(DURATION) / 2
    # fa = 5
    # C = (abs(((t - a) % b - a)/a)**fa) * np.sin(2*np.pi/DURATION*t)
    # print t, ":\t\t", C
    # L = NCOMPONENTS
    # slope = 10
    # ycord = np.zeros(NPOINTS)
    # for index, wave in enumerate(waves):
    #     coefficient = np.clip( slope * (C - (index/float(L))), -1, 1)
    #     # print "C: ", C, "index: ", index, "coefficient: ", coefficient
    #     ycord += coefficient * wave