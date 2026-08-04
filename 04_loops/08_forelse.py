staff = [("htesh", 10), ("raj", 20), ("suresh", 30), ("rajesh", 40), ("Aman", 50), ("Backey", 60), ("Karlos", 70)]

for name , age in staff:
    if age < 18:
        print(f"{name} is not eligible to work")
        continue
    if age > 60:
        print(f"{name} is retired")
        break
    print(f"{name} is working")