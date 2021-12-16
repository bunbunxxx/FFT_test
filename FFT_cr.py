# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:23:00 2020

    Fourier Transfrom for DACSAR

@author: Cr
"""

import os
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# import math


def Fourier(acc):
    # 对读取的地震波数据进行傅里叶变换，并输出图像
    accV = np.ravel(acc) # 必须转化为向量才可以进行傅里叶变换（n行1列的矩阵不可以）
    
    N = len(acc)                                    # 显示波形长度
    readt = int(np.power(2, np.ceil(np.log2(N))))   # 补零后的长度

    M = np.zeros(readt)                             # 本行及下一行是补零操作
    M[0:N-1] = accV[0:N-1]                          # M表示补零后的加速度
    
    accFFT = fft(M)/(readt*0.001)                    # 傅里叶变换，注意要除以总时长T=readt*0.01，最终单位gal*sec
    
    N = readt*0.5 #重新给N赋值
    f = np.arange(N)
    
    half_f = f[range(int(N))] / (readt*0.001) # 设置对半的频率
    half_accFFT = accFFT[range(int(N))]
    
    abs_accFFT = np.abs(half_accFFT) # 取傅里叶变换的模

    return abs_accFFT, half_f
    
def plot_graph(tup):
    abs_accFFT = tup[0]
    half_f = tup[1]

    # ===================输出波形图=====================#
    fig,ax = plt.subplots(figsize=(6,4)) # 以下为输出图像
    ax.plot(np.arange(readt)*0.001,M)
    # plt.xlim(0,50) # 设置x轴范围
    plt.ylim(min(M)*1.1,max(M)*1.1) #设置y轴范围
    plt.xticks(fontsize=20) #设置x轴标签字体
    plt.yticks(fontsize=20)
    plt.title('Acceleration (Unit: gal)',fontsize=20)
    # =======================================================#
    
    # =====================输出频谱图=========================#
    fig,ax = plt.subplots(figsize=(6,4)) # 以下为输出图像
    ax.plot(half_f,abs_accFFT)
    # ax.set_xscale("log")
    # ax.set_yscale("log")
    # plt.xlim(0.1,10) # 设置x轴范围
    # plt.ylim(0,max(abs_accFFT)*1.1) #设置y轴范围
    plt.xticks(fontsize=20) #设置x轴标签字体
    plt.yticks(fontsize=20)
    plt.title('Fourier Transform',fontsize=20)
    # =======================================================#
    
   
def do_all(): 
    acc = np.loadtxt('res01.dat',skiprows=1)[:,2:] #注意乘以0.01可以将地震加速度单位从gal化为m/s²
    freq01 = Fourier(acc[:,0])[0]
    freq02 = Fourier(acc[:,1])[0]
    plot_graph(freq01)
    plot_graph(freq02)
    return freq01,freq02
