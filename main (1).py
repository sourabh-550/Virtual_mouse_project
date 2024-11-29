import cv2                #OpenCV(For video capturing)
import mediapipe as mp    #For hand points and coordinate
import pyautogui          #For double click
import random             
import util              #importing util file here
from pynput.mouse import Button, Controller# for left click right click 
mouse = Controller()


screen_width, screen_height = pyautogui.size()

mpHands = mp.solutions.hands      #mp.solutions.hands is a part of Mediapipe designed for detecting and tracking hands.
                                  #We assign it to the variable mpHands to make it easier to use later in the code.
hands = mpHands.Hands(            
    static_image_mode=False,      #As we are working on video not image.
    model_complexity=1,            
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7,  #0.7 means the model must be at least 70% confident that it's still tracking the same hand.
                                  #If the confidence drops below this level, the model might stop tracking or re-detect the hand.
    max_num_hands=1               #The maximum number of hands the model will detect and track.1 means it will detect only one hand.         
)

def find_finger_tip(processed): #used to find the fingertip of index finger to move the mouse
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]  # Assuming only one hand is detected
        index_finger_tip = hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP] 
        return index_finger_tip 
    return None, None


def move_mouse(index_finger_tip):#function for moving the mouse
    if index_finger_tip is not None:
        x = int(index_finger_tip.x * screen_width) 
        y = int(index_finger_tip.y / 2 * screen_height)
        pyautogui.moveTo(x, y,duration=0.001) #using pyautogui to move the mouse cursor



def is_left_click(landmark_list, thumb_index_dist): #function for left click
    return (
            util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
            util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) > 90 and
            thumb_index_dist > 50
    )


def is_right_click(landmark_list, thumb_index_dist):#function for right click
    return (
            util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
            util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90  and
            thumb_index_dist > 50
    )


def is_double_click(landmark_list, thumb_index_dist):#function for double click
    pass


def is_screenshot(landmark_list, thumb_index_dist):#function for screenshot
   pass

def detect_gesture(frame, landmark_list, processed):# this function is used to detect the gestures
    if len(landmark_list) >= 21: #it'll work only when all 21 points are detected

        index_finger_tip = find_finger_tip(processed) #find the finger tip to move the mouse
        thumb_index_dist = util.get_distance([landmark_list[4], landmark_list[5]]) #
#Movement
        if util.get_distance([landmark_list[4], landmark_list[5]]) < 50  and util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90: 
            #using util file to calculate the distance b/w index finger,thumb(point 4,5) to move the mouse
            move_mouse(index_finger_tip) 
#Left Click
        elif is_left_click(landmark_list,  thumb_index_dist):
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#Right Click        
        elif is_right_click(landmark_list, thumb_index_dist):
            mouse.press(Button.right)
            mouse.release(Button.right)
            cv2.putText(frame, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#Double Click        
        elif is_double_click(landmark_list, thumb_index_dist):
            pass
#Screenshot       
        elif is_screenshot(landmark_list,thumb_index_dist ):
            pass
1

def main():   
    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0) 

    try:   #handle the error if any
        while cap.isOpened():                      #check if the capture running successfully
            ret, frame = cap.read()                #ret(return) is a bool value and we are reading video frame by frame
            if not ret:                            
                break
            frame = cv2.flip(frame, 1)             #this will flip the frame just like we are looking into the mirror.
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            processed = hands.process(frameRGB)             #This variable stores the results after the image has been analyzed using frameRGB

            landmark_list = []      #contains all the landmarks of the hand
            if processed.multi_hand_landmarks: 
                hand_landmarks = processed.multi_hand_landmarks[0]  # Assuming only one hand is detected
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)  #we are using it for own convience.we can see the landmark on the screen
                                                          
                for lm in hand_landmarks.landmark:   #we will loop through the landmark and get the list of all the landmarks

                    landmark_list.append((lm.x, lm.y)) #we are sending all the (x,y) coordinates of landmark


            detect_gesture(frame, landmark_list, processed)

            cv2.imshow('Frame', frame)            #using opencv function 'imshow' to show the captured frame 'frame' is passed to function
            if cv2.waitKey(1) & 0xFF == ord('q'): #'waitkey' is opencv function here after each milisecond if we press q on my keyboard the window will close
                break
    finally:
        cap.release()           #we will release all the captures frame
        cv2.destroyAllWindows() #it will destroy all the opened window


if __name__ == '__main__':
    main()

