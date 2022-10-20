import cv2 as cv
from time import sleep


def main():

    cap = cv.VideoCapture()
    
    cap.open(0)
    
    for _ in range(10):
        t,o = cap.read()
        
        cv.imshow("window:",o)
        
        sleep(1)
        
    
   
    
main()
