# testClarifai.py
# since 1.21.2021

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# This is how you authenticate.
metadata = (('authorization', 'Key ca6dff40c60c49f69cdafd0a3ea2b5e5'),)

request = service_pb2.PostModelOutputsRequest(
    # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
    # public id: aaa03c23b3724a16a56b629203edc62c
    model_id='bd367be194cf45149e75f01d59f77ba7',
    inputs=[
        # good mochi: https://cdn.theculturetrip.com/wp-content/uploads/2018/02/shutterstock_358538228.jpg
        resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url='https://media-cdn.tripadvisor.com/media/photo-s/06/f9/70/5e/caffe-chino.jpg')))
    ])
response = stub.PostModelOutputs(request, metadata=metadata)

if response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Request failed, status code: " + str(response.status.code))

for concept in response.outputs[0].data.concepts:
    print('%12s: %.2f' % (concept.name, concept.value))