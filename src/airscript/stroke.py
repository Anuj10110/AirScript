class Stroke:
    """Stores the points that make up one continuous stroke."""

    def __init__(self):
        # A list to remember every point in this stroke.
        self.points = []

    def add_point(self, x, y):
        """Add a fingertip position to the stroke."""
        self.points.append((x, y))

    def get_points(self):
        """Return all points in this stroke."""
        return self.points

    def is_empty(self):
        """Check whether the stroke contains any points."""
        return len(self.points) == 0
