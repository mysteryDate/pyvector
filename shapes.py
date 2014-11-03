import numpy as np
import moviepy.editor as mpy
import colorsys
import gizeh as gz
import pdb

W,H = 256, 256

surface = gz.Surface(W, H) # dimensions in pixel
# triangle = gz.regular_polygon (r=W/2, # radius, in pixels
#                         angle=np.pi/6,
#                         n = 3,
#                        xy= [W/2, H/2], # coordinates of the center
#                        stroke= (0,0,0), stroke_width=1) # 'red' in RGB coordinates

# triangle.draw( surface ) # draw the triangle on the surface

# square = gz.square(W/4, stroke=(0,0,0), stroke_width = 1, xy= [W/2, H/2])

# square.draw( surface )

# circle = gz.circle(W/8, stroke=(0,0,0), stroke_width = 1, xy= [W/2, H/2])
# circle.draw(surface)

tri = gz.regular_polygon(W/2, 3, stroke=(0,0,0), stroke_width=1, xy=[W/2, H/2])
cir = gz.circle(W/2, stroke=(0,0,0), stroke_width=1, xy=[W/2, H/2])
sqr = gz.square(W/2, stroke=(0,0,0), stroke_width=1, xy=[W/2, H/2])
grp = gz.Group([tri, cir, sqr])
grp.draw(surface)

# surface.get_npimage() # export as a numpy array (we will use that)
surface.write_to_png("shapes.png")

# NFACES, R, NSQUARES, DURATION = 3, 0.3,  70, 10

# def half(t, side="left"):
#     # pdb.set_trace()
#     points = gz.geometry.polar_polygon(NFACES, R, NSQUARES)
#     ipoint = 0 if side=="left" else NSQUARES/2
#     points = (points[ipoint:]+points[:ipoint])[::-1]

#     surface = gz.Surface(W,H)
#     background = gz.square(l=W, xy= [W/2,H/2], fill=(1,1,1))
#     background.draw(surface)
#     direction = np.sin(2*np.pi/DURATION*t)
#     # direction = -1
#     # direction = 0
#     for (r, th, d) in points:
#         center = W*(0.5+gz.polar2cart(r,th))
#         angle = direction*(6*np.pi*d + t*np.pi/DURATION)
#         color= colorsys.hls_to_rgb((2*d+t/DURATION)%1,.5,.5)
#         square = gz.square(l=0.17*W, xy= center, angle=angle,
#                    fill=color, stroke_width= 0.005*W, stroke=(1,1,1))
#         square.draw(surface)
#     im = surface.get_npimage()
#     # pdb.set_trace()
#     return (im[:,:W/2] if (side=="left") else im[:,W/2:])


# def make_frame(t):
#     return np.hstack([half(t,"left"),half(t,"right")])

# clip = mpy.VideoClip(make_frame, duration=DURATION)

# clip.write_gif(""+str(NFACES)+"sided_"+str(R)+"R_"+str(NSQUARES)+"NSQURES_"+str(DURATION)+"DurationUltraLOW.gif",fps=60, opt="OptimizePlus")