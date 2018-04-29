from flask import Flask, render_template, redirect
import pymongo

app = Flask(__name__, static_url_path='/static')

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.movies_db

@app.route("/")
def index():
    movies = db.movies.find()
    return render_template("index.html", movies=movies)

@app.route("/markseen/<title_id>")
def markseen(title_id):
    try:
        db.movies.update({"title_id":title_id}, {'$set':{"seen":True}})
    except:
        print(f'An error occured trying to update {title_id}')
    return redirect(f"/#{title_id}", code=302)

@app.route("/markunseen/<title_id>")
def markunseen(title_id):
    try:
        db.movies.update({"title_id":title_id}, {'$set':{"seen":False}})
    except:
        print(f'An error occured trying to update {title_id}')
    return redirect(f"/#{title_id}", code=302)

if __name__ == "__main__":
    app.run(debug=True)
