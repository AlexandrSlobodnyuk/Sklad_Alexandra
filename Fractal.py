import turtle as tl

def draw_fractal(scale):
    if scale >= 8:
        draw_fractal(scale / 3.0)
        tl.left(120)
        draw_fractal(scale / 3.0)
        tl.right(120)
        draw_fractal(scale / 3.0)
        tl.right(120)
        draw_fractal(scale / 3.0)
        tl.left(120)
        draw_fractal(scale / 3.0)
        
      
    else:
        tl.forward(scale)

scale = 400
tl.penup()
tl.goto(-scale, -scale/4)
tl.pendown()
tl.speed(0)
draw_fractal(scale)
tl.done()
