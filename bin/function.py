#!/bin/python 
def get_info():
	height = float(raw_input("What's your height (inches or meters)?"))
	weight = float(raw_input("What's your weight (pounds ir kilograms)?"))
	print("your height %s" % int(height))
	print("your weight %s" % weight)
	unit = raw_input("Are your measurements in metric or imperial units?").lower().strip()
	bmi = " "
	return(weight,height,unit)

def calculate_bmi(weight,height,unit='metric'):
	if unit == 'metric':
		bmi = (weight / (height ** 2))
	else:
		bmi  = 703 * (weight / (height ** 2))
while True:
	weight, height, unit = get_info()

	if unit.startswith('i'):
		calculate_bmi(height=height, weight=weight, unit=unit)
		break
	elif unit.startswith('m'):
		calculate_bmi(weight,height,unit)
		break
	else:
		print("Error: Unknow value!")
		break
print("Your BMI is %s"  % bmi)
