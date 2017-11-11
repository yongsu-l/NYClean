import mimetypes
import requests
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

def post_imageV2(classifier_name, file, api_key):
    parameters={
        "classifier_ids" : ["Trashdetector_916420994"]
    }
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)

    with open(file, 'rb') as image:
        filename = image.name
        mime_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        files = {'image_file': (filename, image, mime_type)}

        print(json.dumps(visual_recognition.classify(images_file=image, 
                classifier_ids=classifier_name), indent=2))