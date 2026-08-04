# value = 13
# remainder = value % 5

# if remainder:
#     print(f"{value} is not a multiple of 5 and {remainder} is the remainder")



value = 13
if(remainder := value % 5 ):    # walrus operator 
    print(f"{value} is not a multiple of 5 and {remainder} is the remainder")


available_sizes = ["Small", "Medium", "Large", "Extra Large"]

if(requested_size := input("Enter the size of tea you want: ")) in available_sizes:
    print(f"{requested_size} tea is ready")
else:
    print(f"Sorry, {requested_size} tea is not available")