
import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False


def simple_plot():
    """
    simple plot
    """
    # 生成测试数据
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y_cos, y_sin = np.cos(x), np.sin(x)

    # 生成画布，并设定标题
    plt.figure(figsize=(8, 6), dpi=80)
    plt.title("简单曲线图")
    plt.grid(True)

    # 设置X轴
    plt.xlabel("X轴")
    plt.xlim(-4.0, 4.0)
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

    # 设置Y轴
    plt.ylabel("Y轴")
    plt.ylim(-1.0, 1.0)
    plt.yticks(np.linspace(-1, 1, 9, endpoint=True))

    # 画两条曲线
    plt.plot(x, y_cos, "b--", linewidth=2.0, label="cos示例")
    plt.plot(x, y_sin, "g-", linewidth=2.0, label="sin示例")

    # 设置图例位置,loc可以为[upper, lower, left, right, center]
    plt.legend(loc="upper left", shadow=True)

    # 图形显示
    plt.show()
    
simple_plot()
    