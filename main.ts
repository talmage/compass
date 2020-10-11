let newHeading = 0
let heading = 0
let centerX = 80
let centerY = 64
let radius = 62
input.calibrateCompass()
LCD1IN8.LCD_Init()
LCD1IN8.LCD_Clear()
LCD1IN8.LCD_SetBL(123)
LCD1IN8.DrawCircle(centerX, centerY, radius, LCD1IN8.Get_Color(LCD_COLOR.BLACK), DRAW_FILL.DRAW_EMPTY, DOT_PIXEL.DOT_PIXEL_1)
LCD1IN8.LCD_Display()
//  Check the compass heading every 1000ms.  Redraw the pointer if the heading changed.
//  
control.inBackground(function on_in_background() {
    
    heading = 0
    newHeading = 0
    while (true) {
        newHeading = input.compassHeading()
        if (newHeading != heading) {
            LCD1IN8.DrawLine(Math.round(centerX + Math.cos(heading) * radius), Math.round(centerY - Math.sin(heading) * radius), Math.round(centerX - Math.cos(heading) * radius), Math.round(centerY + Math.sin(heading) * radius), LCD1IN8.Get_Color(LCD_COLOR.WHITE), DOT_PIXEL.DOT_PIXEL_1, LINE_STYLE.LINE_SOLID)
            LCD1IN8.DrawLine(Math.round(centerX + Math.cos(newHeading) * radius), Math.round(centerY - Math.sin(newHeading) * radius), Math.round(centerX - Math.cos(newHeading) * radius), Math.round(centerY + Math.sin(newHeading) * radius), LCD1IN8.Get_Color(LCD_COLOR.RED), DOT_PIXEL.DOT_PIXEL_1, LINE_STYLE.LINE_SOLID)
            LCD1IN8.LCD_Display()
            basic.showNumber(newHeading)
            heading = newHeading
        }
        
        basic.pause(1000)
    }
})
