from flask import Flask, render_template
import random
import datetime


app = Flask(__name__)


def make_h1(function):
    def wrapper():
        return f'<h1>{function()}</h1>'
    return wrapper


@app.route('/')
# @ make_h1
def intro_page():
    rand = random.randint(1, 10)
    now = datetime.datetime.now()
    return render_template('index.html', rand_num=rand, year=now.year)


@app.route('/guess/<name>')
def guess_age_and_gender():
    return render_template('age_and_gender.html')

if __name__ == '__main__':
    app.run(debug=True)