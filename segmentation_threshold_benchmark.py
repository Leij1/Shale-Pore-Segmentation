import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pathlib import Path


def gen_foreground(img_path,res_path):
    file_list=os.listdir(img_path) #遍历该目录下的所有图片文件 
    for i,fi in enumerate(file_list):
        basename = os.path.basename(file_list[i])
        file_name = os.path.splitext(basename)[0]
        img = cv.imread(img_path+'/'+file_list[i])
        img0= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        size =img0.shape
        w = size[1] #宽度
        h = size[0] #高度
        #阈值分割
        ret, img00 = cv.threshold(img0, 90, 255, cv.THRESH_BINARY)
        filename1=res_path+'/'+file_name+'.png'
        cv.imwrite(filename1, img00, [cv.IMWRITE_PNG_COMPRESSION, 0]) 
        ret, thresh1 = cv.threshold(img0, 0, 255, cv.THRESH_OTSU) 
        filename2=res_path+'-OTSU/'+file_name+'.png'  
        cv.imwrite(filename2, thresh1, [cv.IMWRITE_PNG_COMPRESSION, 0]) 
        ret, thresh2 = cv.threshold(img0, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
        filename3=res_path+'-TRIANGLE/'+file_name+'.png' 
        cv.imwrite(filename3, thresh2, [cv.IMWRITE_PNG_COMPRESSION, 0]) 
        thresh3 = cv.adaptiveThreshold(img0, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
        filename4=res_path+'-adaptive/'+file_name+'.png' 
        cv.imwrite(filename4, thresh3, [cv.IMWRITE_PNG_COMPRESSION, 0]) 
        #聚类
        grayImage=img0
        rows, cols = grayImage.shape[:]
        data = grayImage.reshape((rows * cols, 1))
        data = np.float32(data)
        #定义中心 (type,max_iter,epsilon)
        criteria = (cv.TERM_CRITERIA_EPS +
            cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        #设置标签
        flags = cv.KMEANS_RANDOM_CENTERS
        #K-Means聚类 聚集成4类
        compactness, labels, centers = cv.kmeans(data, 4, None, criteria, 10, flags)
        #生成最终图像
        dst = labels.reshape((grayImage.shape[0], grayImage.shape[1]))
        for i in range(rows):
            for j in range(cols):
                if dst[i-1][j-1]==0:
                  dst[i-1][j-1]=0
                else:
                     dst[i-1][j-1]=255
        filename5=res_path+'-kmeans/'+file_name+'.png' 
        cv.imwrite(filename5, dst,[cv.IMWRITE_PNG_COMPRESSION, 0])
        #孔隙率计算
        count0=0
        count1=0
        count2=0
        count3=0
        count4=0
        np.array(img00)
        for list0 in img00:
            for element0 in list0:
                if element0==0:
                    count0+=1
        np.array(thresh1)
        for list1 in thresh1:
            for element1 in list1:
                if element1==0:
                    count1+=1
        np.array(thresh2)
        for list2 in thresh2:
            for element2 in list2:
                if element2==0:
                    count2+=1
        np.array(thresh3)
        for list3 in thresh3:
            for element3 in list3:
                if element3==0:
                    count3+=1
        np.array(dst)
        for list4 in dst:
            for element4 in list4:
                if element4==0:
                    count4+=1
        file=open('D:\image\81-4b\example.txt', 'a')
        aaa=w*h
        str11=file_name+'\t'+str(aaa)+'\t'+str(count0/aaa)+'\t'+str(count1/aaa)+'\t'+str(count2/aaa)+'\t'+str(count3/aaa)+'\t'+str(count4/aaa)+'\n'
        file.write(str11)
        file.close()


if __name__ == "__main__":
    path="D:\image\81-4b\images"
    path1="D:\image\81-4b\iithreshold"
    gen_foreground(path,path1)
    

