enums = ["Other",
         "BeveragesTrailer",
         "BoatTrailer",
         "Box",
         "CarCarrier",
         "CattleTruck",
         "Chassis",
         "ConstructionTrailer",
         "FoodTankTrailer",
         "FurnitureLift",
         "GlassTransportSuperstructure",
         "HydraulicWorkPlatform",
         "LongMaterialTransporter",
         "LowLoader",
         "MotorcycleTrailer",
         "Platform",
         "RefrigeratorBody",
         "RollOffTrailer",
         "Silo",
         "StakeBody",
         "StakeBodyAndTarpaulin",
         "SwapChassis",
         "SwapStakeBody",
         "TankBody",
         "ThreeSidedTipper",
         "TimberCarrier",
         "TrafficConstruction",
         "Trailer",
         "WalkingFloor"]
enum_name = "TrailerCategory"
values = ["Other trailers",
          "Beverages trailer",
          "Boat Trailer",
          "Box",
          "Car carrier",
          "Cattle truck",
          "Construction Trailer",
          "Chassis",
          "Food tank trailer",
          "Furniture lift",
          "Glass transport superstructure",
          "Hydraulic work platform",
          "Long material transporter",
          "Low loader",
          "Motorcycle Trailer",
          "Platform",
          "Refrigerator body",
          "Roll-off trailer",
          "Silo",
          "Stake body",
          "Stake body and tarpaulin",
          "Swap chassis",
          "Swap Stake body",
          "Tank body",
          "Timber carrier",
          "Three-sided tipper",
          "Traffic construction",
          "Trailer",
          "Walking floor"]


def create_cases():
    rs = ""
    for e, v in zip(enums, values):
        rs += '''                case {enum_name}.{enum}:
                    return "{value}"; \n'''.format(enum_name=enum_name, enum=e, value=v)
    print(rs)


create_cases()
