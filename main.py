
robots = {"robot1": "údržba", "robot2": "úklid", "robot3": "vaření"}

while True:
    name = input("Zadejte jméno robota (nebo 'konec' pro ukončení): ").strip()
    
    if name.lower() == "konec":
        break 
    if name in robots:

        print(f"Funkce robota {name}: {robots[name]}")
    else:
        function = input(f"Robot {name} není v seznamu. Zadejte jeho funkci: ").strip()
        robots[name] = function
        print(f"Robot {name} byl přidán s funkcí: {function}")
print("\nSeznam robotů a jejich funkcí:")
for name, function in robots.items():
    print(f"{name}: {function}")