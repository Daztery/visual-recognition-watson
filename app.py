import json
from ibm_watson import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='YourApiKey')

with open('img/vin-diesel.jpg', 'rb') as images_file:
    faces = visual_recognition.detect_faces(images_file).get_result()
print(json.dumps(faces, indent=2))