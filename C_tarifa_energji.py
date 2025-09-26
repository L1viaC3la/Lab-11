kwh = int(input("kWh: "))

if kwh < 0:
    print("Gabim: Vlerë e pavlefshme.")
else:
    if kwh <= 100:
        tarifa = 8
    elif kwh <= 300:
        tarifa = 12
    else:
        tarifa = 15

    energjia = tarifa * kwh
    taksa = 120
    totali = energjia + taksa

    print("Energjia (Lek):", energjia)
    print("Taksa fikse:", taksa)
    print("Totali:", totali)

    if totali > 5000:
        print("Etiketa: Konsum i lartë")
