import cv2
import numpy as np
from cv2 import aruco
import time

dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_1000)

parameters = aruco.DetectorParameters()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2048)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3072)

try:
    while True:
        ret, frame = cap.read()
        #frame = cv2.imread('test.png')
        #frame = np.zeros((300, 300, 3), dtype="uint8")
        #aruco.generateImageMarker(dict_aruco, 1,310, frame,1)
        frame = cv2.resize(frame, (960, 540), interpolation=cv2.INTER_CUBIC)

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)

        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

        print(ids)

        cv2.imshow('frame', frame_markers)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyWindow('frame')
    cap.release()
except KeyboardInterrupt:
    cv2.destroyWindow('frame')
    cap.release()