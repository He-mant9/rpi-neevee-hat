from st7735 import ST7735
import time
from PIL import ImageFont
from tca8418 import TCA8418
from si7006 import SI7006
from mma8652 import MMA8652
lcd=ST7735()
lcd.displayClean()
font=ImageFont.truetype("digital-7.ttf",25)
small_font=ImageFont.truetype("digital-7.ttf",20)
cool='key : _'
temp=f'{round(SI7006().getTemperature(),1)} C'
humi=f'{round(SI7006().getHumidity(),1)} %'
start=time.time()
end=0
try:
    while(True):
        if(int(end-start)>=60):
            humi=f'{round(SI7006().getHumidity(),1)} %'
            temp=f'{round(SI7006().getTemperature(),1)} C'
            start=time.time()
            print('hi')
        lcd.displayPrint(temp,5,5,'red',font)
        lcd.displayPrint(humi,70,5,'blue',font)
        key=TCA8418().readKeypad()
        if(key!='255'):
            cool=f'key : {key}'
        lcd.displayPrint(cool,28,45,'white',font)
        x,y,z=MMA8652().get3DValues()  
        lcd.displayPrint(str(x),15,85,'cyan',small_font)
        lcd.displayPrint(str(y),60,85,'cyan',small_font)
        lcd.displayPrint(str(z),30,105,'cyan',small_font)
        lcd.write()
        lcd.displayClean()
        end=time.time()
except(KeyboardInterrupt):
    print('terminated')
    
