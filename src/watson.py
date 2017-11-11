def post_image(url, file, api_key):
    try:
        url = "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key="+api_key+"&version=2016-05-20"

    with open(file, 'rb') as image:
        filename = image.name
        mime_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        files = {'image_file': (filename, image, mime_type)}
        r = requests.request(method = "POST", url= url, files = files)
        print(r.text)

    except:
        print("An Error occurred uploading files")