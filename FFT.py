# -*- coding: utf-8 -*-


import os
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# import math

        

def Fourier(acc):
    # 对读取的波数据进行傅里叶变换，并输出图像
    accV = np.ravel(acc) # 必须转化为向量才可以进行傅里叶变换（n行1列的矩阵不可以）
    
    N = len(acc)                                    # 显示波形长度
    readt = int(np.power(2, np.ceil(np.log2(N))))   # 补零后的长度

    M = np.zeros(readt)                             # 本行及下一行是补零操作
    M[0:N-1] = accV[0:N-1]                          # M表示补零后的波形时序列
    
    accFFT = fft(M)/(readt*0.001)                   # 傅里叶变换，注意要除以总时长T=readt*0.001
    
    N = readt*0.5 #重新给N赋值
    f = np.arange(N)
    
    half_f = f[range(int(N))] / (readt*0.001)       # 设置对半的频率
    half_accFFT = accFFT[range(int(N))]
    
    abs_accFFT = np.abs(half_accFFT)                # 取傅里叶变换的模

    return abs_accFFT, half_f, M
    
def plot_graph(tup):
    abs_accFFT = tup[0]
    half_f = tup[1]
    acc = tup[2]

   
    # =====================输出频谱图=========================#
    fig,ax = plt.subplots(figsize=(6,4))  #以下为输出图像
    ax.plot(half_f,abs_accFFT)
    # ax.set_xscale("log")
    # ax.set_yscale("log")
    # plt.xlim(0.1,10) # 设置x轴范围
    # plt.ylim(0,max(abs_accFFT)*1.1) #设置y轴范围
    plt.xticks(fontsize=20) #设置x轴标签字体
    plt.yticks(fontsize=20)
    plt.title('Fourier Transform',fontsize=20)
    #plt.show()
    # =======================================================#
    
if __name__ == "__main__": # 仅当程序当被作为主程序运行时执行下方命令（被其他程序调用时则不执行）
    ALL_DATA_PAHT = "./data/data_c4"
    dir_list = ["v1", "v2", "v3", "v4","v5", "v6", "v7", "v8","v9", "v10"]
    file_list = ["01", "02","03", "04", "05", "06", "07", "08" ,"09", "10", "11", "12","13", "14", "15", "16", "17", "18"]

    for d in dir_list:
        dir_path = d
        for i in file_list:
            file_path = ALL_DATA_PAHT + "/" + str(dir_path)+ "/" + str(i) + '.csv'
       
        
            acc = np.loadtxt(file_path)
            tup = Fourier(acc)
            plot_graph(tup)
            plt.savefig(str(dir_path) +'-'+ str(i) + '.png' )
    
    