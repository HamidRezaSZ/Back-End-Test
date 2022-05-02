import urllib
import numpy as np
from .apps import CifarModelConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
import cloudinary.uploader
import cv2






class ClassifyView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )
    

    @staticmethod
    def post(request):
        
        file = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(file)
        img = upload_data['url']
        
        
        req = urllib.request.urlopen(img)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, -1) 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (32, 32) )



        #load models
        model = CifarModelConfig.model

        number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',\
                        'frog', 'horse', 'ship', 'truck']

        # PREDICT ON THE IMAGE
        probabilities=model.predict(np.array([image]))
        index = np.argsort(probabilities[0,:])


        return Response({

            'url':img,
            'Most likely': number_to_class[index[9]],
            
            
        }, status=201)