while True:
    data = int(input())
    if not data:
        break

    if not data % 42:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
