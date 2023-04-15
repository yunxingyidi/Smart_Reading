import cv2
import HandTrackingModule1 as htm
import scan as sc
import volume as vo
import sound as so
import strBuffer
import threading
import time
import compile_part.numChange as num
import serial as se

class Fingercounter(threading.Thread):
    def __init__(self, cap):
        threading.Thread.__init__(self)
        self.wCam = 640
        self.hCam = 480
        self.cap = cap
        self.detector = htm.handDetector(detectionCon=0.75)

        self.tipIds = [4, 8, 12, 16, 20]
        self.last_Finger = 0
        self.count = 0


    def run(self):
        scan = sc.Scan(self.cap)
        volume = vo.Volume(self.cap)
        buffer = strBuffer.strBuffer()
        numchange = num.numChange()
        sound = so.Sound()
        data = se.Data()
        pTime = 0
        delay = 0
        scan_flag = False
        sign = False
        bbox = []
        while True:
            success, img = self.cap.read()
            img = cv2.resize(img, (640, 480))
            img = self.detector.findHands(img)
            lmList = self.detector.findPosition(img, draw=False)

            if scan_flag:
                delay += 1
                if delay <= 50:
                    continue
                else:
                    read_text, sign = scan.handle()
                    if sign:
                        buffer.add_string(read_text)
                        print(read_text)
                    else:
                        print("Can't find book!!!!!")
                        # sound.read(read_text)
                        # sound.change_state(True)
                        # sound.start()
                    self.count = 0
                    delay = 0
                    scan_flag = False
            if len(lmList) != 0:
                fingers = []
                # Thumb
                if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # 4 Fingers
                for id in range(1, 5):
                    if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # print(fingers)
                totalFingers = fingers.count(1)
                if totalFingers == self.last_Finger:
                    self.count += 1
                else:
                    self.count = 0
                if self.count == 10:
                    if totalFingers == 1:
                        sign = sound.change_state(sign)
                        self.count = 0
                    elif totalFingers == 2:
                        scan_flag = True
                        # read_text, sign = scan.handle()
                        # if sign:
                        #     print(read_text)
                        # else:
                        #     sound.read(read_text)
                        #     sound.change_state(True)
                        #     sound.start()
                        # self.count = 0
                    elif totalFingers == 3:
                        volume.handle()
                        self.count = 0
                    elif totalFingers == 4:
                        numchange.add(buffer)
                        numlist = numchange.a2num()
                        data.choose(numlist)
                        self.count = 0
                    else:
                        self.count = 0
                self.last_Finger = totalFingers
                print(totalFingers)
                cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(totalFingers - 1), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                            10, (255, 0, 0), 25)
                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime
                cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                            1, (255, 0, 0), 3)

            cv2.imshow("Image", img)
            cv2.waitKey(1)