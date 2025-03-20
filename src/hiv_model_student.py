import numpy as np
import matplotlib.pyplot as plt

class HIVModel:
    def __init__(self, A=1.0, alpha=0.1, B=0.5, beta=0.1):
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta

    def viral_load(self, time):
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)

def load_hiv_data(filename):
    try:
        data = np.loadtxt(filename)
        return data[:, 0], data[:, 1]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None, None
    except ValueError:
        print(f"Error loading file {filename}. Please check the file format.")
        return None, None

def plot_data_and_model(t, viral_load, params):
    A, alpha, B, beta = params
    model_load = HIV_model.viral_load(HIV_model(A, alpha, B, beta), t)
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
    t_data, viral_load_data = load_hiv_data('data/HIVseries.csv')
    
    if t_data is None or viral_load_data is None:
        return
    
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
