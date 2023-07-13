

// Function to call the /update endpoint which pings the API and returns the updated odds data
// The returned data is then used to update the respective html elements 
function update() {
	$.post('/update', {}, function (data) {
		for (var i in data ){
            game = data[i]
			game_div = document.getElementById(game["id"]);
            
            home_team = game_div.querySelector('#home_team');
            away_team = game_div.querySelector('#away_team');

            home_score = game_div.querySelector('#home_score');
            home_score.innerText = game["home_score"]
            away_score = game_div.querySelector('#away_score');
            away_score.innerText = game["away_score"]

            home_odds = game_div.querySelector('#home_odds');
            home_odds.innerText = game["home_odds"]
            away_odds = game_div.querySelector('#away_odds');
            away_odds.innerText = game["away_odds"]

            home_button = game_div.querySelector('#home_button');
            home_button.innerText = "+ BUY @ " + game["away_odds"]
            away_button = game_div.querySelector('#away_button');
            away_button.innerText = "+ BUY @ " + game["away_odds"]

            odds = game_div.querySelector('#odds');
            odds.style.background = `linear-gradient(90deg, black ${game['home_odds']}%, blue 10%)`

		}
	})	
}

// Update the games on the page every 5 seconds
setInterval(update, 5000);
