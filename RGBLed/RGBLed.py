import RPi.GPIO as GPIO
class RGBLed:
    def __init__(self,red=22,green=23,blue=24):
        self.red=red
        self.green=green
        self.blue=blue
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.blue, GPIO.OUT)
        
    def setRGB(self,r,g,b):
        if r == 0:
            GPIO.output(self.red, GPIO.LOW)
        else: 
            GPIO.output(self.red, GPIO.HIGH)
        if g == 0:
            GPIO.output(self.green, GPIO.LOW)
        else:
            GPIO.output(self.green, GPIO.HIGH)
        if b == 0:
            GPIO.output(self.blue, GPIO.LOW)
        else:
            GPIO.output(self.blue, GPIO.HIGH)
        #self.red=r
        #self.green=g    THESE THREE LINES ARE WRONG, AM I CORRECT SIR ?
        #self.blue=b      IT CHANGES THE PIN NUMBERS INSTEAD OF THEIR VALUES
    def getRGB(self):
        #temp=[self.red,self.green,self.blue]
        rgb = bytearray(b'\x00\x00\x00')
        rgb[0]=self.red
        rgb[1]=self.green
        rgb[2]=self.blue
        return "values of R,G,B are "+str(rgb)
#red,green,blue=int(input("Enter the pin numbers red,green and blue\n")),int(input()),int(input()
#obj1.setRGB(0,0,0)
#obj1.setRGB(red,green,blue)
#print(f"Pins of red, green and blue led's are {obj1.red},{obj1.green},{obj1.blue}")
