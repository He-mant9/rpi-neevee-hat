import smbus
import time
class TCA8418:
    num_to_key={34:1, 24:2, 14:3, 4:'A', 33:4, 23:5, 13:6, 3:'B', 32:7, 22:8, 12:9, 2:'C', 31:'*', 21:0, 11:'#', 1:'D'}
    key_to_num={'1':34, '2':24, '3':14, 'A':4, '4':33, '5':23, '6':13, 'B':3, '7':32, '8':22, '9':12, 'C':2, '*':31, '0':21, '#':11, 'D':1}
    key_map=[0x0f,0x0f,0x00]
    
    def __init__(self,bus_number=1):
        self.bus_number=bus_number
        self.bus=smbus.SMBus(self.bus_number)
        #configuration register(0x01) setting
        #(0x95) enables the following interrupts
        #Auto Increment register enabled
        #Interrupts enabled
        #Keypad Lock Interrupt enabled
        #Key Event Interrupt enabled
        self.bus.write_byte_data(0x34, 0x01, 0x95)  
        #MAPPING KEYS
        #KP_GPIO1,KP_GPIO2,KP_GPIO3 (0x1d,0x1e,0x1f) enables the 4x4 keys (1,2,3,4,11,12,13,14,21,22,23,24,31,32,33,34)
        self.bus.write_i2c_block_data(0x34,0x1d,self.key_map)
        #SETTING UNLOCK KEY COMBINATIONS
        self.bus.write_byte_data(0x34,0x0f,0x21) #first  unlock key is 33(0x21)[key 4], UNLOCK1(0x0f) register
        self.bus.write_byte_data(0x34,0x10,0x01) #second unlock key is 1(0x01)[key D], UNLOCK2(0x10) register
        #SETTING KEYPAD LOCK TIMERS
        #KP_LCK_TIMER(0x0e)
        #unlocking should happen in totally 10 seconds
        #unlock_key_2 should be pressed within 2 seconds after pressing unlock_key_1
        self.bus.write_byte_data(0x34,0x0e,0x52)
    
    
    def setUnlockKeys(self,key1,key2):
        if((key1 in self.key_to_num.keys()) and (key2 in self.key_to_num.keys())):
            self.bus.write_byte_data(0x34,0x0f,self.key_to_num[key1])
            self.bus.write_byte_data(0x34,0x10,self.key_to_num[key2])
        else:
            print("Invalid keys..!")
    
    def setLockKeypad(self):
        #KEY LOCK AND EVENT COUNTER REGISTER(0x03)
        #To manually LOCK the keypad below code works
        var=self.bus.read_byte_data(0x34,0x03)
        bit6=var | 0x40 #setting bit6 to 1
        self.bus.write_byte_data(0x34,0x03,bit6)

    def setUnlockKeypad(self):
        #To manually unlock the keypad below code works
        var=self.bus.read_byte_data(0x34,0x03)
        bit6=var & 0x3f #setting bit6 to 0
        self.bus.write_byte_data(0x34,0x03,bit6)

    def getLockStatus(self):
        #To know the status of lock or unlock
        var=self.bus.read_byte_data(0x34,0x03)
        bit5_bit6=var & 0x30 #00110000
        if(bit5_bit6==0):
             return False #Keypad is unlocked
        else:
            return True #Keypad is Locked

    def inputKeypad(self,prompt=''):
        if(self.getLockStatus()):
            print("Keypad is locked...press the keys to unlock")
        else:
            string=''
            print("Press ctrl+C to next line")
            print(prompt,end='')
            try:
                while(True):
                    key_lck_ec=self.bus.read_byte_data(0x34,0x03)    #read key_press counter
                    key_counter=key_lck_ec & 0x0f                    #counter value is stored in [4:0] 
                    if(key_counter!=0):                              #if counter is not zero print value pressed
                        key_value=self.bus.read_byte_data(0x34,0x04) #pressed key is stored in this register(0x04),after reading this register key_press counter decrements
                        if(key_value>=1 and key_value<=34):          #only prints the key release values
                            string+=str(self.num_to_key[key_value])
                            print(self.num_to_key[key_value],end='')
            except KeyboardInterrupt:
                pass
            print()
            return string



