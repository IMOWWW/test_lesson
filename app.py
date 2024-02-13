from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='media')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index1():
    return 'Home Page'


if __name__ == "__main__":
    app.run()