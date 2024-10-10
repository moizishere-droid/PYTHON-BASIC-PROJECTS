# AREA AND PERIMENT  OF SHAPES

def Rectangle(length,width):
    area = int(length*width)
    perimeter = int(2*(area))
    print(area)
    print(perimeter)

def Square(side):
    area = int(side**2)
    perimeter = int(4*(side))
    print(area)
    print(perimeter)

def Triangle(base , side2, side3 ,heigth):
    area = int((0.5) *base * heigth)
    perimeter = int(base + side2 + side3)
    print(area)
    print(perimeter)

def Circle(radius):
    area = int(3.142*(radius**2))
    perimeter = int(2*((3.142)*radius))
    print(area)
    print(perimeter)


user_input = input("ENTER THE SHAPE NAME: ")
while(user_input!=""):
    if(user_input=="rectangle"):
        length = int(input("enter the length of the rectangle: "))
        width = int(input("enter the width of the rectangle: "))
        Rectangle(length,width)
    elif(user_input=="square"):
        side = int(input("enter the side length of the square: "))
        Rectangle(side)
    elif(user_input=="triangle"):
        base = int(input("enter the base of the triangle: "))
        side2 = int(input("enter the side1 of the triangle: "))
        side3 = int(input("enter the side2 of the triangle: "))
        heigth = int(input("enter the heigth of the triangle: "))
        Triangle(base,side2,side3,heigth)    
    elif(user_input=="circle"):
        radius = int(input("enter the radius of the circle: "))
        Circle(radius)
    else:
        print("INvalid")    
    user_input = input("ENTER THE SHAPE NAME:  ")