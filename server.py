from flask import Flask, render_template


app = Flask(__name__)


def make_h1(function):
    def wrapper():
        return f'<h1>{function()}</h1>'
    return wrapper


@app.route('/')
# @ make_h1
def intro_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)