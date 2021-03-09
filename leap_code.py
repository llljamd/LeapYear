def leap(x):
	if x % 4 == 0:
		if x % 100 == 0:
			return str(x) + " is not a leap year";
		
		else:	
			return str(x) + " is a leap year";
	else:
		return str(x) + " is not a leap year";
