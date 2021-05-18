import smbus
import time
class SI7006():
    def __init__(self,bus_number=1):
        self.bus_number=bus_number
        self.bus=smbus.SMBus(self.bus_number)
    
    def getHumidity(self):
        self.bus.write_byte(0x40, 0xF5) #0xF5, Select Relative Humidity NO HOLD MASTER mode
        time.sleep(0.5)
        humiMSB = self.bus.read_byte(0x40)  #Read data back, 2 bytes, Humidity MSB first
        humiLSB = self.bus.read_byte(0x40)
        humidity = (125.0 * (humiMSB * 256.0 + humiLSB) / 65536.0) - 6.0
        return humidity

    def getTemperature(self):
        self.bus.write_byte(0x40, 0xF3) #0xF3, Select temperature NO HOLD MASTER mode
        time.sleep(0.5)
        tempMSB = self.bus.read_byte(0x40)  # Read data back, 2 bytes, Temperature MSB first
        tempLSB = self.bus.read_byte(0x40)
        cTemp = (175.72 * (tempMSB * 256.0 + tempLSB) / 65536.0) - 46.85
        #fTemp = cTemp * 1.8 + 32
        return cTemp

    def getHeaterCurrent(self):
        if(int(0x3a)==self.bus.read_byte_data(0x40,0xe7)):
            print("Heater is turned off")
        val=self.bus.read_byte_data(0x40,0x11)
        if(val==int(0x00)):
            return 3.09
        if(val==int(0x01)):
            return 9.18
        if(val==int(0x02)):
            return 15.24
        if(val==int(0x04)):
            return 27.39
        if(val==int(0x08)):
            return 51.69
        if(val==int(0x0f)):
            return 94.20
        
    def getManufacturerId(self):
        return hex(0x06)     #Hard coded the device ID (info from datasheet)

    def resetSensor(self):
        self.bus.write_byte_data(0x40,0xe6,0xfe) #software reset of sensor

    def setHeaterCurrent(self,val):
        if(int(0x3a)==self.bus.read_byte_data(0x40,0xe7)):
            print("Can't set current...heater is turned off")
        else:
            if(val==1):
                self.bus.write_byte_data(0x40,0x51,0x00) #3.09mA
            if(val==2):
                self.bus.write_byte_data(0x40,0x51,0x01) #9.18mA
            if(val==3):
                self.bus.write_byte_data(0x40,0x51,0x02) #15.24mA
            if(val==4):
                self.bus.write_byte_data(0x40,0x51,0x04) #27.39mA
            if(val==5):
                self.bus.write_byte_data(0x40,0x51,0x08) #51.69mA
            if(val==6):
                self.bus.write_byte_data(0x40,0x51,0x0f) #94.20mA
            

    def setOnHeater(self):
        self.bus.write_byte_data(0x40,0xe6,0x3e)
    
    def setOffHeater(self):
        self.bus.write_byte_data(0x40,0xe6,0x3a)

    def __del__(self):
        self.bus.close()

# SI7006_A20 address, 0x40(64)


#checksum1=bus.read_byte(0x40)

# Convert the data


# SI7006_A20 address, 0x40(64) 



# SI7006_A20 address, 0x40(64

# Convert the data


# Output data to screen
'''print("Relative Humidity is : %.2f %%RH" %humidity)
print("Temperature in Celsius is : %.2f C" %cTemp)
print("Temperature in Fahrenheit is : %.2f F" %fTemp)
print ("checksum1 checksum2 : %d %d" %checksum1 %checksum2)'''