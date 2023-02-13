import InsectClass as I


mosquito = I.Insect("mosquito", 2, 4)
housefly = I.Insect("housefly", 2, 4)

mosquito.flight_length()
housefly.flight_length()

print(f"This {mosquito.get_name()} can fly {mosquito.get_miles()} miles")

print(f"This {housefly.get_name()} can fly {housefly.get_miles()} miles")
