import Tkinter as tk
root = tk.Tk()

europemap = PhotoImage(file = "EUROPEMAP3.png")
europe_map_image = Label(ecanvas, image = europemap)
europe_map_image.photo = europemap
europe_map_image.grid(row = 0, column = 0)


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


root.bind('<Motion>', motion)
root.mainloop()