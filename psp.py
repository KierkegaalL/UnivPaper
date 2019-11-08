# coding:utf-8
import cv2
import numpy as np
import sys
import os
#import findcolor


# 画像の読み込み
imgName = sys.argv

if len(imgName)<=1:
   print "[Error] ファイルを指定してください.\n使用方法: 'python test.py <FilePath>'"
   exit()

path = imgName[1]

if not os.path.isfile(path):
   print "[Error] ファイル '"+imgName[1]+"' は存在しません."
   exit()

imgO = cv2.imread(path)
   
#imgO = cv2.imread('/Users/OkuRyuji/sendforapp/reserch/img/IMG_3540.jpg')


# 読み込んだ画像のリサイズ
img = cv2.resize(imgO, (2000, 3000))
imgO  = img


# BGR空間からHSV空間に変換
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# 画像内の白色部分を抽出
lower_w = np.array([0,0,170], np.uint8)
upper_w = np.array([255,255,255], np.uint8)
img_w = cv2.inRange(img_hsv, lower_w, upper_w)


#cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/white.png', img_w)

# グレースケール画像からRGB画像に変換
img_rgb = cv2.cvtColor(img_w, cv2.COLOR_GRAY2RGB)


# ノイズを除去
kernel = np.ones((9,9), np.uint8)
img_rem = cv2.morphologyEx(img_rgb, cv2.MORPH_OPEN, kernel)
img_rem = cv2.morphologyEx(img_rgb, cv2.MORPH_CLOSE, kernel)


# 白黒を反転
img_rev = 255 - img_rem

#cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/rev.png', img_rem)


# 輪郭を検出
lower_gray = np.array([0],np.uint8)
upper_gray = np.array([128], np.uint8)
img_gray = cv2.inRange(img_rev, lower_gray, upper_gray)
contours, _ = cv2.findContours(img_gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    
# 検出された輪郭の最大面積を検出する
max_area_contour = -1
max_area = 0
    
for contour in contours:
    area=cv2.contourArea(contour)
    if(max_area < area):
        max_area = area
        max_area_contour = contour
            
cont = [max_area_contour]

# 近似した画像を出力したいときは以下をコメントアウト
cv2.drawContours(imgO, max_area_contour, -1, (255, 128, 0), 36)
    
    
# 輪郭を近似する
epsln = 0.01 * cv2.arcLength(max_area_contour,True)
approx = cv2.approxPolyDP(max_area_contour,epsln,True)
#print(approx)

# 近似した画像を出力したいときは以下の３行をコメントアウト
if len(approx) ==4:
   cv2.drawContours(img, [approx], -1, (0, 0, 255), 36)
   cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/grid/failed1.png',img)
   #cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/grid/failed2.png',img)
   #cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/grid/suc1.png',img)
   #cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/grid/suc2.png',img)
   #cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/grid/failed3.png',img)
   #cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/grid/suc3.png',img)
   
# 射影変換（透視変換，ホモグラフィー変換）
#row,col,ch = img.shape

#psp_pts1 = np.array(approx,np.float32).reshape(4,2)

#if (psp_pts1[[0,0]] > psp_pts1[[2,0]]).any() and (psp_pts1[[1,1]] < psp_pts1[[3,1]]).any():
#    psp_pts2 = np.array([[2000,0],[0,0],[0,3000],[2000,3000]],np.float32)
#elif (psp_pts1[[0,0]] < psp_pts1[[2,0]]).any() and (psp_pts1[[1,1]] > psp_pts1[[3,1]]).any():
#    psp_pts2 = np.array([[0,0],[0,3000],[2000,3000],[2000,0]],np.float32)
#print(psp_pts2)

#psp = cv2.getPerspectiveTransform(psp_pts1,psp_pts2)
#img_psp = cv2.warpPerspective(img,psp,(col,row))

# 画像の書き出し
#cv2.imwrite('/Users/OkuRyuji/sendforapp/reserch/Persp/pspexp.png',img_psp)
#findcolor.rw('/Users/OkuRyuji/sendforapp/reserch/Persp/pspexp.png')
