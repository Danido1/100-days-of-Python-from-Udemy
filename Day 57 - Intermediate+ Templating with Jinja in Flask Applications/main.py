from flask import Flask, render_template
import time
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = time.strftime("%Y")
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, genre=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(blog_url)
    all_posts = r.json()
    return render_template("blog.html", posts=all_posts)




if __name__ == "__main__":
    app.run(debug=True)


