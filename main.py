#!/usr/bin/env python3

import sys
import numpy as np
import cv2
from pyfakewebcam import FakeWebcam

y = 100
x = 70
scale = 3 / 4

# real webcam
cap = cv2.VideoCapture("/dev/video0")

original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fakewebcam = FakeWebcam("/dev/video2", original_width, original_height)


def loop():

    success, frame = cap.read()
    if not success:
        print("Error getting a webcam image!")
        sys.exit(1)

    # BGR to RGB
    frame = frame[...,::-1]
    frame = frame.astype(float)

    height = int(original_height*scale)
    width = int(original_width*scale)

    frame = frame[y:y + height, x:x + width]

    frame=cv2.resize(frame, None, fx=1/scale, fy=1/scale)

    frame = frame.astype(np.uint8)
    fakewebcam.schedule_frame(frame)


if __name__ == "__main__":
    while True:
        try:
            loop()
        except KeyboardInterrupt:
            print("stopping.")
            break
