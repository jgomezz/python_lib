from quipudigital.main import Quipu

# Hide the turtle pointer
# turtle.hideturtle()

numbers =[1000, 2024, 1234 , 5234, 120, 1000]

#numbers =[1, 20, 12 , 10, 1, 3]

quipu = Quipu(numbers)

# Use almost full width and height of the display
quipu.screen.setup(width=0.99, height=0.99)  
 
# draw Qhipu
quipu.draw()

