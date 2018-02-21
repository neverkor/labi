import data
import matplotlib.pyplot as plt

# Графическое изображение (не обязательно, так нагляднее)
def graphic():
    circle = plt.Circle((data.centr_x, data.centr_y), data.radius, color='blue', fill=False)
    fig, ax = plt.subplots()
    ax.add_artist(circle)
    ax.axis("equal")
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    plt.scatter(data.x, data.y, s=0.5, color='red')
    plt.scatter(data.os_x, data.os_y, s=1, color='black')
    plt.show()
    data.os_x = []
    data.os_y = data.y
