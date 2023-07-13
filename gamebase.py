from flask import Flask
from flask import Flask, render_template, jsonify, url_for
import requests

app = Flask(__name__)
app.config['DEV'] = True
app.config['ASSETS_ROOT'] = '/static/assets'

odds = []

@app.route('/home.html')
@app.route('/home')
@app.route('/')
def home():
    """ Main route """

    # Dummy data
    dummy_data = [{'away_team': 'CLE Cavaliers', 'away_odds': 0, 'away_score': 0, 'home_team': 'CHI Bulls', 'home_odds': 0, 'home_score': 0, 'id': '29111448'}, 
                  {'away_team': 'PHI 76ers', 'away_odds': 0, 'away_score': 0, 'home_team': 'ATL Hawks', 'home_odds': 0, 'home_score': 0, 'id': '29111449'}, 
                  {'away_team': 'BKN Nets', 'away_odds': 0, 'away_score': 0, 'home_team': 'TOR Raptors', 'home_odds': 0, 'home_score': 0, 'id': '29111450'}, 
                  {'away_team': 'MIA Heat', 'away_odds': 0, 'away_score': 0, 'home_team': 'MIL Bucks', 'home_odds': 0, 'home_score': 0, 'id': '29111454'}, 
                  {'away_team': 'HOU Rockets', 'away_odds': 0, 'away_score': 0, 'home_team': 'GS Warriors', 'home_odds': 0, 'home_score': 0, 'id': '29111455'}, 
                  {'away_team': 'CHA Hornets', 'away_odds': 0, 'away_score': 0, 'home_team': 'NO Pelicans', 'home_odds': 0, 'home_score': 0, 'id': '29111457'}, 
                  {'away_team': 'POR Trail Blazers', 'away_odds': 0, 'away_score': 0, 'home_team': 'ORL Magic', 'home_odds': 0, 'home_score': 0, 'id': '29111458'}, 
                  {'away_team': 'MIN Timberwolves', 'away_odds': 0, 'away_score': 0, 'home_team': 'SAC Kings', 'home_odds': 0, 'home_score': 0, 'id': '29111460'}]
    
    games = dummy_data

    return render_template('home.html', games=games)

@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/your_picks')
def picks():
    return render_template('picks.html')

@app.route('/update', methods=["POST"])
def update():
    return jsonify(update_data())

# Load Icon
@app.route('/favicon.ico')
def favicon():
    return url_for('static', filename='icon.jpeg')


""" Method to ping the API and get the new odds data """
def update_data():
    res = requests.get("https://dk-sports-api-sampasco2024.replit.app/nba")
    # Get list of games from response
    data = res.json()

    # Build list of odds
    new_odds = []
    for game in data: 
        new_odds.append({'away_team':game['away_team'], 'away_odds':game['away_odds'], 'away_score':game['away_score'],
                     'home_team': game['home_team'], 'home_odds': game['home_odds'], 'home_score': game['home_score'], "id": game['matchup_id']})
    # If the odds have changed, return the new odds. If not, return empty
    if odds == new_odds:
        return {}
    else:
        return new_odds


if __name__ == "__main__":
    app.run(debug=app.config['DEV'])