weight=0

EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
#hx.set_reference_unit(-113)
hx.reset()
hx.tare()
#print("Tare done! Add weight now...")

# def getWeight():
#     val = max(0, hx.get_weight(5))
#     kilo =(val/1000)
#     weight = ("{:.0f}".format(kilo))
#     return val

while True:
    print(max(0, hx.get_weight(5)))