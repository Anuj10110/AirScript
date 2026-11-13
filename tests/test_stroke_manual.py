
from airscript.stroke import Stroke


# Create a new stroke.
stroke = Stroke()

print("Is the stroke empty?", stroke.is_empty())

# Add three fingertip positions.
stroke.add_point(0.30, 0.20)
stroke.add_point(0.32, 0.25)
stroke.add_point(0.35, 0.30)

# Display the stored points.
print("Stroke points:", stroke.get_points())
print("Is the stroke empty?", stroke.is_empty())
print("Number of points:", len(stroke.get_points()))
