import turtle
import random

WIDTH = 1024
HEIGHT = 768
def draw_rectangle(x,y,w,h,t):
    """ (int,int,int,int,turtle) ->None
    Function that takes coordinates of the bottom left coordinates and draws a rectangle
    with the width and height given
    """
    t.penup()
    t.setposition(x,y)
    t.pendown()
    
    for i in range(2):  #loop that draws the rectangle
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def wider_than_half_canvas(w):
    """(int)->None
    Function that checks if the width of current
    region is larger than half the width of canvas size
    """
    return w>(WIDTH//2)

def taller_than_half_canvas(h):
    """(int)->None
    Function that checks if the height current
    region is larger than half the height of canvas size
    """
    return h>(HEIGHT//2)

def enough_to_split_horizontally(w):
    """(int)-> int
    Function that checks whether region can be split horizontally
    based on random number
    """
    if w*1.5<120:
        return 120
    else:
        return random.randint(120,int(w*1.5))

def enough_to_split_vertically(h):
    """(int)-> int
    Function that checks whether region can be split vertically
    based on random number
    """
    if h*1.5<120:
        return 120
    else:
        return random.randint(120,int(h*1.5))

def split_into_four(w,h):
    """(int,int)->float,float
    Function that accepts width and height and
    returns horizontal and vertical split points
    """
    split_point_horizontal=random.uniform((w/3),(2*w/3))
    split_point_vertical=random.uniform((h/3),(2*h/3))
    return split_point_horizontal,split_point_vertical
    
def split_vertically(h):
    """(int)->float
    Function that accepts height and
    returns a vertical split point
    """
    
    split_point_vertical=random.uniform((h/3),(2*h/3))
    
    return split_point_vertical
    
def split_horizontally(w):
    """(int)->float
    Function that accepts width and
    returns a horizontal split point
    """
    split_point_horizontal=random.uniform((w/3),(2*w/3))
    
    return split_point_horizontal
def decide_color():
    """ (none)-> None
    Function that returns a color on based
    on a random number generated
    """
    random_value=random.random()
    if random_value<0.0833:
        return "red"
    elif random_value<0.1667:
        return "blue"
    elif random_value<0.25:
        return "yellow"
    else:
        return"white"
    
    
def mondrian(x, y, w, h, t):
    
    # your code should start here.
    # you will want to create other functions
    # for good program design.
    """(int,int,int,int,t)-> None
    Function that draws the entire mondrian art
    """
    if wider_than_half_canvas(w) and taller_than_half_canvas(h):
        
        
        split_point_horizontal,split_point_vertical=split_into_four(w,h) #if the current region is wider and taller than half the entire canvas width and height,region split horizontally and vertically
        
        #the region is split into four smaller rectangles
        draw_rectangle(x,y,x+split_point_horizontal,split_point_vertical,t)       
        draw_rectangle(x,y+split_point_vertical,split_point_horizontal,h-split_point_vertical,t)
        draw_rectangle(x+split_point_horizontal,y,w-split_point_horizontal,split_point_vertical,t)
        draw_rectangle(x+split_point_horizontal,y+split_point_vertical,w-split_point_horizontal,h-split_point_vertical,t)
        #the mondrian funcion is called recursively on each of the four regions
        mondrian(x,y,x+split_point_horizontal,split_point_vertical,t)       
        mondrian(x,y+split_point_vertical,split_point_horizontal,h-split_point_vertical,t)
        mondrian(x+split_point_horizontal,y,w-split_point_horizontal,split_point_vertical,t)
        mondrian(x+split_point_horizontal,y+split_point_vertical,w-split_point_horizontal,h-split_point_vertical,t)
        
        

        
        
    elif wider_than_half_canvas(w):   #if the current region's width is larger than the entire canvas size's width
        #the region is split in a vertical line
        split_point_horizontal=split_horizontally(w)
        
        draw_rectangle(x,y,split_point_horizontal,h,t)#rectangle is drawn to split the current region into two
        #mondrian function is called recursively on each of the two rectangles
        mondrian(x,y,split_point_horizontal,h,t)
        mondrian(x+split_point_horizontal,y,w-split_point_horizontal,h,t)

    elif taller_than_half_canvas(h):#if the current region's height is larger than the entire canvas size's height
        #the region is split in a horizontal line
        split_point_vertical=split_vertically(h)
        
        draw_rectangle(x,y,w,split_point_vertical,t)#rectangle is drawn to split the current region into two
        #mondrian function is called recursively on each of the two rectangles
        
        mondrian(x,y,w,split_point_vertical,t)
        mondrian(x,y+split_point_vertical,w,h-split_point_vertical,t)
    elif enough_to_split_horizontally(w)<w and enough_to_split_vertically(h)<h:
        
        split_point_horizontal,split_point_vertical=split_into_four(w,h)
      
        
        #the region is split into four smaller rectangles
        draw_rectangle(x,y,split_point_horizontal,split_point_vertical,t)       
        draw_rectangle(x,y+split_point_vertical,split_point_horizontal,h-split_point_vertical,t)
        draw_rectangle(x+split_point_horizontal,y,w-split_point_horizontal,split_point_vertical,t)
        draw_rectangle(x+split_point_horizontal,y+split_point_vertical,w-split_point_horizontal,h-split_point_vertical,t)
        #the mondrian funcion is called recursively on each of the four regions
        mondrian(x,y,split_point_horizontal,split_point_vertical,t)       
        mondrian(x,y+split_point_vertical,split_point_horizontal,h-split_point_vertical,t)
        mondrian(x+split_point_horizontal,y,w-split_point_horizontal,split_point_vertical,t)
        mondrian(x+split_point_horizontal,y+split_point_vertical,w-split_point_horizontal,h-split_point_vertical,t)  

    elif enough_to_split_horizontally(w)<w:#if the current region's width is larger than the entire canvas size's width
        #the region is split in a vertical line
        split_point_horizontal=split_horizontally(w)
        
        draw_rectangle(x,y,split_point_horizontal,h,t)#rectangle is drawn to split the current region into two
        #mondrian function is called recursively on each of the two rectangles
        
        mondrian(x,y,split_point_horizontal,h,t)
        mondrian(x+split_point_horizontal,y,w-split_point_horizontal,h,t)

    elif enough_to_split_vertically(h)<h:#if the current region's height is larger than the entire canvas size's height
        #the region is split in a horizontal line
        split_point_vertical=split_vertically(h)
        draw_rectangle(x,y,w,split_point_vertical,t)#rectangle is drawn to split the current region into two
        #mondrian function is called recursively on each of the two rectangles        
        mondrian(x,y,w,split_point_vertical,t)
        mondrian(x,y+split_point_vertical,w,h-split_point_vertical,t)
    else:
        #if none of the cases are met, a colored rectangle is formed
        color_filled=decide_color()
        t.fillcolor(color_filled)
        t.begin_fill()
        draw_rectangle(x,y,w,h,t)
        t.end_fill()
    return
        
        
        
        


def main():
    # Create a window with a canvas
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, WIDTH+1, HEIGHT+1)
    t = turtle.Turtle()
    t.pensize(5)
    t.speed(0)
    t.hideturtle()

    # Draw the art
    mondrian(0, 0, WIDTH, HEIGHT, t)
    wn.exitonclick()

if __name__ == '__main__':
    main()
