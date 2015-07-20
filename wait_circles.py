import pdb
import time

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
import random
import colorsys
import pytweening

R = 256

NCIRCLES, NROTATIONS, DURATION = 3, 1, 2

def make_frame(t):
    surface = gz.Surface(R, R)
    background = gz.square(l=R, xy= [R/2,R/2], fill = (1,1,1,1))
    background.draw(surface)
    r = R/4
    ith = -np.pi/2
    C = pytweening.easeInOutSine(t/DURATION)
    # C = t/DURATION
    for i in range(NCIRCLES):
		th = ith + (i+1)*(2*np.pi*NROTATIONS) * C
		center = gz.polar2cart(R/4,th)
		color = (1.0,1.0,1.0,1.0/255)
		if i % 3 == 0:
			color = (1.0,0,0,1.0/255)
		elif i % 3 == 1:
			color = (0,1.0,0,1.0/255)
		else:
			color = (0,0,1.0,1.0/255)
		cir = gz.circle(R/4 - (i/4), fill=color, xy=center)
		cir.translate([R/2,R/2]).draw(surface)
    im = 255*((surface.get_npimage()) % 2)
    return im

# title = "_new/wait " + time.ctime().replace(':','-') + ".gif"
clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("_new/wait.gif",fps=60, opt="OptimizePlus", fuzz=10)