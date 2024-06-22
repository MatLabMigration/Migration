using PlotlyJS
using Random

# Generate random data points
num_points = 20
x = 1:num_points
y1 = rand(5:15, num_points)  # Oxygen levels
y2 = rand(70:120, num_points)  # Blood pressure

# Create scatter traces for oxygen levels and blood pressure
trace1 = scatter(
    x = collect(x),
    y = y1,
    mode = "markers+lines",
    name = "Zuurstof",
    marker_color = "blue"
)

trace2 = scatter(
    x = collect(x),
    y = y2,
    mode = "markers+lines",
    name = "Bloeddruk",
    marker_color = "red"
)

# Create layout for the plot
layout = Layout(
    title = "Zuurstof en bloeddruk",
    xaxis_title = "Tijd",
    yaxis_title = "Waarde",
    legend = attr(x = 0, y = 1),
    hovermode = "closest"
)

# Create Plotly plot
plotly_plot = Plot([trace1, trace2], layout)

# Display the plot in the default web browser
display(plotly_plot)
