import asyncio
from bleak import BleakScanner
from core.device import Device

class scaner_ble:
    def __init__(self ):
        self.appareils = {}
    def callback(self, device, advertisement_data):
        if device.address in self.appareils:
            objet = self.appareils[device.address]
            objet.update_rssi(advertisement_data.rssi)
        else :
            self.appareils[device.address] = Device(device.address, advertisement_data.rssi, device.name)
    async def scan(self):
        await BleakScanner(self.callback).start()
        await asyncio.sleep(10)
        return self.appareils
    async def spy(self, device):
        scanner = BleakScanner(self.callback)
        scanner.start()
        try :
            while True :
                await asyncio.sleep(0.5)
                if device.address in self.appareils:
                    print(self.appareils[device.address].rssi) 
                    print(self.appareils[device.address].get_direction())
        except KeyboardInterrupt:
            await scanner.stop()
                
                


