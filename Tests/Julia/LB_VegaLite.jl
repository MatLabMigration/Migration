using DataFrames
using VegaLite

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

# Interactieve scatter plot maken met VegaLite
scatter_plot = @vlplot(
    mark=:point,
    data=df,
    x=:Tijd,
    y=:Zuurstof,
    color=:Tijd,
    tooltip=[{field=:Zuurstof, title="Zuurstof"}, {field=:Tijd, title="Tijd"}]
) + @vlplot(
    mark=:point,
    data=df,
    x=:Tijd,
    y=:Bloeddruk,
    color=:Tijd,
    tooltip=[{field=:Bloeddruk, title="Bloeddruk"}, {field=:Tijd, title="Tijd"}]
)

# Weergave van de scatter plot
display(scatter_plot)
