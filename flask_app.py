from flask import Flask, render_template
import random 

app = Flask(__name__)

images = {
    1:"https://i.imgflip.com/2ys7y7.jpg",
    2:"https://i.imgflip.com/2ypmza.jpg",
    3:"https://i.imgflip.com/2ytul6.jpg",
    4:"https://i.imgflip.com/2yrxlt.jpg",
    5:"https://i.imgflip.com/2yrfan.jpg",
    6:"https://i.imgflip.com/2yuqi8.jpg"
}

@app.route("/")
def index():
    key = random.randint(1, 6)
    image_url = images[key]
    print(image_url)
    return render_template('index.html', url=image_url)

if __name__ == "__main__":
        app.run(host="0.0.0.0")