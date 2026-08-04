device_status = input("enter your device status: ").lower()

if device_status == "on" :
    device_temp = int(input("enter your device temperature: "))
    if device_temp >35:
        print("device is on and temperature is high, please turn off the device")
    else:
        print("device is normal ")
else:
    print("device is offline")