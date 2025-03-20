import numpy as np
import matplotlib.pyplot as plt

# 定义HIV模型
def HIV_model(t, A, alpha, B, beta):
    return A * np.exp(-alpha * t) + B * np.exp(-beta * t)

# 加载数据
def load_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    return data[:, 0], data[:, 1]

# 绘制数据和模型
def plot_data_and_model(t, viral_load, params):
    A, alpha, B, beta = params
    model_load = HIV_model(t, A, alpha, B, beta)
    plt.figure(figsize=(10, 6))
    plt.scatter(t, viral_load, label='Experimental Data', color='red', s=10)
    plt.plot(t, model_load, label='Fitted Model', color='blue')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.title('HIV Model Fitting')
    plt.legend()
    plt.grid(True)
    plt.show()

# 主函数
def main():
    # 加载实验数据
    t_data, viral_load_data = load_data('data/HIVseries.csv')
    
    # 初始参数猜测
    params = [1000, 0.1, 500, 0.05]  # A, alpha, B, beta
    
    # 绘制数据和模型
    plot_data_and_model(t_data, viral_load_data, params)

    # 手动调整参数以获得更好的拟合
    # 例如，调整alpha和beta以匹配数据的长期行为
    params[1] = 0.05  # alpha
    params[3] = 0.01  # beta
    plot_data_and_model(t_data, viral_load_data, params)

if __name__ == "__main__":
    main()
