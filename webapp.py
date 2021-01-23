from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from main_python import Main_Python



app=Flask(__name__)
Bootstrap(app)

@app.route("/home", methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route("/about")
def about():
	return "About Us :)"

@app.route('/predict', methods=['GET', 'POST'])
def postRequest():
	if request.method == 'POST':
		url = request.get_data(as_text=True)
		print(url)
		# print(url.decode("utf-8"))
		mp = Main_Python(url)
		result = mp.make_carbon_array(mp.get_food())
		print(mp.make_carbon_array(mp.get_food()))
		print(mp.total_carbon_ingredients(result))
		return "hello"
	return None
		

if __name__ == '__main__':
	app.run(port=5000,debug=True)