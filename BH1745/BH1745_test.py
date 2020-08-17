from BH1745 import BH1745
bus_number=1
sensor=BH1745(bus_number)
sensor.setMeasurementTime(600)
print(f"ManufacturerId : {sensor.getManufacturerId()}")
print(f'Red Luminance : {sensor.getRedValue()}')
print(f'Green Luminance : {sensor.getGreenValue()}')
print(f'Blue Luminance: {sensor.getBlueValue()}')
print(f'Clear value: {sensor.getClearValue()}')
sensor.close()