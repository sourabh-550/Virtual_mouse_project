import numpy as np    #numpy library is used to get the angle,calculating the distance b/w landmark

def get_angle(a, b, c):   
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0]) #np.arctan2 a function that computes the angle (in radians)
    angle = np.abs(np.degrees(radians)) #converting radian value to degree
    return angle

def get_distance(landmark_ist): #function to get the distance betwwn the landmark
    if len(landmark_ist) < 2: 
        return
    (x1, y1), (x2, y2) = landmark_ist[0], landmark_ist[1]  
    L = np.hypot(x2 - x1, y2 - y1) 
    return np.interp(L, [0, 1], [0, 1000]) #Uses numpy's interp function to map the distance L from its original range [0, 1] to a new range [0, 1000].
