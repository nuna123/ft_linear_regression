
# importing csv module
import csv

def normalize_data(data):
	max_km = max(d[0] for d in data)
	return [(d[0] / max_km, d[1]) for d in data], max_km

def load_data(filename = 'data.csv'):
	try:
		data_list = []
		with open(filename, 'r') as file:
			csvFile = csv.DictReader(file)
			for row in csvFile:
				values = (int (row['km'].strip()), int (row['price'].strip()))
				data_list.append(values)
		return data_list
	except FileNotFoundError:
		print ("Thetas file not found!")
		return -1
	except:
		print("Something went wrong!")
		return -1

def save_thetas_csv(theta0, theta1, filename='thetas.csv'):
	with open(filename, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['var', 'value'])          # Header
		writer.writerow(['theta_0', theta0])       # Row for theta_0
		writer.writerow(['theta_1', theta1])       # Row for theta_1

def read_thetas():
	thetas = []
	try:
		with open('thetas.csv', 'r') as file:
			csvFile = csv.DictReader(file)
			for row in csvFile:
				thetas.append(float(row['value']))
		return thetas
	except FileNotFoundError:
		print ("Thetas file not found!")
		return -1
	except:
		print("Something went wrong!")
		return -1

def estimate_price (mil, theta0, theta1):
	return theta0 + mil * theta1

def update_thetas(thetas, data, iterations=1000, learning_rate=0.1):
	theta_0 = thetas[0]
	theta_1 = thetas[1]
	for _ in range (iterations):
		error_sum_0 = 0
		error_sum_1 = 0
		for value in data:
			# calculate price using thetas
			prediction = estimate_price(value[0], theta_0, theta_1)
			
			# add to error sum
			error = prediction - value[1]
			error_sum_0 += error
			error_sum_1 += error * value[0]
		theta_0 -= (learning_rate * error_sum_0) / len (data)
		theta_1 -= (learning_rate * error_sum_1) / len (data)
	return (theta_0, theta_1)



def main():
	data = load_data()
	ret = normalize_data(data)
	thetas = read_thetas()
	data = ret[0]
	thetas = update_thetas(thetas, data)
	save_thetas_csv(thetas[0], thetas[1])
	print (thetas)


'''
	ensures that main is only executed when the script is run directly,
		and not when it is imported as a module in another script.
	
'''
if __name__ == "__main__":
	main()