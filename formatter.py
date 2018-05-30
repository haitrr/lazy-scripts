import re


def format(code):
    f = open("formatted.cs", "w")
    level = 0
    linesBf = code.split("\n")
    lines = []
    for line in linesBf:
        if line == "":
            continue
        if line[-1] == "{":
            lines.append(line[:-1])
            lines.append("{")
        else:
            lines.append(line)
    rs = []
    for line in lines:
        if line == "":
            continue
        if line[0] == "}":
            level -= 1

        rs.append(level * "\t" + line)
        if line[0] == "{":
            level += 1
            print(level)
    for i in rs:
        print(i)
        f.write(i + "\n")
    f.close()


code = '''
using Index.Domain.Core.Models;
using Index.Domain.Dynamic.Interfaces;
using Index.Domain.Dynamic.Models;
using Index.Infrastructure.Data.Dynamic.Interfaces;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Index.Infrastructure.Data.Dynamic.Ultilities
{
public class DatabaseInitializer : IDatabaseInitializer
{
private readonly IAdRepository _adRepository;
private readonly ICategoryRepository _categoryRepository;
private readonly IModuleRepository _moduleRepository;

public DatabaseInitializer(IAdRepository adRepository, IModuleRepository moduleRepository,
ICategoryRepository categoryRepository)
{
_adRepository = adRepository;
_moduleRepository = moduleRepository;
_categoryRepository = categoryRepository;
}

public async Task SeedDatabase()
{
var vehicle = new Module
{
Id = Guid.NewGuid(),
Name = "vehicle"
};

var car = new Category
{
Name = "car",
Id = Guid.NewGuid(),
Module = vehicle.Name,
PropertyConfigs = new List<PropertyConfig> {
new TextPropertyConfig {
Name = "OtherDescription"
},
new NumberPropertyConfig {
Name = "Mileage"
},
new NumberPropertyConfig {
Name = "CubicCapacity"
},
new NumberPropertyConfig {
Name = "Power"
},
new EnumPropertyConfig {
Name = "Fuel",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Gas"
}
}
},
new EnumPropertyOption {
Value = 2,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Diezel"
}
}
}
}
},
new NumberPropertyConfig {
Name = "FuelConsumptionComb"
},
new NumberPropertyConfig {
Name = "FuelConsumptionUrban"
},
new NumberPropertyConfig {
Name = "FuelConsumptionExtraUrban"
},
new NumberPropertyConfig {
Name = "Co2EmissionsComb"
},
new NumberPropertyConfig {
Name = "NumberOfSeats"
},
new NumberPropertyConfig {
Name = "NumberOfDoors"
},
new EnumPropertyConfig {
Name = "Gearbox",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Automatic"
}
}
},
new EnumPropertyOption {
Value = 2,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Manual"
}
}
}
}
},
new EnumPropertyConfig {
Name = "EmissionClass",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Euro I"
}
}
},
new EnumPropertyOption {
Value = 2,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Euro 2"
}
}
}
}
},
new EnumPropertyConfig {
Name = "EmissionSticker",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "1 (Blue)"
}
}
},
new EnumPropertyOption {
Value = 2,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "2 (Yellow)"
}
}
}
}
},
new NumberPropertyConfig {
Name = "NumberOfOwners"
},
new EnumPropertyConfig {
Name = "AirConditioning",
Options = new [] {
new EnumPropertyOption {
Value = 1
}
}
},
new EnumArrayPropertyConfig {
Name = "PackingSensors",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Value = "Back",
Locale = "en"
}
}
},
new EnumPropertyOption {
Value = 2,
DisplayNames = new List<MultiLingualObject> {
new MultiLingualObject {
Value = "Front",
Locale = "en"
}
}
}
}
},
new BooleanPropertyConfig {
Name = "Airbag"
},
new DateTimePropertyConfig {
Name = "FirstRegistration"
},
new EnumPropertyConfig {
Name = "Color",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1
},
new EnumPropertyOption {
Value = 2
}
}
},
new EnumPropertyConfig {
Name = "InteriorDesign",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1
},
new EnumPropertyOption {
Value = 2
}
}
},
new DateTimePropertyConfig {
Name = "VehicleInspectionValidUntil"
},
new BooleanPropertyConfig {
Name = "AuxiliaryHeating"
},
new BooleanPropertyConfig {
Name = "Bluetooth"
},
new BooleanPropertyConfig {
Name = "CdPlayer"
},
new BooleanPropertyConfig {
Name = "CruiseControl"
},
new BooleanPropertyConfig {
Name = "ElectricHeatedSeats"
},
new BooleanPropertyConfig {
Name = "ElectricSeatAdjustment"
}
},
AdvancedSearchConfig = new AdvancedSearchConfig
{
Groups = new List<CriteriaGroup> {
new CriteriaGroup {
Name = "condition",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new ConditionCriteriaConfig {
Key = "IsNew",
Condition = new OrCriteria {
Elements = new List<SearchCriteria> {
new TimeBaseOnNowGreaterCriteria {
Value = new TimeBaseOnNow {
TimeSpan = TimeSpan.FromDays (-180)
},
PropertyName = "FirstRegistration"
},
new NumberLessCriteria {
PropertyName = "Mileage",
Value = 6000
}
}
}
},
new HasPictureCriteriaConfig {
Key = "HasPicture"
},
new NumberRangeCriteriaConfig {
FromKey = "MileageFrom",
ToKey = "MileageTo",
PropertyName = "Mileage"
}
}
},
new CriteriaGroup {
Name = "make-model-version",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new MakeContainCriteriaConfig {
PropertyName = "MakeId",
Key = "MakeIds"
},
new ModelContainCriteriaConfig {
PropertyName = "ModelId",
Key = "ModelIds"
}
}
},
new CriteriaGroup {
Name = "vehicle-type",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new EnumContainCriteriaConfig {
PropertyName = "Category",
Key = "Category"
},
new NumberRangeCriteriaConfig {
PropertyName = "NumberOfSeats",
FromKey = "NumberOfSeatsFrom",
ToKey = "NumberOfSeatsTo"
},
new ConditionSelectionConfig {
Conditions = new List<Condition> {
new Condition {
Code = "2",
Criteria = new NumberEqualCriteria {
Expect = 2,
PropertyName = "NumberOfDoors"
}
},
new Condition {
Code = "3",
Criteria = new NumberEqualCriteria {
Expect = 3,
PropertyName = "NumberOfDoors"
}
},
new Condition {
Code = "4",
Criteria = new NumberEqualCriteria {
Expect = 4,
PropertyName = "NumberOfDoors"
}
},
new Condition {
Code = "MoreThan4",
Criteria = new NumberGreaterCriteria {
Value = 5,
PropertyName = "NumberOfDoors"
}
}
},
Key = "NumberOfDoors"
}
}
},
new CriteriaGroup {
Name = "engine",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new EnumContainCriteriaConfig {
Key = "Fuels",
PropertyName = "Fuel"
},
new EnumContainCriteriaConfig {
Key = "Gearboxs",
PropertyName = "Gearbox"
},
new NumberRangeCriteriaConfig {
ToKey = "CubicCapacityTo",
FromKey = "CubicCapacityFrom",
PropertyName = "CubicCapacity"
}
}
},
new CriteriaGroup {
Name = "exterior-color",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new EnumContainCriteriaConfig {
PropertyName = "Color",
Key = "Colors"
}
}
},
new CriteriaGroup {
Name = "futures",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new BooleanEqualCriteriaConfig {
PropertyName = "AirConditioning",
Key = "AirConditioning"
},
new BooleanEqualCriteriaConfig {
PropertyName = "Security",
Key = "Security"
},
new BooleanEqualCriteriaConfig {
PropertyName = "Airbags",
Key = "Airbags"
}
}
},
new CriteriaGroup {
Name = "offer-details",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new ConditionSelectionConfig {
Key = "OnlineSince",
Conditions = new List<Condition> {
new Condition {
Code = "1",
Criteria = new OnlineSinceCriteria {
TimeBaseOnNow = new TimeBaseOnNow {
TimeSpan = TimeSpan.FromDays (-1)
}
}
},
new Condition {
Code = "3",
Criteria = new OnlineSinceCriteria {
TimeBaseOnNow = new TimeBaseOnNow {
TimeSpan = TimeSpan.FromDays (-3)
}
}
},
new Condition {
Code = "7",
Criteria = new OnlineSinceCriteria {
TimeBaseOnNow = new TimeBaseOnNow {
TimeSpan = TimeSpan.FromDays (-7)
}
}
},
new Condition {
Code = "14",
Criteria = new OnlineSinceCriteria {
TimeBaseOnNow = new TimeBaseOnNow {
TimeSpan = TimeSpan.FromDays (-14)
}
}
}
}
},
new HasPictureCriteriaConfig {
Key = "WithPicture"
}
}
},
new CriteriaGroup {
Name = "environment",
CriteriaConfigs = new List<SearchCriteriaConfig> {
new ConditionSelectionConfig {
Key = "FuelCombinedUpTo",
Conditions = new List<Condition> {
new Condition {
Code = "3",
Criteria = new NumberLessCriteria {
PropertyName = "FuelCombined",
Value = 3
}
},
new Condition {
Code = "5",
Criteria = new NumberLessCriteria {
PropertyName = "FuelCombined",
Value = 5
}
},
new Condition {
Code = "10",
Criteria = new NumberLessCriteria {
PropertyName = "FuelCombined",
Value = 10
}
}
}
},
new ConditionSelectionConfig {
Key = "EmissionClassFrom",
Conditions = new List<Condition> {
new Condition {
Code = "Euro1",
Criteria = new EnumLessCriteria {
Value = 1
}
},
new Condition {
Code = "Euro2",
Criteria = new EnumLessCriteria {
Value = 2
}
},
new Condition {
Code = "Euro3",
Criteria = new EnumLessCriteria {
Value = 3
}
},
new Condition {
Code = "Euro4",
Criteria = new EnumLessCriteria {
Value = 4
}
}
}
},
new ConditionSelectionConfig {
Key = "EmissionStickerFrom",
Conditions = new List<Condition> {
new Condition {
Code = "None",
Criteria = new EnumLessCriteria {
Value = 1
}
},
new Condition {
Code = "Red",
Criteria = new EnumLessCriteria {
Value = 2
}
},
new Condition {
Code = "Yellow",
Criteria = new EnumLessCriteria {
Value = 3
}
},
new Condition {
Code = "Green",
Criteria = new EnumLessCriteria {
Value = 4
}
}
}
}
}
}
}
}
};
await _moduleRepository.Add(vehicle);
await _categoryRepository.Add(car);

var realEstate = new Module
{
Name = "real-estate",
DisplayName = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Real Estate"
}
},
CreatedAt = DateTime.Now,
Id = Guid.NewGuid(),
ImageURL = "https://iascurrent.com/wp-content/uploads/2017/05/Real-Estate-Finance-1.jpg",
IsDeleted = false
};

var houses = new Category
{
Name = "houses",
DisplayName = new List<MultiLingualObject> {
new MultiLingualObject {
Locale = "en",
Value = "Houses"
}
},
CreatedAt = DateTime.Now,
ImageUrl = "https://wp.zillowstatic.com/realestate/2/RE_Guides_Foreclosure-f157b1-434d94-af815b-510x337.jpg",
Id = Guid.NewGuid(),
IsDeleted = false,
Module = realEstate.Name,
SubCategories = new List<SubCategory>(),
PropertyConfigs = new List<PropertyConfig> {
new EnumPropertyConfig {
Name = "Location",
IsRequired = true,
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1
},
new EnumPropertyOption {
Value = 2
},

new EnumPropertyOption {
Value = 3
},

new EnumPropertyOption {
Value = 4
},

new EnumPropertyOption {
Value = 5
},

new EnumPropertyOption {
Value = 6
},

new EnumPropertyOption {
Value = 7
},

new EnumPropertyOption {
Value = 8
},

new EnumPropertyOption {
Value = 9
},

new EnumPropertyOption {
Value = 10
},

new EnumPropertyOption {
Value = 11
},

new EnumPropertyOption {
Value = 12
},

new EnumPropertyOption {
Value = 13
},

new EnumPropertyOption {
Value = 14
},

new EnumPropertyOption {
Value = 15
},

new EnumPropertyOption {
Value = 16
},

new EnumPropertyOption {
Value = 17
},

new EnumPropertyOption {
Value = 18
},

new EnumPropertyOption {
Value = 19
},

new EnumPropertyOption {
Value = 20
},

new EnumPropertyOption {
Value = 21
}
}
},
new EnumPropertyConfig {
Name = "HomeType",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1
},
new EnumPropertyOption {
Value = 2
},

new EnumPropertyOption {
Value = 3
},

new EnumPropertyOption {
Value = 4
},

new EnumPropertyOption {
Value = 5
},

new EnumPropertyOption {
Value = 6
},

new EnumPropertyOption {
Value = 7
},

new EnumPropertyOption {
Value = 8
},

new EnumPropertyOption {
Value = 9
}
}
},
new NumberPropertyConfig {
Name = "Bed"
},
new NumberPropertyConfig {
Name = "FullBaths"
},
new NumberPropertyConfig {
Name = "3qBaths"
},

new NumberPropertyConfig {
Name = "1qBaths"
},

new NumberPropertyConfig {
Name = "FinishedArea"
},

new NumberPropertyConfig {
Name = "LotSize"
},

new NumberPropertyConfig {
Name = "YearBuilt"
},

new NumberPropertyConfig {
Name = "StructuralRemodelYear"
},

new NumberPropertyConfig {
Name = "BasementArea"
},
new NumberPropertyConfig {
Name = "GarageArea"
},
new TextPropertyConfig {
Name = "DescribeYourHome"
},
new BooleanPropertyConfig {
Name = "Dishwasher"
},
new BooleanPropertyConfig {
Name = "Dryer"
},
new BooleanPropertyConfig {
Name = "Freezer"
},
new BooleanPropertyConfig {
Name = "GarbageDisposal"
},
new BooleanPropertyConfig {
Name = "Microwave"
},
new BooleanPropertyConfig {
Name = "RangeOven"
},
new BooleanPropertyConfig {
Name = "Refrigerator"
},
new BooleanPropertyConfig {
Name = "TrashCompactor"
},
new BooleanPropertyConfig {
Name = "Washer"
},
new EnumPropertyConfig {
Name = "Basement",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1
},
new EnumPropertyOption {
Value = 2
},

new EnumPropertyOption {
Value = 3
},

new EnumPropertyOption {
Value = 4
}
}
},
new EnumArrayPropertyConfig {
Name = "FloorCovering",
Options = new List<EnumPropertyOption> {
new EnumPropertyOption {
Value = 1
},
new EnumPropertyOption {
Value = 2
},

new EnumPropertyOption {
Value = 3
},

new EnumPropertyOption {
Value = 4
},

new EnumPropertyOption {
Value = 5
},

new EnumPropertyOption {
Value = 6
},

new EnumPropertyOption {
Value = 7
},

new EnumPropertyOption {
Value = 8
},

new EnumPropertyOption {
Value = 9
}
}
},
new EnumPropertyConfig { }
},
};
}
}
}
'''
format(code)
