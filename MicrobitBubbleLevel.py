#Name: Zosia Stafford
#Partners: Hector and Gillian (We each have different codes but worked together on the basics)
#When running, an arrow points in the direction the microbit needs to move to be flat
#The brighter the arrow, the more it must move

#Imports
from microbit import *
import math

#Functions - finding the angles
def anglex_radian(x, y, z):
    xrad = math.atan2(x,(math.sqrt(y**2+z**2)))      #x in radians
    return xrad
def angley_radian(x, y, z):
    yrad = math.atan2(y,(math.sqrt(x**2+z**2)))      #y in radians
    return yrad
def anglex_degree(xrad):
    xdeg = (xrad/math.pi)*180                        #x in degrees
    return xdeg
def angley_degree(yrad):
    ydeg = (yrad/math.pi)*180                        #y in degrees
    return ydeg

#Variables - the images
circle = Image("00000:09990:09390:09990:00000")
arrow_E1 = Image("00400:00040:44444:00040:00400")
arrow_E2 = Image("00600:00060:66666:00060:00600")
arrow_E3 = Image("00900:00090:99999:00090:00900")
arrow_W1 = Image("00400:04000:44444:04000:00400")
arrow_W2 = Image("00600:06000:66666:06000:00600")
arrow_W3 = Image("00900:09000:99999:09000:00900")
arrow_S1 = Image("00400:00400:40404:04440:00400")
arrow_S2 = Image("00600:00600:60606:06660:00600")
arrow_S3 = Image("00900:00900:90909:09990:00900")
arrow_N1 = Image("00400:04440:40404:00400:00400")
arrow_N2 = Image("00600:06660:60606:00600:00600")
arrow_N3 = Image("00900:09990:90909:00900:00900")
arrow_SW1 = Image("00004:40040:40400:44000:44440")
arrow_SW2 = Image("00006:60060:60600:66000:66660")
arrow_SW3 = Image("00009:90090:90900:99000:99990")
arrow_NE1 = Image("04444:00044:00404:04004:40000")
arrow_NE2 = Image("06666:00066:00606:06006:60000")
arrow_NE3 = Image("09999:00066:00909:09009:60000")
arrow_NW1 = Image("44440:44000:40400:40040:00004")
arrow_NW2 = Image("66660:66000:60600:60060:00006")
arrow_NW3 = Image("99990:99000:90900:90090:00009")
arrow_SE1 = Image("40000:04004:00404:00044:04444")
arrow_SE2 = Image("60000:06006:00606:00066:06666")
arrow_SE3 = Image("90000:09009:00909:00099:09999")


#Main code
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    ax= anglex_degree(anglex_radian(x,y,z))
    ay= angley_degree(angley_radian(x,y,z))

    print((ax, ay))      #prints degree values

    sleep(200)

#All of the values:

#on center
    if((-10<=ax<=10) and (-10<=ay<=10)):
        display.show(circle)
#tilted to the left, arrow points east (right)
    elif((-30<=ax<10) and (0<=ay<10)):
    #low
        display.show(arrow_E1)
    elif((-60<=ax<-30) and (0<=ay<10)):
    #medium
        display.show(arrow_E2)
    elif((-90<=ax<-60) and (0<=ay<10)):
    #high
        display.show(arrow_E3)
#tilted to the right, arrow points west (left)
    elif((10<=ax<30) and (0<=ay<10)):
    #low
        display.show(arrow_W1)
    elif((30<=ax<60) and (0<=ay<10)):
    #medium
        display.show(arrow_W2)
    elif((60<=ax<90) and (0<=ay<10)):
    #high
        display.show(arrow_W3)
#tilted up, arrow points south (down)
    elif((-10<ax<=0) and (-30<=ay<-10)):
    #low
        display.show(arrow_S1)
    elif((-10<ax<=0) and (-60<=ay<-30)):
    #medium
        display.show(arrow_S2)
    elif((-10<ax<=0) and (-90<=ay<-60)):
    #high
        display.show(arrow_S3)
#tilted down, arrow points north (up)
    elif((-10<ax<=0) and (10<ay<=30)):
    #low
        display.show(arrow_N1)
    elif((-10<ax<=0) and (30<ay<=60)):
    #medium
        display.show(arrow_N2)
    elif((-10<ax<=0) and (60<ay<=90)):
    #high
        display.show(arrow_N3)
#tilted north east, arrow points south west
    elif((10<=ax<30) and (-50<ay<=0)):
    #low
        display.show(arrow_SW1)
    elif((30<=ax<50) and (-50<ay<=0)):
    #medium
        display.show(arrow_SW2)
    elif((50<=ax<=90) and (-50<=ay<=0)):
    #high
        display.show(arrow_SW3)
#tilted south west, arrow points north east
    elif((-30<=ax<-10) and (0<=ay<50)):
    #low
        display.show(arrow_NE1)
    elif((-50<=ax<-30) and (0<=ay<50)):
    #medium
        display.show(arrow_NE2)
    elif((-90<=ax<-50) and (0<=ay<50)):
    #high
        display.show(arrow_NE3)
#tilted south east, arrow points north west
    elif((10<ax<=20) and (10<ay<=25)):
    #low
        display.show(arrow_NW1)
    elif((20<ax<=30) and (25<ay<=40)):
    #medium
        display.show(arrow_NW2)
    elif((30<ax<=60) and (40<ay<=60)):
    #high
        display.show(arrow_NW3)
#tilted north west, arrow points south east
    elif((-25<=ax<-10) and (-20<=ay<-10)):
    #low
        display.show(arrow_SE1)
    elif((-40<=ax<-25) and (-30<=ay<-20)):
    #medium
        display.show(arrow_SE2)
    elif((-60<=ax<-40) and (-60<=ay<-30)):
    #high
        display.show(arrow_SE3)




