from tca8418 import TCA8418
sensor=TCA8418(1)
sensor.setUnlockKeypad()
key1=sensor.inputKeypad("Enter the key 1 : ")
key2=sensor.inputKeypad("Enter the key 2 : ")
print(key1)
print(key2)
