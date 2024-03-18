
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, validators
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

#themovedb API
API = "b9b445ca5c45b2341a78d3628118e881"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOWI0NDVjYTVjNDViMjM0MWE3OGQzNjI4MTE4ZTg4MSIsInN1YiI6IjY1YzFmNTVhMDkyOWY2MDE4MmU0ZjViMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kK2y_z7PDXtrlKb0XmLP2dtkxcRAoK4yOd2rtH10kD4"
URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)
# CREATE TABLE

class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# new_movie = Movies(
#     title="home alone",
#     year=1994,
#     description="a boy home alone in his house",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the the protagonist.",
#     image_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#)
#with app.app_context():
    #db.session.add(new_movie)
    #db.session.commit()



class RateMovieForm(FlaskForm):
    rating = FloatField('Your rating between 0 and 10', [validators.NumberRange(min=0, max=10)])
    review = StringField('Your review', [validators.Length(min=2, max=100)])
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    title = StringField("Add movie", validators=[DataRequired()])
    submit = SubmitField("Done")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all() # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movies, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movies, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovie()
    params = {
        "query": form.title.data
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOWI0NDVjYTVjNDViMjM0MWE3OGQzNjI4MTE4ZTg4MSIsInN1YiI6IjY1YzFmNTVhMDkyOWY2MDE4MmU0ZjViMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kK2y_z7PDXtrlKb0XmLP2dtkxcRAoK4yOd2rtH10kD4"
    }
    if form.validate_on_submit():
        response = requests.get("https://api.themoviedb.org/3/search/movie", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()["results"]
        print(data)
        return render_template("select.html", options=data)
        
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiOWI0NDVjYTVjNDViMjM0MWE3OGQzNjI4MTE4ZTg4MSIsInN1YiI6I"
                         "jY1YzFmNTVhMDkyOWY2MDE4MmU0ZjViMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kK2y_z7PDXt"
                         "rlKb0XmLP2dtkxcRAoK4yOd2rtH10kD4",
        "language": "en-US"
    }

    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        #The language parameter is optional, if you were making the website for a different audience
        response = requests.get(movie_api_url, headers=headers)
        data = response.json()
        new_movie = Movies(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            image_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        # Redirect to /edit route instead of home to add rating and review.
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
