from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://cdn.shopify.com/s/files/1/0376/6478/4520/articles/First_Kitten_Banner_968x.jpg?v=1639354876" width=400>'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@app.route("/bye")
@make_bold
def bye():
    return "bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)