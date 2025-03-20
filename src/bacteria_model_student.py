import numpy as np
import matplotlib.pyplot as plt

# 定义两个数学模型
def V(t, tau):
    return 1 - np.exp(-t / tau)

def W(t, A, tau):
    return A * (np.exp(-t / tau) - 1 + t / tau)

# 绘制实验数据和模型拟合图
def plot_data_and_fit(t_data, data, model, params, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(t_data, data, label='Experimental data', color='red', s=10)
    t_fit = np.linspace(min(t_data), max(t_data), 300)
    data_fit = model(t_fit, *params)
    plt.plot(t_fit, data_fit, label='Fitted model', color='blue')
    plt.xlabel('Time (t)')
    plt.ylabel('OD')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# 主函数
def main():
    # 加载实验数据
    v_data = np.loadtxt('data/g149novivkA.txt ')
    w_data = np.loadtxt('data/g149novivkB.txt')
    
    # 假设V和W数据文件的第一列是时间数据，第二列是OD值
    t_v_data = v_data[:, 0]
    v_od_data = v_data[:, 1]
    t_w_data = w_data[:, 0]
    w_od_data = w_data[:, 1]
    
    # 绘制V(t)实验数据图
    plt.figure(figsize=(8, 6))
    plt.scatter(t_v_data, v_od_data, label='V(t) Experimental data', color='red', s=10)
    plt.xlabel('Time (t)')
    plt.ylabel('OD')
    plt.title('V(t) Experimental Data')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # 绘制W(t)实验数据图
    plt.figure(figsize=(8, 6))
    plt.scatter(t_w_data, w_od_data, label='W(t) Experimental data', color='red', s=10)
    plt.xlabel('Time (t)')
    plt.ylabel('OD')
    plt.title('W(t) Experimental Data')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # 绘制V(t)模型拟合图
    plot_data_and_fit(t_v_data, v_od_data, V, [1], 'V(t) Model Fitting')
    
    # 绘制W(t)模型拟合图
    plot_data_and_fit(t_w_data, w_od_data, W, [1, 1], 'W(t) Model Fitting')

if __name__ == "__main__":
    main()

    # 绘制数据和拟合图，并保存图片
    plot_data_and_fit(time_V, concentration_V, fit_params_V, "V.txt data fitting", "V_data_fit.png")
    plot_data_and_fit(time_N, concentration_N, fit_params_N, "N.txt data fitting", "N_data_fit.png")
