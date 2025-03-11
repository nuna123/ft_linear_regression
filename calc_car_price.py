
# importing csv module
import csv

def read_thetas():
	try:
		thetas_dict = {}
		with open('thetas.csv', 'r') as file:
			csvFile = csv.DictReader(file)
			for row in csvFile:
				thetas_dict[row['var'].strip()] = float(row['value'])
		return thetas_dict
	except FileNotFoundError:
		print ("Thetas file not found!")
		return -1
	except:
		print("Something went wrong!")
		return -1

def get_mileage():
	while True:
		try:
			mil = input ("Enter mileage: ")
			mil = int (mil)
			return mil
		except:
			print (f"{mil}: value must be an integer!")

def estimate_price(thetas_dict, mileage):
	return (thetas_dict['theta_0'] + thetas_dict['theta_1'] * mileage)

def main ():
	# read thetas values from thetas file
	thetas_dict = read_thetas()
	if thetas_dict == -1 or len(thetas_dict) != 2 or 'theta_0' not in thetas_dict or 'theta_1' not in thetas_dict:
		print("Something went wrong! thetas file is incorrect or missing values.")
		return

	# get user input for mileage
	mileage = get_mileage()

	# calculate price
	price_estimate = estimate_price(thetas_dict, mileage)
	print (f'Your car is estimated at {price_estimate}')

'''
	ensures that main is only executed when the script is run directly,
		and not when it is imported as a module in another script.
	
'''
if __name__ == "__main__":
	main()