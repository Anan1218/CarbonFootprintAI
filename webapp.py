from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from main_python import Main_Python
import os



app=Flask(__name__)
Bootstrap(app)

@app.route("/home", methods=['GET', 'POST'])
def home():
	return render_template('index.html')

# @app.route("/result")
# def result(carbonEmissions):

# 	context = {
# 		carbonEmissions: carbonEmissions
# 	}
# 	return context

@app.route('/predict', methods=['GET', 'POST'])
def postRequest():
	if request.method == 'POST':
		url = request.get_data(as_text=True)
		print(url)

		mp = Main_Python(url)
		list_of_carbon = mp.make_carbon_array(mp.get_food())
		# print(mp.make_carbon_array(mp.get_food()))
		print('%.1f' % (mp.total_carbon_ingredients(list_of_carbon)))
		result = mp.total_carbon_ingredients(list_of_carbon)
		if(mp.get_finished_food_carbon() != -1):
			result = mp.get_finished_food_carbon()

		foodItems = []
		for item in list_of_carbon:
			foodItems.append(item[0] + ", " + item[1])
		context = { 
			"result": result,
			"foodItems": foodItems
		}
		print(foodItems)
		return context
		# return str(result)
	return ""
		

if __name__ == '__main__':
	app.run(port=5000,debug=True)