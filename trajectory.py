import cvxpy as cp
from cvxpy.atoms.norm import norm2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x_1 = np.load('x_data.npy')
y_1 = np.load('y_data.npy')
z_1 = np.load('z_data.npy')

x1_f = np.array([2,0,1,0,0,0])
x2_f = np.array([2,6,1,0,0,0])
x3_f = np.array([-2,6,1,0,0,0])
x4_f = np.array([-2,0,1,0,0,0])

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlim3d([-3, 3])
ax.set_ylim3d([-0.5, 7])
ax.set_zlim3d([0, 3])
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
ax.set_zlabel('Z(t)')
ax.set_title('Trajectory of Agents')

dataSet1 = np.array([x_1[0], y_1[0], z_1[0]])
dataSet2 = np.array([x_1[1], y_1[1], z_1[1]])
dataSet3 = np.array([x_1[2], y_1[2], z_1[2]])
dataSet4 = np.array([x_1[3], y_1[3], z_1[3]])
num = len(z_1[0])

line1, = ax.plot3D(0,0,0,"blue")
line2, = ax.plot3D(0,0,0,"orange")
line3, = ax.plot3D(0,0,0,"green")
line4, = ax.plot3D(0,0,0,"red")
point1, = ax.plot3D(0,0,1,"blue", marker="o")
point2, = ax.plot3D(0,0,1,"orange", marker="o")
point3, = ax.plot3D(0,0,1,"green", marker="o")
point4, = ax.plot3D(0,0,1,"red", marker="o")

ax.scatter3D(x1_f[0], x1_f[1], x1_f[2], color = "blue", marker="^")
ax.scatter3D(x2_f[0], x2_f[1], x2_f[2], color = "orange", marker="^")
ax.scatter3D(x3_f[0], x3_f[1], x3_f[2], color = "green", marker="^")
ax.scatter3D(x4_f[0], x4_f[1], x4_f[2], color = "red", marker="^")

def func(i):
    line1.set_xdata(dataSet1[0][:i])
    line1.set_ydata(dataSet1[1][:i])
    line1.set_3d_properties(dataSet1[2][:i])
    point1.set_xdata(dataSet1[0][i-1])
    point1.set_ydata(dataSet1[1][i-1])
    point1.set_3d_properties(dataSet1[2][i-1])
    line2.set_xdata(dataSet2[0][:i])
    line2.set_ydata(dataSet2[1][:i])
    line2.set_3d_properties(dataSet2[2][:i])
    point2.set_xdata(dataSet2[0][i-1])
    point2.set_ydata(dataSet2[1][i-1])
    point2.set_3d_properties(dataSet2[2][i-1])
    line3.set_xdata(dataSet3[0][:i])
    line3.set_ydata(dataSet3[1][:i])
    line3.set_3d_properties(dataSet3[2][:i])
    point3.set_xdata(dataSet3[0][i-1])
    point3.set_ydata(dataSet3[1][i-1])
    point3.set_3d_properties(dataSet3[2][i-1])
    line4.set_xdata(dataSet4[0][:i])
    line4.set_ydata(dataSet4[1][:i])
    line4.set_3d_properties(dataSet4[2][:i])
    point4.set_xdata(dataSet4[0][i-1])
    point4.set_ydata(dataSet4[1][i-1])
    point4.set_3d_properties(dataSet4[2][i-1])
    return line1, line2, line3, line4, point1, point2, point3, point4

animation = FuncAnimation(fig, func, frames=range(num), interval=200, blit=False,save_count=1500)
animation.save(r'r_68.mp4')
plt.show()