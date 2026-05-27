class Device:
    def __init__(self, address, rssi, name="inconnue"):
        self.name = name
        self.address = address
        self.rssi = rssi
        self.oldrssi = rssi
    def update_rssi(self, newrssi):
        self.oldrssi = self.rssi
        self.rssi = newrssi
    def get_direction(self):
        if self.oldrssi < self.rssi:
            direction = "raprochement"
        elif self.oldrssi > self.rssi:
            direction = "eloignement"
        elif self.oldrssi == self.rssi:
            direction = "stable"
        return direction