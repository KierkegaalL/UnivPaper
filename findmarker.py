# coding:utf-8
import cv2
import numpy as np
import sys
import poro



def find_marker(src, name):

   
    
    # 平滑化
    blur_src = cv2.GaussianBlur(src, (15, 15), 20)

    # 二値化
    ret, binary_src = cv2.threshold(blur_src, 127, 255, cv2.THRESH_BINARY)
    
    
    # ラベリング処理
    label = cv2.connectedComponentsWithStats(binary_src)
    #print(label)

    # オブジェクト情報を抽出
    n = label[0] - 1
    
    # print(n)
    

    centers = []
    for i in range(1,n+1):
        centers.append(label[3][i])
       # print(center)
    #f.close()


    return centers

    
        

def rw(prefix):
    red = cv2.imread(prefix+'red.png',0)
    orange = cv2.imread(prefix+'orange.png',0)
    yellow =  cv2.imread(prefix+'yellow.png',0)
    green = cv2.imread(prefix+'green.png',0)
    blue =  cv2.imread(prefix+'blue.png',0)
    purple = cv2.imread(prefix+'purple.png',0)
    rp = cv2.imread(prefix+'rp.png',0)
    violet = cv2.imread(prefix+'violet.png',0)
    yg = cv2.imread(prefix+'yg.png',0)
    bg = cv2.imread(prefix+'bg.png',0)
    
    
    red_center = find_marker(red, "red")
    orange_center = find_marker(orange, "orange")
    yellow_center = find_marker(yellow, "yellow")
    green_center = find_marker(green, "green")
    blue_center = find_marker(blue, "blue")
    purple_center = find_marker(purple, "purple")
    rp_center = find_marker(rp, "rp")
    violet_center = find_marker(violet,"violet")
    yg_center = find_marker(yg, "yg")
    bg_center = find_marker(bg, "bg")

    centers = [red_center, orange_center, yellow_center, green_center, blue_center, purple_center, rp_center, violet_center, yg_center, bg_center]
    poro.main(centers)
    
if __name__=="__main__":
    rw()
