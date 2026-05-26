import asyncio
from bleak import BleakScanner
from state import appareils
def main():
    
    choice = input("what xould you like to launch \n [1] : scan \n [2] : spy a device \n")
    if choice == "1":
        asyncio.run(scan())
    elif choice == "2":
        asyncio.run(spy(input("adress mac of the target")))

async def scan():
    async with BleakScanner(detection_callback=callback):
        await asyncio.sleep(10)
def callback(device, advertisement_data):
    print(device.name, device.address)
    appareils[device.address] = {"nom": device.name, "rssi": advertisement_data.rssi}

async def spy(target):
    print("start spying")
    def change(device, advertissement_data):
        if device.address.lower() == target.lower():
            print(f"name : {device.name}\n rssi : {advertissement_data.rssi}")
    scan = BleakScanner(change)
    await scan.start()
    await asyncio.sleep(30000) 

main()