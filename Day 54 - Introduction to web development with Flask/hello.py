# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# app.run()

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    def one():
        print("one")

    def two():
        print("two")

    return nested_function, one, two


inner_function, a, b = outer_function()
inner_function(), b()