YOUR_AGE = int(input("YOUR AGE:"))
license = input("DO YOU HAVE A LICENSE Y/N:")
minumum_age = 18
required_license="Y"

if YOUR_AGE >= minumum_age and license == required_license:
    print("YOU ARE ELIGIBLE TO DRIVE")
elif YOUR_AGE < minumum_age and license == required_license:
    print("YOU STILL NEED A ADULT TO SUPERVISE YOU")
elif YOUR_AGE >= minumum_age and license != required_license:
    print("YOU STILL NEED TO TAKE DRIVING SCHOOL")
else:
    print("YOU ARE NOT ELIGIBLE TO DRIVE")