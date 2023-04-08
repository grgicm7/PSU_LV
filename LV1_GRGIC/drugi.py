x = float(2.55)

while True:
    try:
        x = float(input("Unesite broj u intervalu [0.0, 1.0]: "))

        if (x >= 0.0 and x <= 1.0):
            break;
        else: 
            print("Unjeli ste broj koji nije u zadanom intervalu [0.0, 1.0]")
    except:
        print("Unjeli ste tip podatka koji nije broj")

if x >= 0.9:
    print("ocjena A", x)
elif x >= 0.8:
    print("ocjena B", x)
elif x >= 0.7:
    print("ocjena C", x)
elif x >= 0.6:
    print("ocjena D", x)
else:
    print("ocjena F", x)