

import matplotlib.pyplot as plt
import numpy as np
import csv


def read_data(kms, prices):
	try:
		with open('data.csv', 'r') as file:
			csvFile = csv.DictReader(file)
			for row in csvFile:
				kms.append(float (row['km'].strip()))
				prices.append(float (row['price'].strip()))
	except FileNotFoundError:
		print ("Thetas file not found!")
		return -1
	except:
		print("Something went wrong!")
		return -1


kms = []
prices = []
read_data(kms, prices)



# Standardize the features
kms_mean = np.mean(kms)
kms_std = np.std(kms) # Compute the standard deviation

prices_mean = np.mean(prices)
prices_std = np.std(prices) # Compute the standard deviation

kms_standardized = [(x - kms_mean) / kms_std for x in kms]
prices_standardized = [(y - prices_mean) / prices_std for y in prices]

print (kms_standardized)
print (prices_standardized)
xpoints = np.array(kms_standardized)
ypoints = np.array(prices_standardized)

plt.scatter(xpoints, ypoints)
plt.show()



# https://medium.com/@leogaudin/ft-linear-regression-an-introduction-guide-to-machine-learning-at-42-4d9a19a260e5



# xpoints = np.array(kms)
# ypoints = np.array(prices)

# plt.scatter(xpoints, ypoints)
# plt.show()


# def main ():
# 	pass


# '''
# 	ensures that main is only executed when the script is run directly,
# 		and not when it is imported as a module in another script.
	
# '''
# if __name__ == "__main__":
# 	main()