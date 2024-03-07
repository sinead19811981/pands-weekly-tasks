# This program reads in
# a students percentage
# and prints out the
# corresponding grade

"""
Under 40% => Fail
• Between 40% and 49% => Pass
• Between 50% and 59% => Merit 2
• Between 60% and 69% => Merit 1
• Over 70% => Distinction
"""

percentage = float(input("Please entera percentage: ")) #prints user percentage
if percentage < 0 or percentage > 100:
    print("Please enter an number between 1 and 100")
elif percentage <40:
    print("Fail")
elif percentage <50:
    print("Pass")
elif percentage <60:
    print("Merit1")
elif percentage <70:
    print("Merit2")
else:
    print("Distriction")


