import subprocess
import requests

class NotPornHub:
    def nsfw_score(self, image_path):
        pipe = subprocess.Popen(("docker run"
                                 " --volume=$(pwd)/open_nsfw/:/workspace caffe:cpu"
                                 " python ./classify_nsfw.py"
                                 " --model_def nsfw_model/deploy.prototxt"
                                 " --pretrained_model nsfw_model/resnet_50_1by2_nsfw.caffemodel " + image_path),
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True^False
        )
        stdout, stderr = pipe.communicate()
        print("------------   8=====) -------------")
        str_score = stdout.decode().split("score:")[-1].strip()
        return float(str_score)

husk = NotPornHub()

filepath="images/test_image.jpg"

with open(filepath, 'rb') as f:
    wat = f.read()


SERVER_PATH = "http://127.0.0.1:5000/"
resp = requests.post(SERVER_PATH, data=wat)
print(resp.text)

#print("RESULT: " + str(husk.nsfw_score("./images/test_image.jpg")))
