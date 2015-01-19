from colorsys import rgb_to_hls,hls_to_rgb
from math import sin,cos,atan2,pi

def average_colors2(rgb1, rgb2):
    h1, l1, s1 = rgb_to_hls(rgb1[0]/255., rgb1[1]/255., rgb1[2]/255.)
    h2, l2, s2 = rgb_to_hls(rgb2[0]/255., rgb2[1]/255., rgb2[2]/255.)
    s = 0.5 * (s1 + s2)
    l = 0.5 * (l1 + l2)
    x = cos(2*pi*h1) + cos(2*pi*h2)
    y = sin(2*pi*h1) + sin(2*pi*h2)
    if x != 0.0 or y != 0.0:
        h = atan2(y, x) / (2*pi)
    else:
        h = 0.0
        s = 0.0
    r, g, b = hls_to_rgb(h, l, s)
    return (r*255., g*255., b*255.)


def average_colors(*rgb):
	rgb1 = average_colors2(rgb[0], rgb[1])
	if len(rgb) > 3:
		return average_colors(rgb1, *rgb[2:])
	else:
		return rgb1

c1 = (255.,255.,255.)
c2 = (247.,247.,240.)
c3 = (255., 0, 0)
c4 = (242., 10., 37.)

ac3 = average_colors(c1, c2, c3, c4)

print(ac3)
