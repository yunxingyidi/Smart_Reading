import fingercounter as fi
import sound as so
import cv2
import threading
import globalvar as gl

gl._init()
gl.set_value("text", "")
cap = cv2.VideoCapture(0)

fingercounter = fi.Fingercounter(cap)
fingercounter.start()

