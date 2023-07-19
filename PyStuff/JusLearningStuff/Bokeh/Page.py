import math
import numpy
from bokeh.plotting import *

x=numpy.arange(0, math.pi*2, 0.05)
y=numpy.sin(x)

output_file('Graph.html')
p=figure(title='SinGraph', x_axis_label='x', y_axis_label='y')
p.line(x,y,line_width=2)
show(p)
