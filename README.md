# Smart_Reading 
## Project Introduction
***Project Participants:  
tairan zhang, yifei li, yongchen qu, zhihao luo from hfut start at 2022.5.23***  

For this project, we designed it to solve the reading problem of blind people. Due to the advancement of AI text recognition and speech conversion technology, there are currently many devices on the market to convert e-books into speech for blind people to read, but due to the copyright of e-books, most of the books on the market have not been completed electronically, so the problem of how to use paper books for blind people to read still exists. And we use the gesture module, hope to offer a smooth user experience for them.

We have also designed a device for text output of tactile information for blind people, relying on a perfect Braille compilation system to complete the dynamic display of Braille.

Our system can be divided into image module, audio module, gesture recognition module and hardware module .

![](D:\college\大创\图片1.png)

## Image module:

The design of the image module is based on OpenCV to correct images and extract documents, and then improve the clarity processing, and use tessactocr for text recognition.image

![image](D:\college\大创\图片2.png)

## Gesture module:

The gesture recognition module uses the mediapipe framework provided by Google to determine the different positions of the key points of the hand supplement 21, realize the recognition of hand numbers, and realize the volume adjustment by judging the distance between two fingers.

## Hardware module:

The hardware module first designed a compilation system based on second-level Braille Braille to implement a finite automaton to convert letters or combinations of letters into corresponding Braille points.The electromagnet movement is then controlled by a binary sequence.

![](D:\college\大创\图片3.png)

![](D:\college\大创\图片4.png)

## Audio module:

The audio module plays the converted audio.
