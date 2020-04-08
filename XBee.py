from digi.xbee.devices import XBeeDevice
device = XBeeDevice("COM5", 9600)
device.open()
device.send_data_broadcast("Hello XBee World!")
device.close()