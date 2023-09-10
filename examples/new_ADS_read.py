import os
import time
import ADS1x15
import datetime
import pytz

# choose your sensor
# ADS = ADS1x15.ADS1013(1, 0x48)
# ADS = ADS1x15.ADS1014(1, 0x48)
# ADS = ADS1x15.ADS1015(1, 0x48)
# ADS = ADS1x15.ADS1113(1, 0x48)
# ADS = ADS1x15.ADS1114(1, 0x48)

ADS = ADS1x15.ADS1115(1, 0x48)

print(os.path.basename(__file__))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))

# set gain to 4.096V max
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

thailand_timezone = pytz.timezone('Asia/Bangkok')

while True :
    val_0 = ADS.readADC(0)
    val_1 = ADS.readADC(1)
    val_2 = ADS.readADC(2)
    
    voltage_0 = val_0*f
    voltage_1 = val_1*f
    voltage_2 = val_2*f
    
    # ดึงข้อมูลเวลาปัจจุบัน
    current_time_utc = datetime.datetime.utcnow()
    
    # แปลงเวลาปัจจุบันเป็นเวลาในโซนเวลาประเทศไทย
    current_time_thailand = current_time_utc.astimezone(thailand_timezone)
    
    # แปลงเวลาเป็นรูปแบบ "ว/ด/ปี ชั่วโมง:นาที:วินาที"
    formatted_time = current_time_thailand.strftime("%d/%m/%Y %H:%M:%S")
    
    # แสดงผลลัพธ์พร้อมข้อมูลเวลาในรูปแบบที่กำหนด
    print("Analog0: {0:d}\tVoltage0: {1:.3f} V\tAnalog1: {2:d}\tVoltage1: {3:.3f} V\tAnalog2: {4:d}\tVoltage2: {5:.3f} V\tTime (Thailand): {6}".format(val_0, voltage_0, val_1, voltage_1, val_2, voltage_2, formatted_time))
    
    time.sleep(1)
