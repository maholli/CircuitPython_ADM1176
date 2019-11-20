import time, board, busio
import adm1176
 
i2c = busio.I2C(board.SCL, board.SDA) 
adm = adm1176.ADM1176(i2c)

while True:
    print(adm.read())
    time.sleep(1)