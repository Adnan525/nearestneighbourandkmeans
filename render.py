from tkinter import *

tk = Tk()
window = Canvas(tk, bg="white", height=700, width=1000)
radius = 3
scale = 70
offset = 200
colors_set = ["grey", "magenta", "green", "orange"]


def renderPoints(dataset, color):
    for item in dataset:
        renderOval(item, color)


def renderOval(point, colour):
    window.create_oval(point[0] * scale - radius + offset,
                       point[1] * scale - radius + offset,
                       point[0] * scale + radius + offset,
                       point[1] * scale + radius + offset,
                       outline="white", fill=colour)


def renderLine(point1: list[float], point2: list[float], colour: float):
    window.create_line(point1[0] * scale + offset,
                       point1[1] * scale + offset,
                       point2[0] * scale + offset,
                       point2[1] * scale + offset,
                       fill=colour)


def renderClusters(getCluster, centerPoints):
    color_index = 0
    for indexCenter in range(0, len(centerPoints)):
        for point in getCluster[indexCenter]:
            renderLine(centerPoints[indexCenter], point, colors_set[color_index % 4])

        renderPoints(getCluster[indexCenter], "blue")
        renderPoints([centerPoints[indexCenter]], "red")
        color_index += 1


def run_tk_window():
    window.pack()
    tk.mainloop()
