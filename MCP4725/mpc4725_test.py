import mpc4725
dac=mpc4725.MPC4725()
dac.setVoltage(1.3)
dac.setDefaultVoltage(0)
print(dac.getVoltage())
print(dac.getDefaultVoltage())