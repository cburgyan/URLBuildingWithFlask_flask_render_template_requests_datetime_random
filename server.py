from flask import Flask, render_template
import random
import datetime
import requests
import ast


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
def guess_age_and_gender(name):
    age_text = requests.get(url=f'https://api.agify.io/?name={name}').text
    gender_text = requests.get(url=f'https://api.genderize.io/?name={name}').text
    print(age_text)
    age_dict = ast.literal_eval(age_text)
    age = age_dict["age"]
    print(gender_text)
    gender_dict = ast.literal_eval(gender_text)
    gender = gender_dict["gender"]
    return render_template('age_and_gender.html', name=name.title(), age=age, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)