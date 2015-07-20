import pdb
import time

import numpy as np
import moviepy.editor as mpy
import gizeh as gz
import random
import colorsys

W, H = 640, 260

surface = gz.Surface(W, H) # dimensions in pixel

txt = gz.text("AARONK", fontfamily="Franck Lloyd Extra",
              fontsize=120, fill=(0,0,0),xy=(W/2,H/2))
txt.draw(surface)

surface.get_npimage() # export as a numpy array (we will use that)
title = "_new/text " + time.ctime().replace(':','-') + ".png"
surface.write_to_png(title) # export as a PNG