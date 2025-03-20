"""
Logistic映射与混沌系统研究
"""

import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        x: 迭代序列数组
    """
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x

def plot_time_series(r, x0, n):
    """
    绘制时间序列图
    
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
        
    返回:
        fig: matplotlib图像对象
    """
    x = iterate_logistic(r, x0, n)
    fig, ax = plt.subplots()
    ax.plot(x)
    ax.set_title(f'Logistic Map Time Series (r={r})')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('x')
    return fig

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图
    
    参数:
        r_min: r的最小值
        r_max: r的最大值
        n_r: r的取值个数
        n_iterations: 每个r值的迭代次数
        n_discard: 每个r值丢弃的初始迭代点数
        
    返回:
        fig: matplotlib图像对象
    """
    r_values = np.linspace(r_min, r_max, n_r)
    fig, ax = plt.subplots(figsize=(10, 6))
    for r in r_values:
        x = iterate_logistic(r, 0.5, n_iterations)
        ax.plot(x[n_discard:], ',k', alpha=0.1)
    ax.set_title('Logistic Map Bifurcation Diagram')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('x')
    ax.set_xlim(0, n_iterations)
    ax.set_ylim(0, 1)
    return fig

def main():
    """主函数"""
    # 时间序列分析
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 100
    
    for r in r_values:
        fig = plot_time_series(r, x0, n)
        fig.savefig(f"logistic_r{r}.png", dpi=300)
        plt.close(fig)
    
    # 分岔图分析
    fig = plot_bifurcation(2.5, 4.0, 1000, 1000, 100)
    fig.savefig("bifurcation.png", dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    main()
