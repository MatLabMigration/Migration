using Gadfly
using Random

# Willekeurige gegevens genereren
num_points = 20
x = 1:num_points
y1 = rand(5:15, num_points)  # Zuurstofniveaus
y2 = rand(70:120, num_points)  # Bloeddruk

# DataFrame aanmaken met de gegevens
df = DataFrame(
    Tijd = collect(x),
    Zuurstof = y1,
    Bloeddruk = y2
)

# Interactieve scatter plot maken met Gadfly
scatter_plot = plot(
    df,
    x=:Tijd,
    y=:Zuurstof,
    Geom.point,
    color=:Tijd,
    Guide.xlabel("Tijd"),
    Guide.ylabel("Zuurstof"),
    Guide.title("Interactieve Scatter Plot (Zuurstof)")
)

# Weergave van de scatter plot
display(scatter_plot)
