from flask import Flask
import classify_nsfw
import caffe
import uuid
import os
app = Flask(__name__)

MODEL_DEF = "./nsfw_model/deploy.prototxt"
PRETRAINED_MODEL="./nsfw_model/resnet_50_1by2_nsfw.caffemodel"

nsfw_net = caffe.Net(MODEL_DEF,
                     PRETRAINED_MODEL,
                     caffe.TEST)

@app.route('/', methods=["POST"])
def deep():
    data = request.data
    filepath = uuid.uuid4() + ".jpg"
    with open(filepath, 'wb') as f:
        f.write(data)
    res = classify_nsfw.classify_image(filepath, nsfw_net)
    os.remove(filepath)
    return res

app.run(host='0.0.0.0')
