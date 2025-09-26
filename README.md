Ky projekt përmban 4 skripte që përdorin operatorë në Python:

- A_konvertime.py: konvertim Celsius në Fahrenheit dhe cm në metra.
- B_cmim_zbritje.py: llogaritje çmimi me zbritje dhe TVSH.
- C_tarifa_energji.py: tarifim sipas kWh dhe etiketim për konsum të lartë.
- D_kredenciale.py: verifikim hyrjeje me kushte logjike.

Raste kufi të testuara:
- Celsius = 0 dhe 37
- Cmimi bazë negativ ose zbritje > 100%
- kWh = 350 → etiketa “Konsum i lartë”
- Përdorues të gabuar → hyrje e refuzuar
