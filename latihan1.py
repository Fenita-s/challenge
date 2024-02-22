for i in range (1,100):
    a = i >= 10 and i <= 20 and i % 2 == 0
    b = i >= 90 and i <= 100 and i % 2 == 1
    if a or b:
        print(f"{i}")
    else:
        continue