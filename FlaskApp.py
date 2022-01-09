from flask import Flask, render_template, request
from test import get_tweet


app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/tweet', methods=['POST','GET'])
def tweet():
    print("123")
    tweetText = request.form.get('tweetText')
    print("456")
    print(tweetText)
    status = get_tweet(tweetText)
    return "Your Tweet has been posted"


if __name__ == '__main__':
    app.run()