"""
最小二乘拟合和光电效应实验
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def load_data(filename):
    """
    加载数据文件
    
    参数:
        filename: 数据文件路径
        
    返回:
        x: 频率数据数组
        y: 电压数据数组
    """
    # 在此处编写代码，读取数据文件
    data = np.loadtxt(filename)
    x = data[:, 0]
    y = data[:, 1]
    return x, y

def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    
    参数:
        x: x坐标数组
        y: y坐标数组
        
    返回:
        m: 斜率
        c: 截距
        Ex: x的平均值
        Ey: y的平均值
        Exx: x^2的平均值
        Exy: xy的平均值
    """
    # 在此处编写代码，计算Ex, Ey, Exx, Exy, m和c
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x**2)
    Exy = np.mean(x * y)
    m = (Exy - Ex * Ey / len(x)) / (Exx - Ex**2 / len(x))
    c = Ey - m * Ex
    return m, c, Ex, Ey, Exx, Exy

def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    
    参数:
        x: x坐标数组
        y: y坐标数组
        m: 斜率
        c: 截距
    
    返回:
        fig: matplotlib图像对象
    """
    # 在此处编写代码，绘制数据点和拟合直线
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')
    ax.plot(x, m * x + c, 'r', label='Fit')
    ax.set_title('Data and Fit')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    return fig

def calculate_planck_constant(m):
    """
    计算普朗克常量
    
    参数:
        m: 斜率
        
    返回:
        h: 计算得到的普朗克常量值
        relative_error: 与实际值的相对误差(%)
    """
    # 电子电荷
    e = 1.602e-19  # C
    
    # 在此处编写代码，计算普朗克常量和相对误差
    # 提示: 实际的普朗克常量值为 6.626e-34 J·s
    e = 1.602e-19  # C
    h = e / m
    actual_h = 6.626e-34  # J·s
    relative_error = abs((h - actual_h) / actual_h) * 100
    return h, relative_error

def main():
    """主函数"""
    # 数据文件路径
    filename = "/workspaces/cp2025-practices-week4-zsy/data/millikan.txt"
    
    # 加载数据
    x, y = load_data(filename)
    
    # 计算拟合参数
    m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
    
    # 打印结果
    print(f"Ex = {Ex:.6e}")
    print(f"Ey = {Ey:.6e}")
    print(f"Exx = {Exx:.6e}")
    print(f"Exy = {Exy:.6e}")
    print(f"斜率 m = {m:.6e}")
    print(f"截距 c = {c:.6e}")
    
    # 绘制散点图
    fig_data = plt.figure()
    plt.scatter(x, y, label='Experimental Data', color='blue')
    plt.xlabel('Frequency')
    plt.ylabel('Voltage')
    plt.title('Experimental Data Scatter Plot')
    plt.legend()
    plt.savefig("experimental_data.png", dpi=300)
    plt.close(fig_data)

    # 绘制拟合直线
    fig_fit = plot_data_and_fit(x, y, m, c)
    plt.savefig("fit_line.png", dpi=300)
    plt.close(fig_fit)

    # 计算普朗克常量
    h, relative_error = calculate_planck_constant(m)
    print(f"计算得到的普朗克常量 h = {h:.6e} J·s")
    print(f"与实际值的相对误差：{relative_error:.2f}%")

if __name__ == "__main__":
    main()
