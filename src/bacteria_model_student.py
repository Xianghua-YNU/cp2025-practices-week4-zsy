import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 定义细菌生长模型，例如指数增长模型
def growth_model(t, a, b, c):
    return a * np.exp(-b * t) + c

# 读取实验数据
def load_data(path):
    data = np.loadtxt(path)
    return data[:, 0], data[:, 1]  # 假设第一列是时间，第二列是生长量

# 绘制实验数据和模型拟合图
def plot_data_and_fit(title, t, v, model, params):
    plt.figure(figsize=(8, 6))
    plt.scatter(t, v, label='Experimental data', color='red', s=10)
    t_fit = np.linspace(min(t), max(t), 300)
    v_fit = model(t_fit, *params)
    plt.plot(t_fit, v_fit, label='Fitted model', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Growth')
    plt.title(title)
    plt.legend()
    plt.show()

# 主函数
def main():
    # V实验数据路径
    path_v = '/workspaces/cp2025-practices-week4-zsy/data/g149novickA.txt'  
    # W实验数据路径
    path_w = '/workspaces/cp2025-practices-week4-zsy/data/g149novickB.txt'  
    
    # 读取V数据
    t_v, v = load_data(path_v)
    
    # 使用curve_fit进行V数据拟合
    initial_guess_v = [1, 0.1, 0]  # 初始猜测参数
    params_v, covariance_v = curve_fit(growth_model, t_v, v, p0=initial_guess_v)
    
    print(f"Fitted parameters for V: {params_v}")
    
    # 绘制V数据和拟合曲线
    plot_data_and_fit('Bacterial Growth Model Fitting for V', t_v, v, growth_model, params_v)

    # 读取W数据
    t_w, w = load_data(path_w)
    
    # 使用curve_fit进行W数据拟合
    initial_guess_w = [1, 0.1, 0]  # 初始猜测参数
    params_w, covariance_w = curve_fit(growth_model, t_w, w, p0=initial_guess_w)
    
    print(f"Fitted parameters for W: {params_w}")
    
    # 绘制W数据和拟合曲线
    plot_data_and_fit('Bacterial Growth Model Fitting for W', t_w, w, growth_model, params_w)

if __name__ == "__main__":
    main()
try:
    from scipy.optimize import curve_fit
except ImportError:
    print("Error: scipy module is not installed. Please install it using 'pip install scipy'.")
    exit(1)
