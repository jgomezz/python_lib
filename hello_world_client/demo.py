import tkinter as tk
from tkinter import simpledialog

def draw_knots(canvas, number):
    # Limpiar el canvas
    canvas.delete("all")
    # Posiciones iniciales para dibujar
    x, y = 50, 50
    knot_size = 10

    # Dibujar la cuerda
    canvas.create_line(x - 20, y, x + 20 + knot_size * number, y, fill="brown", width=3)

    # Dibujar los nudos en la cuerda
    for i in range(number):
        canvas.create_oval(x + knot_size * i, y - knot_size, x + knot_size * i + knot_size, y + knot_size, fill="blue")

def get_number(canvas):
    # Pedir al usuario un número
    number = simpledialog.askinteger("Input", "Enter a number:")
    if number is not None and number > 0:
        draw_knots(canvas, number)

def main():
    root = tk.Tk()
    root.title("Visualización de Quipu")

    # Canvas para dibujar el quipu
    canvas = tk.Canvas(root, width=400, height=200)
    canvas.pack()

    # Botón para obtener el número
    button = tk.Button(root, text="Ingrese un número para mostrar el quipu", command=lambda: get_number(canvas))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
