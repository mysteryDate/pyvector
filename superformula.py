import pdb
import time

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
import random
import colorsys
import pytweening

R = 256

DURATION = 5

NPOINTS = 256

A, B, M, N1, N2, N3 = 1, 1, 6, 1, 1, 6

def sf(a, b, m, n1, n2, n3, theta):
	ans =  np.power( np.abs( np.cos(m * theta / 4) /a ), n2)
	ans += np.power( np.abs( np.sin(m * theta / 4) /b ), n3)
	ans =  np.power( ans, -1.0 / n1 )
	return ans

def make_frame(t):
    surface = gz.Surface(R, R)
    background = gz.square(l=R, xy= [R/2,R/2], fill = (1,1,1,1))
    background.draw(surface)
    points = []
    a = A * t / DURATION
    b = B * t / DURATION
    m = M * t / DURATION
    n1 = N1 * (t + 1.0) / DURATION
    n2 = N2 * t / DURATION
    n3 = N3 * t / DURATION
    for i in range(NPOINTS):
    	theta = 2 * np.pi * i / NPOINTS
    	r = sf(A, B, M, N1, n2, n3, theta) * R/4
    	points.append((r * np.cos(theta), r * np.sin(theta)))
    line = gz.polyline(points, stroke=(0,0,0,1), stroke_width=0.4)
    line.translate([R/2,R/2]).draw(surface)
    im = surface.get_npimage()
    return im

title = "_new/wait " + time.ctime().replace(':','-') + ".gif"
clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("_new/superformula.gif",fps=24, opt="OptimizePlus", fuzz=10)