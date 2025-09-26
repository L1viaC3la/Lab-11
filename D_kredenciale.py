user = input("User: ").strip().lower()
password = input("Pass: ").strip().lower()

if (user == "admin" and password == "python") or (user == "guest" and password == "1234"):
    print("Hyrje e lejuar")
else:
    print("Hyrje e refuzuar")
