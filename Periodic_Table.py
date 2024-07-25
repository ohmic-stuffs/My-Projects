import periodictable
#getting details
Atomic_No =int(input("Enter Atomic Number :"))
element = periodictable.elements[Atomic_No]
print(f'Atomic No : {element.number}')
print(f"Symbol : {element.symbol}")
print(f"Name : {element.name}")
print(f"Atomic Mass : {element.mass}")
print(f"Density : {element.density}")
print(f"Isotopes : {element.isotopes}")