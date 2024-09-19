import json
import csv
import urllib

data = {}
with urllib.request.urlopen("https://documenter.getpostman.com/view/24232555/2s93shzpR3#358b5496-a459-4e05-9f9d-e924633454fb") as jsonfile:
    data = json.load(jsonfile)



with open('basketball.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id",
            "playerName",
            "position",
            "age",
            "games",
            "gamesStarted",
            "minutesPg" ,
            "fieldGoals" ,
            "fieldAttempts" ,
            "fieldPercent" ,
            "threeFg" ,
            "threeAttempts" ,
            "threePercent" ,
            "twoFg" ,
            "twoAttempts" ,
            "twoPercent" ,
            "effectFgPercent" ,
            "ft" ,
            "ftAttempts" ,
            "ftPercent" ,
            "offensiveRb" ,
            "defensiveRb",
            "totalRb" ,
            "assists",
            "steals" ,
            "blocks" ,
            "turnovers" ,
            "personalFouls" ,
            "points" ,
            "team",
            "season",
            "playerId"
                        ])
    writer.writerows(data)