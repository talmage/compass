newHeading = 0
heading = 0
centerX = 80
centerY = 64
radius = 62
input.calibrate_compass()
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
LCD1IN8.draw_circle(centerX,
    centerY,
    radius,
    LCD1IN8.Get_Color(LCD_COLOR.BLACK),
    DRAW_FILL.DRAW_EMPTY,
    DOT_PIXEL.DOT_PIXEL_1)
LCD1IN8.LCD_Display()

def on_in_background():
    while True:
        basic.show_number(heading)
        basic.pause(1000)
control.in_background(on_in_background)

# Check the compass heading every 1000ms.  Redraw the pointer if the heading changed.

def on_in_background2():
    global heading, newHeading
    heading = 0
    newHeading = 0
    while True:
        newHeading = input.compass_heading()
        if newHeading != heading:
            LCD1IN8.draw_line(Math.round(centerX + Math.cos(heading) * radius),
                Math.round(centerY - Math.sin(heading) * radius),
                Math.round(centerX - Math.cos(heading) * radius),
                Math.round(centerY + Math.sin(heading) * radius),
                LCD1IN8.Get_Color(LCD_COLOR.WHITE),
                DOT_PIXEL.DOT_PIXEL_1,
                LINE_STYLE.LINE_SOLID)
            LCD1IN8.draw_line(Math.round(centerX + Math.cos(newHeading) * radius),
                Math.round(centerY - Math.sin(newHeading) * radius),
                Math.round(centerX - Math.cos(newHeading) * radius),
                Math.round(centerY + Math.sin(newHeading) * radius),
                LCD1IN8.Get_Color(LCD_COLOR.RED),
                DOT_PIXEL.DOT_PIXEL_1,
                LINE_STYLE.LINE_SOLID)
            LCD1IN8.LCD_Display()
            heading = newHeading
        basic.pause(1000)
control.in_background(on_in_background2)
