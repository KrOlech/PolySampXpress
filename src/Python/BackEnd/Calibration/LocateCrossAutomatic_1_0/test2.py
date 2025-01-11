import cv2
import cv2.aruco as aruco
if __name__ == '__main__':
    # Load the image
    #image = cv2.imread('full2.png')
    image = cv2.imread('tst-1.png')


    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the ArUco dictionary
    aruco_dict = aruco.Dictionary(aruco.DICT_4X4_100, 10)

    # Define the parameters for marker detection
    parameters = aruco.DetectorParameters()

    # Detect ArUco markers in the image
    corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # Draw the detected markers on the image
    if ids is not None:
        aruco.drawDetectedMarkers(image, corners, ids)

    # Display the image
    cv2.imshow('ArUco Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
