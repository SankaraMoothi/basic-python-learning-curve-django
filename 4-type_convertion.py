birth_year=input("Enter Your Year Of Birth? ")
# age=2023-birth_year will case error because age=2023-"1999"

# there was Many Inbuilt Function For Convertion the data type
# like:
# int()
# float()
# str()
# bool()

age=2023-int(birth_year)
print("Your Age Is ",age)