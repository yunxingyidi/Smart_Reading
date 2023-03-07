import cv2
import numpy as np
import HandTrackingModule2 as htm
import globalvar as gl


class Volume:
    def __init__(self, cap):
        self.cap = cap

    def handle(self):
        detector = htm.handDetector(detectionCon=0.8, maxHands=1)
        # devices = AudioUtilities.GetSpeakers()
        # interface = devices.Activate(IAudioEndpointVolume._iid_, 7, None)
        #volume = cast(interface, POINTER(IAudioEndpointVolume))
        area = 0
        i = 0
        print("In the volume")
        while i < 100:
            success, img = self.cap.read()
            # Find Hand
            img = detector.findHands(img)
            lmList, bbox, flag = detector.findPosition(img, draw=False)
            if flag == False:
                continue
            if len(lmList) != 0:
                # Filter based on size
                area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
                # print(area)
                if 250 < area < 1000:
                    # Find Distance between index and Thumb
                    length, img, lineInfo = detector.findDistance(4, 8, img)
                    # Convert Volume
                    volPer = np.interp(length, [100, 400], [0, 100])
                    # Reduce Resolution to make it smoother
                    smoothness = 10
                    volPer = smoothness * round(volPer / smoothness)
                    # Check fingers up
                    fingers = detector.fingersUp()
                    # If pinky is down set volume
                    # if not fingers[4]:
                    #     volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                    #     cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)

            # cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
            ###############
            #使用更改音量函数#
            ###############
            print(volPer)
            i += 1