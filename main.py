import time
import cv2
from wheelchair import Wheelchair
import numpy as np
from pupil_apriltags import Detector

chair = Wheelchair()
cap = cv2.VideoCapture(0)

april_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)

try:
    while True:
        ok, frame = cap.read()
        mono = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        apriltags = april_detector.detect(mono) 

        if len(apriltags) > 0:
            tag = apriltags[0]
            c = tag.center
            print(c)
            chair.forward(0.5)
        else:
            chair.stop()

except KeyboardInterrupt:
    chair.stop()
    cap.release()