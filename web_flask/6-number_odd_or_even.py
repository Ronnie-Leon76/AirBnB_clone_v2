#!/home/adeptschneiderthedev/.miniconda3/envs/myenv/bin/python
"""Start a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Return C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Return Python followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return n is a number only if n is an integer"""
    if type(n) is int:
        return '{} is a number'.format(n)
    

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return a HTML page only if n is an integer"""
    if type(n) is int:
        return render_template('5-number.html', n=n)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
