from wheelchair import Wheelchair
from pupil_apriltags import Detector
import cv2, time

chair = Wheelchair()

cf = cv2.VideoCapture(0)
cv2.namedWindow("Camera Feed")

april_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)

while True:
    ret, frame = cf.read()
    cv2.imshow("Camera Feed", frame)
    
    mono = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    apriltags = april_detector.detect(mono) 

    if len(apriltags) > 0:
        print("a")
    else:
        print("b")
    
    keypressed = cv2.waitKey(1)
    if keypressed == 27:
        break

cf.release()
cv2.destroyAllWindows()