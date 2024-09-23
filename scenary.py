"""This is a program that will draw a table with your desired size within set parameters,
a cake sitting on the table, the cake will have four layers each having a different random color,
the size of the cake can be inputted by the user, the cake will have a cherry and a candle on top of it."""

import turtle
import random

def draw_rectangle(turtle_obj, width, height, color):
    """Draws a filled rectangle with the inputted width and color using recursion."""
    
    def draw_side(turtle_obj, width, height, sides_left):
        """Recursively draw the sides of the rectangle."""
        if sides_left == 0:  # Base case: no more sides to draw
            return
        
        if sides_left % 2 == 0:  # Even number of sides: draw width
            turtle_obj.forward(width)
        else:  # Odd number of sides: draw height
            turtle_obj.forward(height)
        
        turtle_obj.left(90)  # Turn left after each side
        
        # Recursive call for the next side
        draw_side(turtle_obj, width, height, sides_left - 1)
    
    # Begin filling the color
    turtle_obj.fillcolor(color)
    turtle_obj.begin_fill()
    
    # Start drawing with 4 sides
    draw_side(turtle_obj, width, height, 4)
    
    # End filling
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
    
    # Returns the turtle to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

    return table_top_y  # Returns the Y-coordinate of the top of the table

def draw_cake(turtle_obj, cake_width, cake_height, table_top_y):
    """Draws a rectangular cake with multiple layers, and random color on each layer positioned on the table."""
    
    cake_bottom_y = table_top_y + 20
    layer_height = cake_height / 4
    
    def draw_layer(turtle_obj, cake_width, cake_bottom_y, layer_height, current_layer):
        """Recursively draw cake layers."""
        if current_layer == 4:  # Base case: stop after 4 layers
            return
        
        # Generate a random color for the layer
        color = (random.random(), random.random(), random.random())
        
        # Move turtle to the starting position for this layer
        turtle_obj.penup()
        turtle_obj.goto(-cake_width / 2 + current_layer * 10, cake_bottom_y + current_layer * layer_height)
        turtle_obj.pendown()
        
        # Draw the rectangular layer
        draw_rectangle(turtle_obj, cake_width - current_layer * 20, layer_height, color)
        
        # Recursive call for the next layer
        draw_layer(turtle_obj, cake_width, cake_bottom_y, layer_height, current_layer + 1)
    
    # Start drawing from the first layer (layer 0)
    draw_layer(turtle_obj, cake_width, cake_bottom_y, layer_height, 0)

    # Returns the turtle to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

    return cake_width, cake_height, cake_bottom_y + cake_height - layer_height  # Returns the Y-coordinate of the top layer of the cake

def draw_candle(turtle_obj, cake_width, cake_height, top_layer_y):
    """Draws a 2D candle on top of the cake's top layer, centered horizontally on the cake surface."""
    
    candle_width = cake_width / 10
    candle_height = cake_height / 4
    # Centers the candle on top of the cake's top layer
    candle_x = -candle_width / 2  
    candle_y = top_layer_y + 20

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
    
    # Returns the turtle to original orientation
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(0)

def draw_cherry(turtle_obj, top_layer_y):
    """Draws a cherry next to the candle on top of the cake's top layer."""
    
    cherry_x = 25
    cherry_y = top_layer_y + 20
    
    turtle_obj.penup()
    turtle_obj.goto(cherry_x, cherry_y)
    turtle_obj.pendown()
    
    turtle_obj.fillcolor("red")
    turtle_obj.begin_fill()
    turtle_obj.circle(8)
    turtle_obj.end_fill()
    
    # Returns the turtle to original orientation
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

    # Separate turtle for writing text
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()

    table_length = int(screen.textinput("Table Length", "Please enter the length of one side of a table (between 10-100):"))
    table_color = screen.textinput("Table Color", "Please enter the color of the table:")
    cake_size = int(screen.textinput("Cake Size", "Please enter the size of the cake (between 40-100):"))

    if 10 <= table_length <= 100 and 40 <= cake_size <= 100 and cake_size <= table_length:
        text_turtle.goto(0, -250)
        text_turtle.write("Drawing in process, please wait!", align="center", font=("Arial", 16, "normal"))
    else:
        text_turtle.goto(0, -250)
        text_turtle.write("Invalid input. Please enter table length and cake size within the allowed range.", align="center", font=("Arial", 16, "normal"))
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

    text_turtle.clear()
    text_turtle.write("Done! Here is your cake! Happy Birthday!", align="center", font=("Arial", 16, "normal"))

    screen.mainloop()  # Keeps the canvas open

if __name__ == "__main__":
    main()






