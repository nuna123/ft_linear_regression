
# importing csv module
import csv

#import matlib stuff
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

DATA_FILE = 'data.csv'
THETAS_FILE = 'thetas.csv'


def normalize_data(data):
	max_km = max(d[0] for d in data)
	return [(d[0] / max_km, d[1]) for d in data], max_km

def load_data(filename = DATA_FILE):
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

def save_thetas_csv(thetas, max_km, filename=THETAS_FILE):
	print ("SAVE THETAS")
	with open(filename, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['var', 'value'])
		writer.writerow(['theta_0', thetas[0]])
		writer.writerow(['theta_1', thetas[1]])
		writer.writerow(['max_km', max_km])

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
	for i in range (1, iterations + 1):
		error_sum_0 = 0
		error_sum_1 = 0
		for value in data:
			value_km = value[0]
			value_price = value[1]
			# calculate price using thetas
			prediction = estimate_price(value_km, theta_0, theta_1)
			
			# add to error sum
			error = prediction - value_price
			
			error_sum_0 += error
			error_sum_1 += error * value_km

		theta_0 -= (learning_rate * error_sum_0) / len (data)
		theta_1 -= (learning_rate * error_sum_1) / len (data)
		if i % 10 == 0 or i == 1:
			yield theta_0, theta_1, i

def animate(data, thetas, iterations=1000, learning_rate=.1):
	fig, ax = plt.subplots()
	x_vals = [d[0] for d in data]
	y_vals = [d[1] for d in data]
	y_predictions = [0 for x in x_vals]
	scatter = ax.scatter(x_vals, y_vals, color='#077A7D')
	line, = ax.plot(x_vals, y_predictions, color='#7AE2CF', linewidth=2)

	ax.set_xlim(0, 1)
	ax.set_ylim(0, max(y_vals) * 1.1)
	ax.set_xlabel("Normalized km")
	ax.set_ylabel("Price")

	ax.set_facecolor('#06202B')
	# Add iteration count text
	iter_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, color='white', fontsize=12, verticalalignment='top')


	last_theta_values = None
	theta_gen = update_thetas(thetas, data, iterations, learning_rate)

	def update(frame):
		nonlocal last_theta_values
		theta_0, theta_1, i = next(theta_gen)
		last_theta_values = (theta_0, theta_1)  # Capture the latest theta values

		print (i, ":", theta_0, theta_1)
		y_pred = [estimate_price(x, theta_0, theta_1) for x in x_vals]
		line.set_data(x_vals, y_pred)
		iter_text.set_text(f"Iteration: {i}")

		return line, iter_text

	anim = FuncAnimation(fig, update, frames=iterations // 10, interval=50, repeat=False)
	plt.show()
	return last_theta_values

def main():
	data = load_data()
	if data == -1 :
		return -1
	ret = normalize_data(data)
	thetas = (0,0)
	data = ret[0]
	max_km = ret[1]
	
	thetas = animate(data, thetas)
	print (thetas)



	print ("HERE")
	# Denormalize theta_1, to be able to use it in predictions
	thetas = (thetas[0], thetas[1] / max_km)

	save_thetas_csv(thetas, max_km)
	print (thetas)


'''
	ensures that main is only executed when the script is run directly,
		and not when it is imported as a module in another script.
	
'''
if __name__ == "__main__":
	main()