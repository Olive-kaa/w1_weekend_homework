# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, nr_pets_sold):
    pet_shop["admin"]["pets_sold"] += nr_pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, chosen_breed):
    pets_of_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == chosen_breed:
            pets_of_breed.append(chosen_breed)
        else:
            pets_of_breed == 0
    return pets_of_breed

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pass

#     for pet in pet_shop["pets"]:
#         pet_shop["pets"].append(pet)
