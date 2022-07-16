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
    try:
        age_text = requests.get(url=f'https://api.agify.io/?name={name}')
        # print(age_text)
        age = age_text.json()["age"]
    except Exception as error_message:
        print(error_message)
        age = "??"

    try:
        gender_text = requests.get(url=f'https://api.genderize.io/?name={name}')
        # print(gender_text)
        gender = gender_text.json()["gender"]
    except Exception as error_message:
        print(error_message)
        gender = "??"

    return render_template('age_and_gender.html', name=name.title(), age=age, gender=gender)


@app.route('/blog')
def blog_page():
    url = 'https://api.npoint.io/ec84679d2403beee8160'
    blog_posts_json = requests.get(url).json()
    print(blog_posts_json)
    print(blog_posts_json[0]["title"])
    return render_template('blog.html', posts=blog_posts_json)

if __name__ == '__main__':
    app.run(debug=True)