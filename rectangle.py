class Rectangle:
    def __init__(self, width, height, corner_x, corner_y):
        self.width = width
        self.height = height
        self.corner_x = corner_x
        self.corner_y = corner_y

    def find_center(self):
        # Center is calculated as midpoint of opposite corners
        center_x = self.corner_x + self.width / 2
        center_y = self.corner_y + self.height / 2
        # Return an instance representing the center
        return Rectangle(0, 0, center_x, center_y)

    def area(self):
        # Area of the rectangle
        return self.width * self.height

    def perimeter(self):
        # Perimeter of the rectangle
        return 2 * (self.width + self.height)

    def __str__(self):
        # String representation of the rectangle
        return f"Rectangle(width={self.width}, height={self.height}, corner=({self.corner_x}, {self.corner_y}))"

# Create a rectangle instance
rect = Rectangle(10, 20, 0, 0)

# Calculate and display area and perimeter
print(f"Area: {rect.area()}")  # Output: Area: 200
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 60

# Find and display the center
center = rect.find_center()
print(f"Center: ({center.corner_x}, {center.corner_y})")  # Output: Center: (5.0, 10.0)
