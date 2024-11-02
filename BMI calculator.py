Height= float(input('Enter your Height in Centemeters: '))
Mheight=Height*0.01
weight= float(input('Enter your weight (in KG): '))
BMI= weight/(Mheight**2)
BMI= round(BMI,2)
str_BMI=str(BMI)
print('Your BMI is: '+ str_BMI)
if BMI <18.5:
 print('Under Weight')
elif BMI>= 18.5 and BMI<25:
 print('Standard Weight')
elif BMI>=25:
 print('Over Weight')
else:
 print('You need plastic surgery')
