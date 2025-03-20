import numpy as np
import matplotlib.pyplot as plt

class BacteriaModel:
    def __init__(self, A=1.0, tau=2.0):
        self.A = A
        self.tau = tau

    def v_model(self, t):
        return 1 - np.exp(-t / self.tau)

    def w_model(self, t):
        return self.A * (np.exp(-t / self.tau) - 1 + t / self.tau)

def load_bacteria_data(filename):
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]

# 绘制模型曲线
def plot_models(A_values, tau_values):
    t = np.linspace(0, 10, 400)
    plt.figure(figsize=(10, 6))
    
    for A in A_values:
        for tau in tau_values:
            w = W(t, A, tau)
            plt.plot(t, w, label=f'W(A={A}, τ={tau})')

    plt.xlabel('Time (t)')
    plt.ylabel('OD')
    plt.title('Model Curves for Different Parameters')
    plt.legend()
    plt.grid(True)
    plt.show()

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
    # 参数设置
    A_values = [1, 2, 3]
    tau_values = [1, 2, 3]
    
    # 绘制不同参数下的模型曲线
    plot_models(A_values, tau_values)
    
    # 加载实验数据
    t_v_data, v_od_data = load_data('data/g149novickA.txt')
    t_w_data, w_od_data = load_data('data/g149novickB.txt')
    
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
    plot_data_and_fit(t_v_data, v_od_data, V, [2.0], 'V(t) Model Fitting')
    
    # 绘制W(t)模型拟合图
    plot_data_and_fit(t_w_data, w_od_data, W, [1.0, 2.0], 'W(t) Model Fitting')

if __name__ == "__main__":
    main()
