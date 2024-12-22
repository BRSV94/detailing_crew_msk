import json


with (open('autos/brands_autos.json', 'r', encoding='utf-8') as brands,
      open('autos/models_autos.json', 'r', encoding='utf-8') as models):

    CHOICE_BRANDS = json.load(brands)
    CHOICE_MODELS = json.load(models)



# with open('autos/choice_models.json', 'r', encoding='utf-8') as file:
    
#     CHOICE_MODELS = json.load(file)




# with (open('autos/models_autos.json', 'r', encoding='utf-8') as file,
#       open('autos/cars.json', 'r', encoding='utf-8') as file2):
#     cmodels = json.load(file)
#     data = json.load(file2)
#     X = []
#     for brand in data:
#         if brand['popular']:
#             models = []
#             for model in cmodels[brand['name']]:
#                 models.append(model)
#             X.append((brand['name'], models))
#     for brand in data:
#         if not brand['popular']:
#             models = []
#             for model in cmodels[brand['name']]:
#                 models.append(model)
#             X.append((brand['name'], models))

#     with open('autos/choice_models.json', 'w', encoding='utf-8') as wfile:
#         json.dump(X, wfile, indent=2)
    



# with (open('autos/brands_autos.json', 'r', encoding='utf-8') as brands,
#       open('autos/models_autos.json', 'r', encoding='utf-8') as models):
#         BRANDS = json.load(brands)
#         MODELS = json.load(models)

# with open('autos/models_autos.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     CHOICE_MODELS = []
#     for brand in data:
#         models = []
#         for model in data[brand]:
#             models.append(model)
#         CHOICE_MODELS.append((brand, models))
#     print(CHOICE_MODELS)
    
#     with open('autos/choice_models.json', 'w', encoding='utf-8') as wfile:
#         json.dump(CHOICE_MODELS, wfile, indent=2)


    # with open('autos/models_autos.json', 'w', encoding='utf-8') as wfile:
    #     DATA = {}
    #     for brand in auto_data:
    #         DATA[brand] = [(model, model) for model in AUTO_DATA[brand]]

    #     json.dump(DATA, wfile, indent=4)
