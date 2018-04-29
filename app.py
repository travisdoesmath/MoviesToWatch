from flask import Flask, render_template
import pymongo

app = Flask(__name__, static_url_path='/static')

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.movies_db

@app.route("/")
def index():
    #movies = db.movies.find({'index': { '$gt': 10, '$lt': 20 }})
    movies = db.movies.find()
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
