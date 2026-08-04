flavours = ["Green Tea", "Black Tea", "White Tea", "Oolong Tea" ,"Out of Stock","Discontinued"]

for flavor in flavours:
    if flavor == "Out of Stock" :
        print(f"{flavor} is not available")
        continue
    if flavor == "Discontinued" :
        print(f"{flavor} is no longer available")
        break
    print(f"{flavor} chai is ready")