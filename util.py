import numpy as np    #numpy library is used to get the angle,calculating the distance b/w landmark

def get_angle(a, b, c):   #we are getting the angle of the fingers when we perfom any finger action
                          #we are using  a,b,c to calculate the angle between the points of the finger
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0]) #np.arctan2 a function in NumPy that computes the angle 𝜃 (in radians)
    '''we are calculationg the angle (c[1] - b[1], c[0] - b[0]) the angle b/w a,b and  np.arctan2(a[1] - b[1], a[0] - b[0])
    the angle between b,c'''
    angle = np.abs(np.degrees(radians)) #converting radian value to degree
    return angle

'''
#np.abs(...):

Takes the absolute value of the resulting degree measure.
This ensures the angle is non-negative, as angles can be negative depending on the direction of the vectors.


#np.degrees(radians):

Converts the angle from radians to degrees.
Since angles in trigonometric functions like arctan2 are calculated in radians by default, 
this step converts it into a more human-readable format.

'''


def get_distance(landmark_ist): #function to get the distance betwwn thw landmark
    if len(landmark_ist) < 2: #landmark_ist: A list of at least two tuples, where each tuple represents the (x, y) coordinates of a landmark.
        return
    (x1, y1), (x2, y2) = landmark_ist[0], landmark_ist[1]  #Unpacks the coordinates of the first two landmarks in the list.
    L = np.hypot(x2 - x1, y2 - y1) #Computes the Euclidean distance between the two landmarks using numpy's hypot function
    return np.interp(L, [0, 1], [0, 1000]) #Uses numpy's interp function to map the distance L from its original range [0, 1] to a new range [0, 1000].