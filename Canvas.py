# Import from pip:
import tkinter as tk

# Debuging:
print("Tal: You are in the Canvas.py file")

# Variables:
path = '.\Pictures\logo.png'

# Working:
def Canvas(x, y):
    window = tk.Tk()

    # Frame:
    size = str(x+10) + 'x' + str(y+55)
    window.geometry(size)
    window.title('Pic2Peak')

    # Buttons:
    button = tk.Button(window, text="Upload image", font=('Arial', 16), background='light grey')
    button.pack(pady=2)

    # Workbox:
    canvas = tk.Canvas(window, width=x, height=y, bg='white')
    canvas.pack(anchor=tk.CENTER, expand=True)

    # Picture:
    logo = tk.PhotoImage(file = path)
    canvas.create_image((x/2, y/2), image=logo)


    window.mainloop()