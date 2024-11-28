# app.py
from flask import Flask, request, render_template
from recommend_mov import recommand

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_movies = []
    
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        recommended_movies = recommand(movie_name)

    return render_template('index2.html', recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
