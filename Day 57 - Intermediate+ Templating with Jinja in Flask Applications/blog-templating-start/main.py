from flask import Flask, render_template
import requests


app = Flask(__name__)



@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_blogs = response.json()
    return render_template("index.html", blogs=all_blogs)

@app.route('/post/<int:blog_id>')
def blogs(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_blogs = response.json()
    data_list = []
    for id_data in all_blogs:
        if id_data["id"] == blog_id:
            data_list.append(id_data)
        else:
            pass
    return render_template("post.html", data_list=data_list)

if __name__ == "__main__":
    app.run(debug=True)
