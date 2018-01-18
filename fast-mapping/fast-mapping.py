from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


ui = [


    "Category",
    "First Registration",
    "Construction Year",
    "Fuel",
    "Gearbox",
    "Operating Hours",
    "Installation Height",
    "Lifting Height",
    "Lifting Capacity (in kg)",
    "Cabin",
    "Power Assisted Steering",
    "Protection roof",
    "Renting Possible",
    "Trailer coupling",


]

api = [
    "ID String",
    "Title String",
    "MainPrice Number",
    "AlternativePrice Number",
    "Status String",

    "Address String",
    "FirstRegistration string",
    "Category String",
    "SubCategory String",
    "Mileage Interger",
    "Power Interger",
    "GearBox String",
    "Fuel String",
    "OtherDescription String",
    "ImageLink String",
    "IsFavorite bool",
    "RelativeURL String",
    "Type String",
    "SubType string",
    "Color string",
    "VehicleInspectionValidUntil String",
    "ApprovedUserProgramme string",
    "NumberOfVehicleOwner int",
    "CubicCapacity float",

    "ConstructionYear int",
    "OperatingHours int",
    "InstallationHeight int",
    "LiftingHeight int",
    "LiftingCapacityHeight int",
    "Climatisation string",

    "Cabin bool",
    "PowerAssistSteering bool",
    "RentingPossible bool",
    "TrailerCoupling bool",
    "ProtectionRoof bool",
]
m = [(i.split(" ")[0], i.split(" ")[1]) for i in api]
rs = []

for i in ui:
    mx = similar(i, m[0][0])
    mi = 0
    for j in range(1, len(m)):
        if similar(i, m[j][0]) > mx:
            mx = similar(i, m[j][0])
            mi = j
    rs.append((i, m[mi][0], m[mi][1]))

for r in rs:
    print("{name}\t{type}".format(
        name=r[1], type=r[2], display=r[0]))
