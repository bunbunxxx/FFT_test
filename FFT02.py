
import os
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# import math

        

def Fourier(acc):
    # 筋電データに対して、フーリエ変換をする
    accV = np.ravel(acc) # ベクトルに変更してから　フーリエ変換　必须转化为向量才可以进行傅里叶变换（n行1列的矩阵不可以）
    
    N = len(acc)                                    #　波の長さ　显示波形长度
    readt = int(np.power(2, np.ceil(np.log2(N))))   # ０を補充した後の長さ　补零后的长度

    M = np.zeros(readt)                             # 本行及下一行是补零操作
    M[0:N-1] = accV[0:N-1]                          # Mはゼロを補充した後の波の時系列　M表示补零后的波形时序列
    
    accFFT = fft(M)/(readt*0.001)                   # フーリエ変換　傅里叶变换，注意要除以总时长T=readt*0.001
    
    N = readt*0.5                                   #　Nを半分にする　重新给N赋值
    f = np.arange(N)
    
    half_f = f[range(int(N))] / (readt*0.001)       # 周波数を半分にする　设置对半的频率
    half_accFFT = accFFT[range(int(N))]
    
    abs_accFFT = np.abs(half_accFFT)                # 絶対値を取る　フーリエ変換後の振幅になる　取傅里叶变换的模

    return abs_accFFT, half_f, M
    
def plot_graph(tup):
    abs_accFFT = tup[0]
    half_f = tup[1]
    acc = tup[2]

   
    # =====================输出频谱图（plot frenquence)=========================#
    fig,ax = plt.subplots(figsize=(6,4))  #以下为输出图像
    ax.plot(half_f  ,abs_accFFT)
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
   
        acc = np.loadtxt("07.csv") # 要让他loop到每个文件
        tup = Fourier(acc)
        plot_graph(tup)
        plt.savefig('07.png' ) #输出名和原文件名相对应
        
    
    