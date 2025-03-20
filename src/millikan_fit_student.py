import numpy as np

def load_data(filename):
    """
    加载数据文件
    """
    try:
        data = np.loadtxt(filename)
        if data.shape[1] != 2:
            raise ValueError("数据文件格式不正确，必须包含两列数据")
        x = data[:, 0]
        y = data[:, 1]
        if len(x) != len(y):
            raise ValueError("x和y数值长度必须相同")
        return x, y
    except Exception as e:
        raise FileNotFoundError(f"无法加载文件: {filename}") from e

def calculate_parameters(x, y):
    """
    计算最小二乘拟合参数
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("输入数据不能为空")
    if len(x) != len(y):
        raise ValueError("x和y数值长度必须相同")

    N = len(x)
    Ex = np.mean(x)
    Ey = np.mean(y)
    Exx = np.mean(x**2)
    Exy = np.mean(x*y)

    denominator = Exx - Ex**2
    if denominator == 0:
        raise ValueError("无法计算参数. 分母为零")
    m = (Exy - Ex*Ey) / denominator
    c = Ey - m * Ex

    return m, c, Ex, Ey, Exx, Exy

def calculate_planck_constant(m):
    """
    计算普朗克常数
    """
    if m <= 0:
        raise ValueError("斜率必须为正数")
    e = 1.602e-19  # 电子电荷
    h = m * e
    return h
