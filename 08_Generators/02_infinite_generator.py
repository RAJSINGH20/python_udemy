def infinite_Chai():
    count = 1;
    while True:
        yield f"Chai cup {count}"
        count += 1
        
requested_chai = infinite_Chai()

for _ in range(10):
    print(next(requested_chai)) 