# carbon_converter.py
# since: 1.22.2021
class carbon_converter:
    def __init__(self):
        self.food_to_carbon = {
            "bread" : 1.4,
            "berry" : 1.1,
            "oatmeal" : 1.6,
            "onion" : 0.3,
            "corn" : 1.1,
            "rice" : 4,
            "nuts" : 0.2,
            "tofu" : 3,
            "tomato" : 1.4,
            "chicken" : 6.1,
            "lamb" : 24.5,
            "lime" : 0.3,
            "pork" : 7.2,
            "potato" : 0.3,
            "pea" : 0.8,
            "banana" : 0.8,
            "apple" : 0.3,
            "coffee" : 16.5,
            "fruit" : 0.3,
            "beef" : 59.4,
            "milk" : 2.8,
            "cheese" : 21.2,
            "egg" : 4.5,
            "fish" : 5.1,
            "shrimp" : 11.8
        }
        
        self.finished_food_to_carbon = {
            "hamburger" : 243.0,
            "ramen" : 0.0,
            "mochi" : 0.0,
        }


    def get_carbon(self, name):
        try:
            return self.food_to_carbon[name]
        except KeyError as ke:
            return -1
    
    def get_big_carbon(self, name):
        try:
            return self.finished_food_to_carbon[name]
        except KeyError as ke:
            return -1