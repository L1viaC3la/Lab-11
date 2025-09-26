baze = float(input("Cmimi bazë: "))
zb = float(input("Zbritja (%): "))

if baze < 0 or zb < 0 or zb > 100:
    print("Gabim: Vlera të pavlefshme.")
else:
    pas = baze * (1 - zb / 100)
    final = pas * 1.15
    print("Pas zbritjes:", round(pas, 2))
    print("Me TVSH (15%):", round(final, 2))
