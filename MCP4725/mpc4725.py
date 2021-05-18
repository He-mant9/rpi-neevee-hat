import smbus
import time
class MPC4725():
    def __init__(self,bus_number=1):
        self.bus_number=bus_number
        self.bus=smbus.SMBus(self.bus_number)
        
    def setDefaultVoltage(self,volt):
        assert (round(volt,3)*1000)<3255,"Voltage can't be higher than 3.255v"
        value=(volt*4096.0)/3.3
        value=int(round(value,0))
        var1=value & 0xff0
        var2=value & 0x00f
        var1=var1>>4
        var2=var2<<4
        self.bus.write_i2c_block_data(0x64,0x60,[var1,var2])
        time.sleep(0.3)
        
    def setVoltage(self,volt):
        assert (round(volt,3)*1000)<3255,"Voltage can't be higher than 3.255v"
        value=(volt*4096.0)/3.3
        value=int(round(value,0))
        var1=value & 0xf00
        var2=value & 0x0ff
        var1=value>>8
        self.bus.write_byte_data(0x64,var1,var2)
        
    def getVoltage(self):
        a=self.bus.read_i2c_block_data(0x64,0x00,5)
        msb=a[1]<<4
        lsb=a[2]>>4
        value=msb+lsb
        volt=(value*3.3)/4096.0
        return round(volt,4)
    
    def getDefaultVoltage(self):
        a=self.bus.read_i2c_block_data(0x64,0x00,5)
        msb=a[3]<<8
        lsb=a[4]
        value=msb+lsb
        volt=(value*3.3)/4096.0
        return round(volt,4)
