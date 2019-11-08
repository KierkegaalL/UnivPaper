# coding:utf-8

import numpy as np
import sys
#データベースモジュールをインポート
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

pi = np.pi

# 3点のマーカーの座標を配列として出力
def load_data(data):
        #data = np.genfromtxt('/Users/OkuRyuji/sendforapp/reserch/csv/markers.csv',delimiter=',',skip_header=1, dtype='float')
        print(data)
        center_list = list()
        theta_list = list()
        for i in range(0, len(data)):
                point1 = np.array([data[i][0][0], data[i][0][1]])
                point2 = np.array([data[i][1][0], data[i][1][1]])
                point3 = np.array([data[i][2][0], data[i][2][1]])
                #print(point1)
                #print(point2)
                #print(point3)
                center, theta = calculate(point1, point2, point3)
                center_list.append(center)
                theta_list.append(theta)
        return center_list, theta_list

# 角度と中心座標を求める
def calculate(point1, point2, point3):
        
        theta = 0.0
        center = [0.0, 0.0]
        
        # データから値を引っ張る
        # dict = []
        points = [point1, point2, point3]
        # dict(data[i][0]) = points
        # print(points)
    
        
        # 2点間のユークリッド距離を求める
        d1 = point1 - point2
        d2 = point2 - point3    
        d3 = point3 - point1
        dis1 = np.linalg.norm(d1)
        dis2 = np.linalg.norm(d2)
        dis3 = np.linalg.norm(d3)
        
        ardis1 = np.array(dis1)
        # print(ardis1)
        ardis2 = np.array(dis2)
        # print(ardis2)
        ardis3 = np.array(dis3)
        # print(ardis3)
    
    
        # 3つの距離を比較して最大値を求める
        dis_max = np.amax(np.array([ardis1,ardis2,ardis3]))
        # print(dis_max)
    
    
        # 中心距離と角度を計算
    
        # マーカー1とマーカ2が最大距離のときマーカー1とマーカ2の中点が中心座標
        if dis_max == ardis1:
                # print(point1,point2)
                center = (point1 + point2) / 2
                # print('center1=',center)
                
                # マーカー3が前方を表し，マーカー3と中心座標を用いて角度を求める
                xr = point3[0] - center[0]
                # print(xr)
                yr = point3[1] - center[1]
                # print(yr)
                r1 = np.power(xr,2)
                # print(r1)
                r2 = np.power(yr,2)
                # print(r2)
                r = np.sqrt(r1+r2)
                # print(r)
                x = np.abs(yr)
                # print(x)
                val = x / r
                # print(val)
                rad = np.arccos(val)
                # print(rad)

                # マーカー3の位置によってpiを加減する場合分け
                if point3[1] > center[1]:
                        if point3[0] < center[0]:
                                rad1 = rad
                        else:
                                rad1 =(2 * pi) - rad
                # print(rad1)
                # ラジアンから度数に変換
                theta = np.rad2deg(rad1)
                print('theta1=',theta)
            

        # マーカー2とマーカ3が最大距離のときマーカー2とマーカ3の中点が中心座標
        elif dis_max == ardis2:
                # print(point2,point3)
                center = (point2 + point3)/ 2
                # print('center2=',center)
                
                # マーカー1が前方を表し，マーカー1と中心座標を用いて角度を求める
                xr = point1[0] - center[0]
                #print(xr)
                yr = point1[1] - center[1]
                #print(yr)
                r1 = np.power(xr,2)
                #print(r1)
                r2 = np.power(yr,2)
                #print(r2)
                r = np.sqrt(r1+r2)
                #print(r)
                x = np.abs(yr)
                #print(x)
                val = x / r
                #print(val)
                rad = np.arccos(val)
              #  print(rad)

                if point1[1] < center[1]:
                        if point1[0] < center[0]:
                                rad1 = pi - rad
                        else:
                                rad1 = pi + rad
                
              #  print(rad1)
                
                theta = np.rad2deg(rad1)
                print('theta2=',theta)
            

        # マーカー1とマーカ3が最大距離のときマーカー1とマーカ3の中点が中心座標
        elif dis_max == ardis3:
                # print(point3,point1)
                center = (point3 + point1) / 2
                # print('center3=',center)

                # マーカー2が前方を表し，マーカー2と中心座標を用いて角度を求める
                xr = point2[0] - center[0]
                #print(xr)
                yr = point2[1] - center[1]
                #print(yr)
                r1 = np.power(xr,2)
                # print(r1)
                r2 = np.power(yr,2)
                # print(r2)
                r = np.sqrt(r1+r2)
                #print(r)
                x = np.abs(yr)
                #print(x)
                val = x / r
                # print(val)
                rad = np.arccos(val)
                #  print(rad)
               # th = np.rad2deg(rad)
               # print('th3=', th)
                if point2[0] < center[0]:
                        if point2[1] >= center[1]:
                                rad1 = rad
                        else:
                                rad1 = pi - rad
                else:
                        if point2[1] > center[1]:
                                rad1 = (2 * pi) - rad
                        else:
                                rad1 = pi + rad
              #  print(rad1)
                
                theta = np.rad2deg(rad1)
                print('theta3=', theta)
                
        return center, theta


# firebaseに中心座標と角度のデータを送信
def main(point_centers):
       # print(point_centers)       
        centers, thetas = load_data(point_centers)
        # print(centers)
        # print(thetas)
        
        
        if (not len(firebase_admin._apps)):
                cred = credentials.Certificate('/Users/OkuRyuji/sendforapp/correlationdiagram-97e0c-firebase-adminsdk-02t0f-0fa4c792ed.json')
                
                firebase_admin.initialize_app(cred, {
                        'databaseURL': 'https://correlationdiagram-97e0c.firebaseio.com/',
                        'databaseAuthVariableOverride': {
                                'uid': 'my-service-worker'
                        }
                })


        # データベース参照を取得
        users_ref = db.reference('/Tungible_test2')
        
        all = []
        for j in range(0, len(centers)):
                person = {
                        "manAffinA" : np.cos(np.pi*thetas[j]/180),
                        "manAffinB" : np.sin(np.pi*thetas[j]/180),
                        "manAffinC" : -np.sin(np.pi*thetas[j]/180),
                        "manAffinD" : np.cos(np.pi*thetas[j]/180),
                        "manPlaceX" : centers[j][0],
                        "manPlaceY" : centers[j][1]
                }
                all.append(person)
                
                json = "contents"
                man = all
                
                print(np.cos(np.pi*thetas[j]/180))
                
        users_ref.set({
                "Tungible2" : {
                        "changePoint" : "No",
                        "man" : [ man ]
                }
        })
        
 

if __name__ == "__main__" :
        main()
