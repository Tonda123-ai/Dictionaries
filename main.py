robots = {"Anna": "údržba", "Jakub": "úklid", "Filip": "vaření", "Eva": "nákupy", "Petr": "zahradničení"} 

while True:
    name = input("Zadejte jméno robota (nebo 'konec' pro ukončení): ")
    
    if name == "konec":
        break 
    if name in robots:
        print(f"Funkce robota {name}: {robots[name]}")
    else:
        function = input(f"Robot {name} není v seznamu. Zadejte jeho funkci: ")
        robots[name] = function
        print(f"Robot {name} byl přidán s funkcí: {function}")
print("\nSeznam robotů a jejich funkcí:")
for name, function in robots.items():
    print(f"{name}: {function}")
