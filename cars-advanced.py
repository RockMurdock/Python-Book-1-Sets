makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)


models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)

# You must first build a new dictionary that follows the format below.

# Each key in the dictionary should be the name of a make, and its value will be a dictionary.

# The keys in the make dictionary will be the models, and the value will be a list of colors in which that the model is available.
"""
{
    'Toyota': {
      'Prius': ['Charcoal', 'Brick', 'Ivory'],
      'Camry': ['Black', 'Red', 'White']
    },
    'Nissan': {
      'Sentra': ['Charcoal', 'Blue', 'Ivory'],
      'Altima': ['Black', 'Charcoal', 'White'],
      'Xterra': ['Charcoal', 'Navy', 'Ivory']
    },
    'Mini': {
      'Countryman': ['Charcoal', 'Navy', 'White'],
      'Cooper': ['Red', 'Navy', 'Ivory']
    },
    'Ford': {
      'F150': ['Black', 'Blue', 'Ivory'],
      'Thunderbird': ['Black', 'Red', 'White']
    },
    'Honda': {
      'Civic': ['Black', 'Navy', 'White'],
      'Pilot': ['Black', 'Brick', 'White'],
      'Accord': ['Red', 'Blue', 'Ivory']
    },
    'Dodge': {
      'Ram': ['Charcoal', 'Blue', 'White'],
      'Charger': ['Black', 'Brick', 'White'],
      'Dart': ['Charcoal', 'Red', 'White']
    }
}
"""

cars = dict()

cars = {make[1]: {} for make in makes}
# print(cars)

for (modelId, modelName, modelMakeId) in models:
    for (makeId, makeName) in makes:
        if makeId == modelMakeId:
            cars[makeName][modelName] = list()
# print(cars)

modelCarColor = dict()

for (modelId, modelName, modelMakeId) in models:
    modelCarColor[modelName] = list()
# print(modelCarColor)

for(availableColorModelId, availableColorColorId) in available_car_colors:
    for (modelId, modelName, modelMakeId) in models:
        if availableColorModelId == modelId:
            for(colorId, colorName) in colors:
                if colorId == availableColorColorId:
                    modelCarColor[modelName].append(colorName)
# print(modelCarColor)

for (model, modelMakes) in cars.items():
    for(make, makeColors) in modelMakes.items():
        for(modelMakes, modelMakeColors) in modelCarColor.items():
            if modelMakes == make:
                cars[model][make] = modelMakeColors

# print(cars)

# Output a report on the command line that looks like this.
"""
Ford
------------------
F150 available in Black, Blue, Ivory
Thunderbird available in Black, Red, White

etc...
"""

reports = list()
for(model, modelMakes) in cars.items():
    reports.append(f"{model} --------------------")
    for(make, makeColors) in modelMakes.items():
        reports.append(f"{make} available in {', '.join(makeColors)}")

print("\n".join(reports))

