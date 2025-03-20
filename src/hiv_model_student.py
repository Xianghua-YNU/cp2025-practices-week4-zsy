import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
class HIVModel:
    def __init__(self, A, alpha, B, beta):
        # TODO: 初始化模型参数
        self.A = A  # 初始CD4+ T细胞数量
        self.alpha = alpha  # T细胞自然死亡率
        self.B = B  # 病毒清除率
        self.beta = beta  # 病毒复制率

    def viral_load(self, time):
        # TODO: 计算病毒载量
        T = self.A * np.exp(-self.alpha * time)
        V = self.B * T * np.exp(self.beta * time) / (1 + np.exp(self.beta * time)**2)
        return V
        return np.zeros_like(time)

    def plot_model(self, time):
        # TODO: 绘制模型曲线
        V = self.viral_load(time)
        plt.figure(figsize=(10, 6))
        plt.plot(time, V, label='Viral Load')
        plt.title('HIV Model')
        plt.xlabel('Time (days)')
        plt.ylabel('Viral Load')
        plt.legend()
        plt.grid(True)
        plt.savefig("HIV Model", dpi=300)
        plt.show()

def load_hiv_data(filepath):
    # TODO: 加载HIV数据
   data = np.loadtxt(filepath, delimiter=',')
   time = data[:, 0]
   viral_load = data[:, 1]
   return time, viral_load
   return np.array([]), np.array([])

def main():
    # TODO: 主函数，用于测试模型
    model = HIVModel(A=1000, alpha=0.01, B=0.1, beta=0.5)
    time = np.linspace(0, 200, 100)  # 模拟200天的数据
    model.plot_model(time)
    filepath = '/workspaces/cp2025-practices-week4-zsy/data/HIVseries.csv'  
    time_data, viral_load_data = load_hiv_data(filepath)



    # 绘制实验数据
    plt.figure(figsize=(10, 6))
    plt.plot(time_data, viral_load_data, 'o', label='Experimental Data')
    plt.plot(time, model.viral_load(time), '-', label='Model Prediction')
    plt.title('HIV Model vs Experimental Data')
    plt.xlabel('Time (days)')
    plt.ylabel('Viral Load')
    plt.legend()
    plt.grid(True)
    plt.savefig("HIV Model vs Experimental Data", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
