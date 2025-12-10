import matplotlib.pyplot as plt

coords = [list(map(int, l.strip().split(','))) for l in open('input/09.txt').readlines()]

x, y = zip(*coords)
plt.plot(x, y, marker='o')
plt.plot([x[-1], x[0]], [y[-1], y[0]])
plt.plot([6271, 6271, 94582, 94582, 6271], [68563, 50174, 50174, 68563, 68563])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Connected Coordinates Plot")
plt.axis('equal')
plt.grid(True)

plt.show()
