# -------------
# -- User Input --

fname = input("What\'s is Your First Name?\n")
mname = input("What\'s is Your Middle Name?\n")
lname = input("What\'s is Your Last Nfame?\n")
fname = fname.capitalize().strip()
mname = mname.capitalize().strip()
lname = lname.capitalize().strip()

print(f"Your Full Name is: {fname} {mname:.1s} {lname}")
