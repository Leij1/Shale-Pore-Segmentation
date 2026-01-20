import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# 打开Excel文件
wb = load_workbook('D:\shalegas\data\data.xlsx')
# 选择指定的工作表
sheet = wb['Sheet1']
# 选择需要读取的范围
range_str = 'A2:F76661'
cells = sheet[range_str]
# 将数据存储为二维数组
data = []
for row in cells:
    row_data = []
    for cell in row:
        row_data.append(cell.value)
    data.append(row_data)
    
data=np.log10(data)    
num_bins = 25
plt.figure(figsize=(9,6), dpi=100)
n, bins, patches = plt.hist(data[1:270][2], num_bins,color='w', edgecolor='k',hatch=r'ooo',density=1,label='频率')
#y = data[:][1]

#plt.plot(bins, y, '--', label='概率密度函数')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('')
plt.ylabel('概率密度')
plt.title('')
plt.legend()
plt.show()
