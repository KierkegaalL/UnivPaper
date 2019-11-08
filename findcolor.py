# coding:utf-8
import cv2
import findmarker

def find_color(src, lower_color, upper_color, s_th, v_th):
    
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    if lower_color > upper_color:
        ret, h_dst_1 = cv2.threshold(h, lower_color, 255, cv2.THRESH_BINARY) 
        ret, h_dst_2 = cv2.threshold(h, upper_color,  255, cv2.THRESH_BINARY_INV)
        dst = cv2.bitwise_or(h_dst_1, h_dst_2)
        
    else:
        ret, dst = cv2.threshold(h,   lower_color, 255, cv2.THRESH_TOZERO) 
        ret, dst = cv2.threshold(dst, upper_color,  255, cv2.THRESH_TOZERO_INV)
        ret, dst = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY)
        
    ret, s_dst = cv2.threshold(s, s_th, 255, cv2.THRESH_BINARY)
    ret, v_dst = cv2.threshold(v, v_th, 255, cv2.THRESH_BINARY)
        
    dst = cv2.bitwise_and(dst, s_dst)
    dst = cv2.bitwise_and(dst, v_dst)

    return dst




def rw(path):
    img = cv2.imread(path)
    

    red_img = find_color(img, 175, 5,  100, 100)
    orange_img = find_color(img, 8, 20, 100, 100)
    yellow_img = find_color(img, 20, 29, 50, 50)
    yg_img = find_color(img, 30, 42, 80, 80)
    green_img = find_color(img, 42, 58, 50, 50)
    bg_img = find_color(img, 60, 79, 50, 80)
    blue_img = find_color(img, 82, 101, 60, 90)
    violet_img = find_color(img, 102, 123, 40, 80)
    purple_img = find_color(img, 124, 145, 50,  50)
    rp_img = find_color(img, 146, 175, 50,  50)    
    
    prefix = '/Users/OkuRyuji/sendforapp/reserch/pointmask/'

    
    if red_img is not None:
        cv2.imwrite(prefix+'red.png',red_img)
    if orange_img is not None:
        cv2.imwrite(prefix+'orange.png',orange_img)
    if yellow_img is not None:
        cv2.imwrite(prefix+'yellow.png',yellow_img)
    if green_img is not None:
        cv2.imwrite(prefix+'green.png',green_img)
    if blue_img is not None:
        cv2.imwrite(prefix+'blue.png',blue_img)
    if purple_img is not None:
        cv2.imwrite(prefix+'purple.png',purple_img)
    if rp_img is not None:
        cv2.imwrite(prefix+'rp.png',rp_img)
    if violet_img is not None:
        cv2.imwrite(prefix+'violet.png',violet_img)
    if yg_img is not None:
        cv2.imwrite(prefix+'yg.png',yg_img)
    if bg_img is not None:
        cv2.imwrite(prefix+'bg.png',bg_img)

        
    findmarker.rw(prefix)
    
if __name__=="__main__":
    rw(prefix)
    cv2.destroyAllWindows()
    
