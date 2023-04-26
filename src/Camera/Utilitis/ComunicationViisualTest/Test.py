import cv2

from tests import Camera

# test use deprecated metod no longer works

if __name__ == '__main__':

    kam = Camera()

    while True:
        frame = kam.getFrame()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    kam.device.release()
    # Destroy all the windows
    cv2.destroyAllWindows()