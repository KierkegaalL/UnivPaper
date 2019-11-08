import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


f = open('/Users/OkuRyuji/sendforapp/reserch/csv/markers.csv','w')
f.write('color,ID,x,y\n')

#read mask image
red = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/red.png',0)
orange = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/orange.png',0)
yellow = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/red.png',0)
green = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/green.png',0)
blue = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/blue.png',0)
purple = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/purple.png',0)
pink = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/rp.png',0)
violet = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/violet.png',0)
chart = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/yg.png',0)
cyan = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/pointmask/bg.png',0)

#labeling
red_label = cv2.connectedComponentsWithStats(red)
orange_label = cv2.connectedComponentsWithStats(orange)
yellow_label = cv2.connectedComponentsWithStats(yellow)
green_label = cv2.connectedComponentsWithStats(green)
blue_label = cv2.connectedComponentsWithStats(blue)
purple_label = cv2.connectedComponentsWithStats(purple)
pink_label = cv2.connectedComponentsWithStats(pink)
violet_label = cv2.connectedComponentsWithStats(violet)
chart_label = cv2.connectedComponentsWithStats(chart)
cyan_label = cv2.connectedComponentsWithStats(cyan)

#plt.imshow(red_label)
#plt.show()

#insert object information
nred = red_label[0] - 1
norange = orange_label[0] - 1
nyellow = yellow_label[0] - 1
ngreen = green_label[0] - 1
nblue = blue_label[0] - 1
npurple = purple_label[0] - 1
npink = pink_label[0] - 1
nviolet = violet_label[0] - 1
nchart = chart_label[0] - 1
ncyan = cyan_label[0] - 1

#print(norange)

data = np.delete(violet_label[2], 0, 0)

red_center = np.delete(red_label[3], 0, 0)
orange_center = np.delete(orange_label[3], 0, 0)
yellow_center = np.delete(yellow_label[3], 0, 0)
green_center = np.delete(green_label[3], 0, 0)
blue_center = np.delete(blue_label[3], 0, 0)
purple_center = np.delete(purple_label[3], 0, 0)
pink_center = np.delete(pink_label[3], 0, 0)
violet_center = np.delete(violet_label[3], 0, 0)
chart_center = np.delete(chart_label[3], 0, 0)
cyan_center = np.delete(cyan_label[3], 0, 0)



#save axis data
for i in range(nred):
    f.write('red,'+ str(i + 1) +','+str(red_center[i][0])+','+str(red_center[i][1])+'\n')
for i in range(norange):
    f.write('orange,'+ str(i + 1) +','+str(orange_center[i][0])+','+str(orange_center[i][1])+'\n')
for i in range(nyellow):
    f.write('yellow,'+ str(i + 1) +','+str(yellow_center[i][0])+','+str(yellow_center[i][1])+'\n')
for i in range(ngreen):
    f.write('green,'+ str(i + 1) +','+str(green_center[i][0])+','+str(green_center[i][1])+'\n')
for i in range(nblue):
    f.write('blue,'+ str(i + 1) +','+str(blue_center[i][0])+','+str(blue_center[i][1])+'\n')
for i in range(npurple):
    f.write('purple,'+ str(i + 1) +','+str(purple_center[i][0])+','+str(purple_center[i][1])+'\n')
for i in range(npink):
    f.write('pink,'+ str(i + 1) +','+str(pink_center[i][0])+','+str(pink_center[i][1])+'\n')
for i in range(nviolet):
    f.write('violet,'+ str(i + 1) +','+str(violet_center[i][0])+','+str(violet_center[i][1])+'\n')
for i in range(nchart):
    f.write('chart,'+ str(i + 1) +','+str(chart_center[i][0])+','+str(chart_center[i][1])+'\n')
for i in range(ncyan):
    f.write('cyan,'+ str(i + 1) +','+str(cyan_center[i][0])+','+str(cyan_center[i][1])+'\n')



    #output color
    src = cv2.cvtColor(orange, cv2.COLOR_GRAY2BGR)
    x = data[i][0] + data[i][2]
    y = data[i][1] + data[i][3]
    cv2.putText(src, "ID: " +str(i + 1), (x - 20, y - 30), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255))
    cv2.putText(src, "x: " + str(int(violet_center[i][0])), (x - 20, y + 25), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255))
    cv2.putText(src, "y: " + str(int(violet_center[i][1])), (x - 20, y + 100), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255))

    #print('chart,'+ str(i +1) +','+str(chart_center[i][0])+','+str(chart_center[i][1]))
    
    #save axis data
    
    
   
    

cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/pointmask/pointaxis/redaxis.png',src)

