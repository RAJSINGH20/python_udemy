chai_menu = {"Masala0":30,"ginger":40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("not exist")

