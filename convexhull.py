import numpy as np

def myConvexHull(list):
    list = np.array(sort(list)) # save bucket as a numpy array
    # take the farmost left and right point from the data set
    extremeLeft = list[0]
    extremeRight = list[-1]
    # empty list to store point from the above and below of the line made by the 2 point of extreme left and right
    labove =[]
    lbelow =[]

    # empty list to store convex hull point from above and below of the line made by the 2 point of extreme left and right
    global final_up, final_down 
    final_up= []
    final_down = []

    # check each point and assign it to labove / lbelow based on its position
    for point in list:
        if(position(point,extremeLeft,extremeRight) == "above"):
            labove.append(point)
        elif(position(point,extremeLeft,extremeRight) =="below"):
            lbelow.append(point)
    
    #find the convexhullpoint on labove and lbelow
    convexhullPoint(labove,extremeLeft,extremeRight,"up")
    convexhullPoint(lbelow,extremeRight,extremeLeft,"down") # the positon of extremeRight and left is switch because its position in below
    sort(final_up) #sort the point based on the axis first then the ordinate in ascending order
    sort_down(final_down) #sort but in descending order
    final = np.concatenate((final_up, final_down), axis=0) #merge the two list as the final convexhull point
    return(final)

def convexhullPoint(list, min, max,pos):
    #basis
    if(len(list)==0): # list here is the list of point above the line, if there is no point above the line
        # the two point that make up the line is included as convexhullpoint
        if(pos =="up"):
            final_up.extend([min])
            final_up.extend([max])
        elif(pos == "down"):
            final_down.extend([min])
            final_down.extend([max])
    else: #recursive
        furthest = furthestpoint(list,min,max) #find the furthestpoint from the line
        # empty list to store point above the line made by the previous left point and furthest & furthest and previous right point
        checkabove_left=[]
        checkabove_right=[]
        # check each point and assign based on its position
        for point in list:
            if(position(point,min,furthest) == "above"):
                checkabove_left.extend([point])
        for point in list:
            if(position(point,furthest,max) =="above"):
                checkabove_right.extend([point])
        convexhullPoint(checkabove_left,min,furthest,pos) #recursive
        convexhullPoint(checkabove_right,furthest,max,pos) #recursive

"""
To find whether point(xp,yp) is above the line from (x1,y1) to (x2,y2) or not, use the determinant concept
If its positive its above, if its negative its below

x1y2 + xpy1 + x2yp - xpy2 -x2y1 -x1yp
(x1,y1) = min[0][1]
(x2,y2) = max[0][1]
(xp,yp) = point[0][1]

"""
def position(point, min,max):
    xmin, ymin = min
    xmax, ymax = max
    xp,yp = point
    determinant = (xmin*ymax + xp*ymin + xmax*yp - xp*ymax - xmax*ymin - xmin*yp)
    if(determinant > pow(10,-10)):
        return "above"
    elif(determinant < 0):
        return "below"
    
def furthestpoint(list,p1,p2):
    furthest = []
    far = 0
    for point in list:
        if(distance(point,p1,p2) >= far):
            far = distance(point,p1,p2)
            furthest = point
    return furthest

def distance(point,p1,p2): # find the distance of point to line make up by p1 and p2
    p1 = np.asfarray(p1) #convert type to float type
    p2 = np.asfarray(p2)
    point = np.asfarray(point)
    return(np.linalg.norm(np.cross(p2-p1, p1-point))/np.linalg.norm(p2-p1)) # distance equation


def sort(list): #method to sort the original data set and final_up
    return sorted(list , key=lambda x:[x[0], x[1]])

def sort_down(list): #method to sort final_down, using reverse because the position of all the point is below
    return sorted(list , key=lambda x:[x[0], x[1]], reverse=True)