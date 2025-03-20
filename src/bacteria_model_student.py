import numpy as np
import matplotlib.pyplot as plt

# 定义逻辑斯蒂生长模型（Logistic模型）
def logistic_model(t, K, P0, r):
    """
    Logistic生长模型
    t: 时间
    K: 最大承载量
    P0: 初始细菌浓度
    r: 增长率
    """
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# 读取数据
def read_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=5)
    return data[:, 0], data[:, 1]

# 绘制实验数据图
def plot_experiment_data(time, concentration, title, save_path):
    plt.figure(figsize=(10, 6))
    plt.scatter(time, concentration, label="experimental data", color="blue")
    plt.title(title)
    plt.xlabel("time (h)")
    plt.ylabel("OD")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

# 绘制实验数据和模型拟合图
def plot_data_and_fit(time, concentration, fit_params, title, save_path):
    plt.figure(figsize=(10, 6))
    plt.scatter(time, concentration, label="experimental data", color="blue")

    # 使用拟合参数绘制模型曲线
    c_fit = np.linspace(min(time), max(time), 100)
    f_fit = logistic_model(c_fit, fit_params[0], fit_params[1], fit_params[2])

    plt.plot(c_fit, f_fit, label="model fitting", color="red", linestyle="--")

    plt.title(title)
    plt.xlabel("time (h)")
    plt.ylabel("OD")
    plt.legend()
    plt.grid(True)

    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

# 主程序
if __name__ == "__main__":
    # 读取数据
    time_V, concentration_V = read_data("data/g149novickA.txt")
    time_N, concentration_N = read_data("data/g149novickB.txt")

    # 拟合模型
    fit_params_V = (100, 0.1, 0.5)  # 假设的拟合参数
    fit_params_N = (100, 0.1, 0.5)  # 假设的拟合参数

    # 绘制实验数据图
    plot_experiment_data(time_V, concentration_V, "V.txt experimental data", "V_experiment_data.png")
    plot_experiment_data(time_N, concentration_N, "N.txt experimental data", "N_experiment_data.png")

    # 绘制数据和拟合图，并保存图片
    plot_data_and_fit(time_V, concentration_V, fit_params_V, "V.txt data fitting", "V_data_fit.png")
    plot_data_and_fit(time_N, concentration_N, fit_params_N, "N.txt data fitting", "N_data_fit.png")
