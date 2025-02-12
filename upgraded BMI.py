height = input ("enter your height in m: ")
weight = input ("enter your weight in kg: ")

#print(int(int(weight) / (float (height))**2))

bmi = int(weight) / float(height) ** 2
bmi_as_int = int (bmi)

print (bmi_as_int)

if bmi_as_int<18.5:
    print(f"your bmi is {bmi_as_int}, and u are under weight")
elif bmi_as_int<25:
    print(f"your bmi is {bmi_as_int}, and u are normal weight")
elif bmi_as_int<30:
    print(f"your bmi is {bmi_as_int}, and u are over weight")
elif bmi_as_int<35:
    print(f"your bmi is {bmi_as_int}, and u are obese")
else:
    print(f"your bmi is {bmi_as_int}, and u are clinically obese")

