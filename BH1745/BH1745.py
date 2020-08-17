import smbus
import time
class BH1745():
    def __init__(self,bus_number=1):
        self.bus_number=bus_number
        self.bus=smbus.SMBus(self.bus_number)
        self.bus.write_byte_data(0x38, 0x41, 0x00)  #default time set to 160msec
        self.bus.write_byte_data(0x38, 0x42, 0x10)  #0x10 instruct the sensor to measure the light and set the gain to 1X
        self.bus.write_byte_data(0x38, 0x44, 0x02)  #default value of mode_control3 register
        time.sleep(0.5)

    def setMeasurementTime(self,msec):
        if(160<=msec and msec<=240):
            self.bus.write_byte_data(0x38, 0x41, 0x00)
        if(240<msec and msec<=320):
            self.bus.write_byte_data(0x38, 0x41, 0x01)
        if(320<msec and msec<=480):
            self.bus.write_byte_data(0x38, 0x41, 0x01)
        if(480<msec and msec<=640):
            self.bus.write_byte_data(0x38, 0x41, 0x02)
        if(640<msec and msec<=960):
            self.bus.write_byte_data(0x38, 0x41, 0x02)
        if(960<msec and msec<=1280):
            self.bus.write_byte_data(0x38, 0x41, 0x03)
        if(1280<msec and msec<=1920):
            self.bus.write_byte_data(0x38, 0x41, 0x03)
        if(1920<msec and msec<=2560):
            self.bus.write_byte_data(0x38, 0x41, 0x04)
        if(2560<msec and msec<=3840):
            self.bus.write_byte_data(0x38, 0x41, 0x04)
        if(3840<msec and msec<=5120):
            self.bus.write_byte_data(0x38, 0x41, 0x05)

    def getColorValue(self):
        data = self.bus.read_i2c_block_data(0x38, 0x50, 8)
        color=[]
        color.append(data[1] * 256 + data[0])    #accessing two bytes from the first word (data[0]-->LSB) (data[1]-->MSB)
        color.append(data[3] * 256 + data[2])
        color.append(data[5] * 256 + data[4])
        color.append(data[7] * 256 + data[6])
        return color
        

    def getManufacturerId(self):
        return hex(self.bus.read_byte_data(0x38,0x92))

    def getRedValue(self):
        color=self.getColorValue()
        return color[0]

    def getGreenValue(self):
        color=self.getColorValue()
        return color[1]
    
    def getBlueValue(self):
        color=self.getColorValue()
        return color[2]

    def getClearValue(self):
        color=self.getColorValue()
        return color[3]
    
    def __del__(self):
        self.bus.close()
