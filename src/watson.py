import mimetypes
import requests
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

def post_imageV2(classifier_name, file, api_key):

    visual_recognition = VisualRecognitionV3('2016-05-20', api_key=api_key)

    with open(file, 'rb') as image:

        print(json.dumps(visual_recognition.classify(images_file=image, 
                classifier_ids=classifier_name, threshold=0.0),  indent=2))