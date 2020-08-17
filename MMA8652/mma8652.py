import smbus
import time

class MMA8652():
    def __init__(self,bus_number=1):
        self.bus_number=bus_number
        self.bus=smbus.SMBus(self.bus_number)
        self.bus.write_byte_data(0x1d, 0x2A, 0x00)  #Select Control register 0x2A , 0x00 Standby Mode
        self.bus.write_byte_data(0x1d, 0x2A, 0x01)  #Select Control register 0x2A , 0x01 Active mode
        self.bus.write_byte_data(0x1d, 0x0E, 0x00)  #Select Configuration register 0x0E , 0x00 Set range to +/- 2g
        time.sleep(0.5)
    
    def setStandbyMode(self):
        self.bus.write_byte_data(0x1d, 0x2A, 0x00)
    
    def setActiveMode(self):
        self.bus.write_byte_data(0x1d, 0x2A, 0x01)
    
    def ResetSensor(self):
        self.bus.write_byte_data(0x1d,0x2b,0x40) #software reset of sensor (all set to defaults)
    
    def getManufacturerId(self):
        return hex(self.bus.read_byte_data(0x1d,0x0d))

    def get3DValues(self):
        data=self.bus.read_i2c_block_data(0x1d, 0x00, 7)
        axis=[]                                       #axis[0]=x-axis , axis[1]=y-axis , axis[2]=z-axis
        axis.append((data[1] * 256 + data[2]) / 16)
        axis.append((data[3] * 256 + data[4]) / 16)
        axis.append((data[5] * 256 + data[6]) / 16)
        if axis[0] > 2047:
            axis[0] -= 4096
        if axis[1] > 2047:
            axis[1] -= 4096
        if axis[2] > 2047:
            axis[2] -= 4096
        return axis

    def getXValue(self):
        xaxis=self.get3DValues()
        return xaxis[0]

    def getYValue(self):
        yaxis=self.get3DValues()
        return yaxis[1]

    def getZValue(self):
        zaxis=self.get3DValues()
        return zaxis[2]

    def __del__(self):
        self.bus.close()