import requests
import time

BASE_URL = "https://www.cricbuzz.com/match-api"

def get_live_scores():
    response = requests.get(BASE_URL)
    data = response.json()

    if response.status_code == 200:
        matches = data["matches"]

        for match in matches:
            match_id = match["match_id"]
            series_name = match["series"]["series_name"]
            venue = match["venue"]["name"]
            team1 = match["team1"]["name"]
            team2 = match["team2"]["name"]
            status = match["status"]

            print("------------------------------")
            print(f"Match ID: {match_id}")
            print(f"Series: {series_name}")
            print(f"Venue: {venue}")
            print(f"{team1} vs {team2}")
            print(f"Status: {status}")
            print("------------------------------")
    else:
        print("Error fetching live scores.")

def main():
    while True:
        print("Fetching live cricket scores...")
        get_live_scores()
        time.sleep(60)  # Wait for 1 minute before fetching scores again

if __name__ == "__main__":
    main()
