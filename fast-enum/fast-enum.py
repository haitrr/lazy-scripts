# Faster create enums 
# Work for c#
import re
# The options
options = [
    "Other Vans/Trucks up to 7.5t", "Ambulance", "Beverages van", "Box",
    "Box-type delivery van", "Box-type delivery van – high",
    "Box-type delivery van - high and long", "Box-type delivery van - long",
    "Breakdown truck Car", "Car carrier", "Cattle truck", "Chassis",
    "Dumper truck", "Estate - minibus up to 9 seats",
    "Glass transport superstructure", "Hydraulic work platform",
    "Refrigerator body", "Refrigerator Box", "Refuse truck", "Roll-off tipper",
    "Security van", "Stake body", "Stake body and tarpaulin", "Swap chassis",
    "Sweeping machine", "Tank body", "Three-sided Tipper", "Tipper",
    "Traffic construction", "Truck-mounted crane",
    "Vacuum and pressure vehicle"
]

enums = []
t = 0
for o in options:
    i = 0
    name = ""
    prev = False
    while i < len(o):
        if re.match(r"[a-zA-Z0-9]", o[i]):
            if prev:
                name += o[i].upper()
                prev = False
            else:
                name += o[i]
        else:
            prev = True
        i += 1
    enums.append((name, t))
    t += 1

for i in enums:
    print(i[0] + " = " + str(i[1]) + ",")
