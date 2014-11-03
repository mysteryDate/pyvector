import pdb

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
# import colorsys

R = 256

ROTATION_SPEED, DURATION = 1, 5

def make_frame(t):
    surface = gz.Surface(R, R)
    background = gz.square(l=R, xy= [R/2,R/2], fill=(1,1,1))
    background.draw(surface)
    cir = gz.circle(R/2, stroke=(1,1,1), fill=(0, 1, 0, 0.5), stroke_width=1, xy=[R/2, R/2])
    tri = gz.regular_polygon(R/2, 3, stroke=(1,1,1), fill=(1, 0, 0, 0.5), stroke_width=1, xy=[R/2, R/2], angle=2*t/DURATION*np.pi)
    sqr = gz.square(R/2, stroke=(1,1,1), fill=(0, 0, 1, 0.5), stroke_width=1, xy=[R/2, R/2], angle=-2*t/DURATION*np.pi)
    grp = gz.Group([cir, tri, sqr])
    grp.draw(surface)
    im = surface.get_npimage()
    return im

clip = mpy.VideoClip(make_frame, duration=DURATION)
clip.write_gif("moving_shapes.gif",fps=60, opt="OptimizePlus", fuzz=10)
