class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal
    
    def get_picture(self):
        width_lines = '*' * self.width
        height_lines = f'{width_lines}\n' * self.height

        if (self.width > 50) or (self.height > 50):
            return 'Too big for picture'
        else:
            return height_lines
        
    
class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.height = width
        self.height = width
        

    

rect = Rectangle(10, 5)
rect.set_height(8)
rect.set_width(4)

rect2 = Rectangle(4, 4)

sq1 = Square(8)

print(rect.get_picture())