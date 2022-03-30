choice = input("Choose Shape \n")
if (choice== "circle"):
    radius= float(input("enter radius\n"))
    area= 3.14*radius*radius
    perimeter= 2*3.14*radius
    print("Area is {} Perimeter is {} ".format(area,perimeter))
elif (choice== "square"):
    side= float(input("enter side\n"))
    area= side*side
    perimeter= 4*side
    print("Area is {} Perimeter is {} ".format(area,perimeter))
elif (choice== "triangle"):
    base= float(input("enter base\n"))
    height= float(input("enter height \n"))
    area= 0.5*base*height
    
    print("Area is: ",area )
else:
    print("invalid argument")
    
    
