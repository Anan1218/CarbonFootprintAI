# aarush.py
# since 1.21.2021

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

from carbon_converter import carbon_converter
cc = carbon_converter()

# This is how you authenticate.
metadata = (('authorization', 'Key ca6dff40c60c49f69cdafd0a3ea2b5e5'),)

request = service_pb2.PostModelOutputsRequest(
    # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
    # public id: aaa03c23b3724a16a56b629203edc62c
    
    model_id='bd367be194cf45149e75f01d59f77ba7',
    inputs=[
      resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url='https://cdn.theculturetrip.com/wp-content/uploads/2018/02/shutterstock_358538228.jpg')))
    ])
response = stub.PostModelOutputs(request, metadata=metadata)

if response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Request failed, status code: " + str(response.status.code))

total = 0
for concept in response.outputs[0].data.concepts:
    carbon_footprint = (cc.get_carbon(concept.name))
    if carbon_footprint != -1 and concept.value > .5:
        total += cc.get_carbon(concept.name)
        print('%12s: %.2f \tcarbon: %.1f kgCO2' % (concept.name, concept.value, (carbon_footprint)))

print("Total carbon emission based on ingredients: " + str(total) + ' kgCO2')
food_item = response.outputs[0].data.concepts[0]
big_carbon = cc.get_big_carbon(food_item.name)
if big_carbon != -1:
    print(food_item.name + " has an estimated carbon footprint of " + str(big_carbon) +" kgCO2")