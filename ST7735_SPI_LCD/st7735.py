from PIL import Image,ImageDraw,ImageFont
import numpy as np
from time import sleep
from spidev import SpiDev
import RPi.GPIO as GPIO
class ST7735:
    temphumiflag=False
    image=Image.new('RGB',(132,132),'black')
    draw=ImageDraw.Draw(image)
    pixels=image.load()
    def __init__(self,AO=35,RESET=12,CS=24,speed=1000000):
        self.spi=SpiDev()
        self.spi.open(0,0)
        self.spi.max_speed_hz=speed
        self.AO=AO
        self.RESET=RESET
        self.CS=CS
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.AO,GPIO.OUT)    #data/command pin AO
        GPIO.setup(self.RESET,GPIO.OUT) #Reset pin
        GPIO.setup(self.CS,GPIO.OUT)    #chip select pin
        GPIO.output(self.RESET,True)    #reset pin should be high always
        GPIO.output(self.CS,False)      #select the lcd
        GPIO.output(self.AO,False)      #command transfer mode activated
        self.spi.xfer([0x11])           #sleep mode off
        sleep(0.005)  
        self.spi.xfer([0x29])           #display on
        sleep(0.005)
        self.spi.xfer([0x2c])           #write data in lcd display ram
        sleep(0.005)
        GPIO.output(self.AO,True)       #data transfer mode activated

     
        
    def displayClean(self):
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                self.pixels[i,j]=(0,0,0)

    def displayPrint(self,string,x,y,color,font):
        self.draw.text((x,y),string,fill=color,font=font)
        
    def write(self):
        arr=np.array(self.image)
        arr[:,:,0],arr[:,:,2]=arr[:,:,2].copy(),arr[:,:,0].copy()
        self.spi.writebytes2(arr)

    def displayImage(self,filename):
        image=Image.open(filename)
        im=(image.resize((132,132))).convert('RGB')
        arr=self.to_bgr(im)
        self.spi.writebytes2(arr)
       
    def __del__(self):
        self.spi.close()
        self.image.close()








