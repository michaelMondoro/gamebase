from flask import Flask
from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)
app.config['DEV'] = True
app.config['ASSETS_ROOT'] = '/static/assets'


@app.route('/home.html')
@app.route('/home')
@app.route('/')
def home():
    """ Main route """
    games = [{"team1": "LA Clippers",
             "team2": "MEM Grizzlies",
             "score1": 0,
             "score2": 0,
             "odds1": 40,
             "odds2": 60},
             
             {"team1": "MIN Timberwolves",
             "team2": "ATL Hawks",
             "score1": 0,
             "score2": 0,
             "odds1": 50,
             "odds2": 50},
             
             {"team1": "GS Warriors",
             "team2": "DAL Mavericks",
             "score1": 0,
             "score2": 0,
             "odds1": 38,
             "odds2": 62}]
    return render_template('home.html', games=games)

@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/your_picks')
def picks():
    return render_template('picks.html')

# Load Browser Favorite Icon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='icon.jpeg')

if __name__ == "__main__":
    app.run(debug=app.config['DEV'])