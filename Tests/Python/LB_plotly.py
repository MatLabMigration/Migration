import plotly.graph_objects as go
import numpy as np

# Generating data points
num_points = 20
y1 = np.random.randint(5, 15, num_points)  # Oxygen levels
y2 = np.random.randint(70, 120, num_points)  # Blood pressure

# Create traces for oxygen levels and blood pressure
trace1 = go.Scatter(y=y1, mode='lines+markers', name='Zuurstof', line=dict(color='blue'))
trace2 = go.Scatter(y=y2, mode='lines+markers', name='Bloeddruk', line=dict(color='red'))

# Create layout with axis labels and title
layout = go.Layout(
    title='Zuurstof en bloeddruk (Plotly)',
    xaxis=dict(title='Tijd'),
    yaxis=dict(title='Waarde'),
    showlegend=True,
    hovermode='closest'
)

# Create figure and plot
fig = go.Figure(data=[trace1, trace2], layout=layout)
fig.show()
