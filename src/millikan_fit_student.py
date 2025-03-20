import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """
    加载数据文件
    """
    try:
        data = np.loadtxt(filename)
        return data[:, 0], data[:, 1]
    except Exception as e:
        raise FileNotFoundError(f"无法加载文件：{filename}") from e

def calculate_parameters(x, y):
    """
    计算输入x和y的参数
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据不能为空")

    n = len(y)
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x**2)
    Eyy = np.mean(y**2)
    Exy = np.mean(x * y)

    denominator = Ex * Ex - n
    if denominator == 0:
        raise ValueError("无法计算参数，分母为零")

    m = (Ey * Exx - Ex * Ey) / denominator
    c = (Exx * Ey - Ex * Exy) / denominator

    return m, c, Ex, Ey, Exx, Exy

def plot_data_and_fit(x, y, m, c):
    """
    绘制数据点和拟合直线
    """
    if np.isnan(m) or np.isnan(c):
        raise ValueError("斜率和截距不能为NaN")

    fig, ax = plt.subplots()
    ax.scatter(x, y, label="实验数据")
    ax.plot(x, m * x + c, 'r', label="拟合直线")
    ax.set_xlabel("频率 (ν)")
    ax.set_ylabel("电压 (V)")
    ax.set_title("Millikan光电效应拟合")
    ax.legend()
    plt.show()

def calculate_planck_constant(m, e=1.602e-19):
    """
    计算普朗克常量
    """
    h = m * e
    return h

def main():
    """
    主函数
    """
    try:
        # 数据文件路径
        filename = "millikan.txt"

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

        # 绘制数据和拟合直线
        plot_data_and_fit(x, y, m, c)

        # 计算普朗克常量
        h = calculate_planck_constant(m)
        print(f"计算得到的普朗克常量 h = {h:.6e} J·s")

        # 保存图像
        plt.savefig("millikan_fit.png", dpi=300)
        plt.close()

    except Exception as e:
        print(f"程序出错: {str(e)}")

if __name__ == "__main__":
    main()
