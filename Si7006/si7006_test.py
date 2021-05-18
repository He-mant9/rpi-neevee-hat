from si7006 import SI7006
sensor=SI7006(1)
print(f"Humidity : {round(sensor.getHumidity(),2)}%")
print(f"Temperature : {round(sensor.getTemperature(),2)} deg.Celcius")
#sensor.setOnHeater()
sensor.setHeaterCurrent(1) # 1 value gives more heat sir....6 is the least
sensor.setOffHeater()
print(f"Heater Current : {sensor.getHeaterCurrent()} mA")
print("setting new heater current")
#valid values...1 to 6
print(f"Heater Current : {sensor.getHeaterCurrent()} mA")
print(f"ManufacturerId : {sensor.getManufacturerId()}")