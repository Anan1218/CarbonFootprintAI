# main_python.py
# since: 1.22.2021

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

from carbon_converter import carbon_converter
cc = carbon_converter()


class Main_Python:
    
    # constructor
    def __init__ (self, url):
        print("ITS WORKING")
        self.link = url
        self.food_list = []
        self.carbon_values = []
    
    # creates a list of foods, their prediction value and other relevant data
    def get_food(self):
        metadata = (('authorization', 'Key ca6dff40c60c49f69cdafd0a3ea2b5e5'),)

        request = service_pb2.PostModelOutputsRequest(
            # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
            # public id: aaa03c23b3724a16a56b629203edc62c
            
            model_id='bd367be194cf45149e75f01d59f77ba7',
            inputs=[
            resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=self.link)))
            ])
        response = stub.PostModelOutputs(request, metadata=metadata) 

        if response.status.code != status_code_pb2.SUCCESS:
            raise Exception("Request failed, status code: " + str(response.status.code))

        
        return response.outputs[0].data.concepts # may need to return

    # complies list of only ingredients and their carbon footprint
    def make_carbon_array(self, foods):
        # foods = food_list
        array = []
        for food in foods:
            carbon_footprint = (cc.get_carbon(food.name))
            if carbon_footprint != -1 and food.value > .5:
                array.append((food.name, carbon_footprint))
        return array # might cause an issue, may need to return values

    # gets the total carbon footprint of all ingredients
    def total_carbon_ingredients(self, values):
        total = 0
        for carbon in values:
            total += carbon[1]

        return total