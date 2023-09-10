import os
import time
import ADS1x15
import datetime
import pytz
import matplotlib.pyplot as plt

ADS = ADS1x15.ADS1115(1, 0x48)


print(os.path.basename(__file__))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15.__version__))

# set gain to 4.096V max
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()
# กำหนดโซนเวลาในประเทศไทย
thailand_timezone = pytz.timezone('Asia/Bangkok')

# สร้างรายการว่างสำหรับเก็บค่า voltage และ formatted_time
voltage_0_data = []
voltage_1_data = []
voltage_2_data = []
formatted_time_data = []

while True:
    val_0 = ADS.readADC(0)
    val_1 = ADS.readADC(1)
    val_2 = ADS.readADC(2)
    
    voltage_0 = val_0 * f
    voltage_1 = val_1 * f
    voltage_2 = val_2 * f
    
    # ดึงข้อมูลเวลาปัจจุบัน
    current_time_utc = datetime.datetime.utcnow()
    
    # แปลงเวลาปัจจุบันเป็นเวลาในโซนเวลาประเทศไทย
    current_time_thailand = current_time_utc.astimezone(thailand_timezone)
    
    # แปลงเวลาเป็นรูปแบบ "ว/ด/ปี ชั่วโมง:นาที:วินาที"
    formatted_time = current_time_thailand.strftime("%d/%m/%Y %H:%M:%S")
    
    # เพิ่มค่าข้อมูลในรายการ
    voltage_0_data.append(voltage_0)
    voltage_1_data.append(voltage_1)
    voltage_2_data.append(voltage_2)
    formatted_time_data.append(formatted_time)

    # แสดงค่าข้อมูลที่เพิ่มไปในรายการแต่ละครั้ง (หรือสามารถไม่แสดงก็ได้)
    print("Analog0: {0:.3f} V\tAnalog1: {1:.3f} V\tAnalog2: {2:.3f} V\tTime (Thailand): {3}".format(voltage_0, voltage_1, voltage_2, formatted_time))
    
    # พล็อตกราฟ
    plt.clf()  # ลบกราฟเก่า
    plt.plot(formatted_time_data, voltage_0_data, label='Voltage 0')
    plt.plot(formatted_time_data, voltage_1_data, label='Voltage 1')
    plt.plot(formatted_time_data, voltage_2_data, label='Voltage 2')
    
    # ตั้งค่าแกน x และ y
    plt.xlabel('เวลา (ประเทศไทย)')
    plt.ylabel('Voltage (V)')
    
    # เพิ่มคำอธิบายในกราฟ
    plt.title('กราฟ Voltage ตามเวลา')
    
    # เพิ่มคำอธิบายเส้นกราฟ
    plt.legend()
    
    # แสดงกราฟ
    plt.pause(1)  # รอ 1 วินาทีแล้วรีเฟรชกราฟ

