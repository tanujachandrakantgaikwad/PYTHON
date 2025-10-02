#Write a function named pt_in_circle that takes a circle and a point and returns 
#true if point lies on the boundry of circle.
def pt_in_circle(center, radius, point):
    x, y = point
    h, k = center
    
    if (x - h)**2 + (y - k)**2 == radius**2:
        return True
    else:
        return False

center = (0, 0)
radius = 5
point1 = (3, 4)
point2 = (1, 1)

print(pt_in_circle(center, radius, point1)) 
print(pt_in_circle(center, radius, point2))  
