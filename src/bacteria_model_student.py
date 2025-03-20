import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义两个数学模型
def V(t, tau):
    return 1 - np.exp(-t / tau)

def W(t, A, tau):
    return A * (np.exp(-t / tau) - 1 + t / tau)

# 绘制不同参数下的模型曲线
def plot_models(A_values, tau_values):
    t = np.linspace(0, 10, 400)
    plt.figure(figsize=(12, 6))
    
    for A in A_values:
        for tau in tau_values:
            v = V(t, tau)
            w = W(t, A, tau)
            plt.plot(t, v, label=f'V(τ={tau})')
            plt.plot(t, w, label=f'W(A={A}, τ={tau})')

    plt.xlabel('Time (t)')
    plt.ylabel('OD')
    plt.title('Model Curves for Different Parameters')
    plt.legend()
    plt.grid(True)
    plt.show()

# 拟合实验数据
def fit_data(t_data, data, model, initial_guess):
    popt, _ = curve_fit(model, t_data, data, p0=initial_guess)
    return popt

# 绘制实验数据和拟合曲线
def plot_data_and_fit(t_data, data, model, popt, title):
    t_fit = np.linspace(min(t_data), max(t_data), 400)
    data_fit = model(t_fit, *popt)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(t_data, data, label='Experimental data', color='red', s=10)
    plt.plot(t_fit, data_fit, label='Fitted model', color='blue')
    plt.xlabel('Time (t)')
    plt.ylabel('OD')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# 主函数
def main():
    # 参数设置
    A_values = [1, 2, 3]
    tau_values = [1, 2, 3]
    
    # 绘制不同参数下的模型曲线
    plot_models(A_values, tau_values)
    
    # 加载实验数据
    v_data = np.loadtxt('https://www.physics.upenn.edu/biophys/PMLS/Datasets/15novick/g149novickA.txt')
    w_data = np.loadtxt('https://www.physics.upenn.edu/biophys/PMLS/Datasets/15novick/g149novickB.txt')
    
    # 假设V和W数据文件的第一列是时间数据，第二列是OD值
    t_v_data = v_data[:, 0]
    v_od_data = v_data[:, 1]
    t_w_data = w_data[:, 0]
    w_od_data = w_data[:, 1]
    
    # 拟合V(t)模型
    popt_v = fit_data(t_v_data, v_od_data, V, [1])  # 使用初始猜测参数
    print(f"Fitted parameters for V(t): {popt_v}")
    
    # 绘制V(t)实验数据和拟合曲线
    plot_data_and_fit(t_v_data, v_od_data, V, popt_v, 'V(t) Experimental Data and Fitted Curve')
    
    # 拟合W(t)模型
    popt_w = fit_data(t_w_data, w_od_data, W, [1, 1])  # 使用初始猜测参数
    print(f"Fitted parameters for W(t): {popt_w}")
    
    # 绘制W(t)实验数据和拟合曲线
    plot_data_and_fit(t_w_data, w_od_data, W, popt_w, 'W(t) Experimental Data and Fitted Curve')

if __name__ == "__main__":
    main()
