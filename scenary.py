import turtle
import random

def draw_rectangle(turtle_obj, width, height, color):
    """Draws a filled rectangle with the given width, height, and color."""
    turtle_obj.fillcolor(color)
    turtle_obj.begin_fill()
    for _ in range(2):
        turtle_obj.forward(width)
        turtle_obj.left(90)
        turtle_obj.forward(height)
        turtle_obj.left(90)
    turtle_obj.end_fill()

def draw_table(turtle_obj, length, height, color):
    """Draws a rectangular table with four legs."""
    
    turtle_obj.penup()
    table_top_y = 0  # Top of the table Y-coordinate
    turtle_obj.goto(-length / 2, table_top_y)  # Centering the position
    turtle_obj.pendown()

    draw_rectangle(turtle_obj, length, height / 6, color)

    leg_width = length / 20
    leg_height = height

    # First leg (bottom left)
    turtle_obj.penup()
    turtle_obj.goto(-length / 2, table_top_y - leg_height)  
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, leg_width, leg_height, color)

    # Second leg
    turtle_obj.penup()
    turtle_obj.goto(-length / 2 + 50, table_top_y - leg_height)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, leg_width, leg_height, color)
    
    # Third leg
    turtle_obj.penup()
    turtle_obj.goto(length / 2 - 70, table_top_y - leg_height)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, leg_width, leg_height, color)
    
    # Fourth leg (bottom right)
    turtle_obj.penup()
    turtle_obj.goto(length / 2 - leg_width, table_top_y - leg_height)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, leg_width, leg_height, color)
    
    # Return to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

    return table_top_y  # Returns the Y-coordinate of the top of the table

def draw_cake(turtle_obj, cake_width, cake_height, table_top_y):
    """Draws a rectangular cake with multiple layers and random color for each layer, positioned on the table."""
    
    cake_bottom_y = table_top_y + 20
    layer_height = cake_height / 4
    
    # First layer
    color1 = (random.random(), random.random(), random.random())
    turtle_obj.penup()
    turtle_obj.goto(-cake_width / 2, cake_bottom_y)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, cake_width, layer_height, color1)

    # Second layer
    color2 = (random.random(), random.random(), random.random())
    turtle_obj.penup()
    turtle_obj.goto(-cake_width / 2 + 10, cake_bottom_y + layer_height)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, cake_width - 20, layer_height, color2)

    # Third layer
    color3 = (random.random(), random.random(), random.random())
    turtle_obj.penup()
    turtle_obj.goto(-cake_width / 2 + 20, cake_bottom_y + 2 * layer_height)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, cake_width - 40, layer_height, color3)

    # Fourth layer
    color4 = (random.random(), random.random(), random.random())
    turtle_obj.penup()
    turtle_obj.goto(-cake_width / 2 + 30, cake_bottom_y + 3 * layer_height)
    turtle_obj.pendown()
    draw_rectangle(turtle_obj, cake_width - 60, layer_height, color4)
    
    # Return to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

    return cake_width, cake_height, cake_bottom_y + cake_height - layer_height  # Returns the Y-coordinate of the top layer of the cake

def draw_candle(turtle_obj, cake_width, cake_height, top_layer_y):
    """Draws a 2D candle on top of the cake's top layer, centered horizontally on the cake surface."""
    
    candle_width = cake_width / 10
    candle_height = cake_height / 4
    candle_x = -candle_width / 2  
    candle_y = top_layer_y + 30

    turtle_obj.penup()
    turtle_obj.goto(candle_x, candle_y)
    turtle_obj.pendown()

    draw_rectangle(turtle_obj, candle_width, candle_height, "white")

    turtle_obj.penup()
    turtle_obj.goto(0, candle_y + candle_height)  # Centers the flame on the candle
    turtle_obj.pendown()
    turtle_obj.fillcolor("orange")
    turtle_obj.begin_fill()
    turtle_obj.circle(7)
    turtle_obj.end_fill()

    # Return to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

def draw_cherry(turtle_obj, top_layer_y):
    """Draws a cherry next to the candle on top of the cake's top layer."""
    
    cherry_x = 25
    cherry_y = top_layer_y + 25
    
    turtle_obj.penup()
    turtle_obj.goto(cherry_x, cherry_y)
    turtle_obj.pendown()
    
    turtle_obj.fillcolor("red")
    turtle_obj.begin_fill()
    turtle_obj.circle(8)
    turtle_obj.end_fill()
    
    # Return to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

def main():
    screen = turtle.Screen()
    screen.title("Birthday Cake Drawing")
    screen.setup(width=600, height=600)
    screen.bgcolor("skyblue")

    cake_turtle = turtle.Turtle()
    cake_turtle.speed(3)

    # Get inputs from the user via the terminal
    table_length = int(input("Please enter the length of the table (between 10-100): "))
    table_color = input("Please enter the color of the table: ")
    cake_size = int(input("Please enter the size of the cake (between 10-100): "))

    # Validate inputs
    if not (10 <= table_length <= 100 and 10 <= cake_size <= 100 and cake_size <= table_length):
        print("Invalid input. Please ensure that table length and cake size are within the allowed range.")
        turtle.done()
        return

    # Draw the table and retrieve the Y-coordinate of the top of the table
    table_top_y = draw_table(cake_turtle, table_length * 4, 150, table_color)

    # Draw the cake on top of the table and retrieve the Y-coordinate of the top layer of the cake
    cake_width, cake_height, top_layer_y = draw_cake(cake_turtle, cake_size * 3, cake_size * 2, table_top_y)

    # Draw the candle on the surface of the top layer
    draw_candle(cake_turtle, cake_width, cake_height, top_layer_y)

    # Draw a cherry next to the candle on the surface of the top layer
    draw_cherry(cake_turtle, top_layer_y)

    screen.mainloop()  # Keeps the canvas open

if __name__ == "__main__":
    main()






