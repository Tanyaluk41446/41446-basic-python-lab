number = int(input("Enter your number: "))
for i in range(1,13):
    print(f"แม่ {i}")
    for j in range(1,13):
        print(f"{i}*{j} = {i*j}")
    print()