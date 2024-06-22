from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource
import numpy as np

# Generating data points
num_points = 20
x = np.arange(1, num_points + 1)
y1 = np.random.randint(5, 15, num_points)  # Oxygen levels
y2 = np.random.randint(70, 120, num_points)  # Blood pressure

# Create a ColumnDataSource with data for tooltips
source1 = ColumnDataSource(data=dict(
    x=x,
    y=y1,
    value=[f'{val:.2f}' for val in y1]  # Format values as strings for tooltips
))

source2 = ColumnDataSource(data=dict(
    x=x,
    y=y2,
    value=[f'{val:.2f}' for val in y2]  # Format values as strings for tooltips
))

# Create a new plot with a title and axis labels
p = figure(title='Zuurstof en bloeddruk', x_axis_label='Tijd', y_axis_label='Waarde')

# Add circles for oxygen levels with hover tooltips
circle1 = p.circle('x', 'y', source=source1, legend_label='Zuurstof', color='blue', size=8)
p.add_tools(HoverTool(renderers=[circle1], tooltips=[('Value', '@value')]))

# Add squares for blood pressure with hover tooltips
square1 = p.square('x', 'y', source=source2, legend_label='Bloeddruk', color='red', size=8)
p.add_tools(HoverTool(renderers=[square1], tooltips=[('Value', '@value')]))

# Connect data points with lines (oxygen levels)
p.line(x, y1, line_width=2, color='blue', legend_label='Zuurstof')

# Connect data points with lines (blood pressure)
p.line(x, y2, line_width=2, color='red', legend_label='Bloeddruk')

# Display legends on the plot
p.legend.location = 'top_left'

# Show the plot in the default web browser
show(p)
