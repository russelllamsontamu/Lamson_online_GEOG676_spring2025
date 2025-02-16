#Creating the classes that we will use to read the text file and execute the code for the file info
class shape():
    def __init__(self):
        pass

class rectangle(shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def get_the_area(self):
        return self.length * self.width
    
class circle(shape):
    def __init__(self, r):
        self.radius = r
    def get_the_area(self):
        return 3.14 * self.radius**2

class triangle(shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def get_the_area(self):
        return (self.base * self.height)/2
    
# Code to read the text file "shape.txt" that we will use to return the areas from
file = open("C:\\TexasA&M_Masters\\GitHub\\Lamson_online_GEOG676_spring2025\\Labs\\Lab3\\shape.txt", 'r')
lines = file.readlines()
file.close()

# Code to run when the file is read in order to return the area given the new information
for line in lines:
    components = line.split(',')  # This code is allowing us to split the string at the comma for how the text file is written
    shape = components[0]  # This is grabbing the sting name at the first point in the list and defining it as shape for later use for the loops

    if shape == 'rectangle':
        rec = rectangle(int(components[1]), int(components[2])) # Have to change them to int as it will read as a string
        print('The area of the rectangle is: ', rec.get_the_area())

    elif shape == 'circle':
        cir = circle(int(components[1])) # Have to change them to int as it will read as a string
        print('The area of the circle is: ', cir.get_the_area())

    elif shape == 'triangle':
        tri = triangle(int(components[1]), int(components[2])) # Have to change them to int as it will read as a string
        print('The area of the triangle is: ', tri.get_the_area())
    
    else:
        pass