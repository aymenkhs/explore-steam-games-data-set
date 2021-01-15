from datetime import datetime

import pandas as pd

def read_data_set(path = "steam.csv"):
    steam_data = pd.read_csv(path)
    steam_data = steam_data[["name", "release_date", "developer", "publisher", "platforms", "price"]]

    # converting strings to datetime to treat them
    steam_data["release_date"] = [datetime.strptime(date, '%Y-%m-%d').year for date in steam_data["release_date"].tolist()]

    steam_data["price"] = [float(price) for price in steam_data["price"]]

    steam_data["developer"] = [dev.lower() for dev in steam_data["developer"]]

    return steam_data


def print_games(data_games):
    counter = 0
    print(end="\n\n")
    print ("{:4} {:<60} {:<20} {:<40} {:<40} {:<40} {:<10}".format("num" ,"name", "release_date", "developer", "publisher", "platforms", "price"))
    print("_" * 215)
    for index in data_games.index.tolist():
        if index > 100:
            break
        print ("{:4} {:<60} {:<20} {:<40} {:<40} {:<40} {:<10}".format(index ,data_games.loc[index,"name"] , data_games.loc[index,"release_date"],
            data_games.loc[index, "developer"], data_games.loc[index, "publisher"], data_games.loc[index, "platforms"], data_games.loc[index, "price"]))
        print("_" * 215)


def menu(steam_data):
    print("choose between (we'll print only the 100 first result):\n1. print all games\n2. print games depending on prices\n3. print games depending on release date "
            , "\n3. print games depending on developer")
    num = input("type your input there : ")
    if num == "1":
        print_games(steam_data)
    elif num == "2":
        price = float(input("give a price (for free games just type 0) : "))
        masque = steam_data["price"] <= price
        print_games(steam_data[masque])
    elif num == "3":
        developer = input("developers name : ")
        masque = steam_data["developer"] == developer
        print_games(steam_data[masque])
    elif num == "4":
        year = int(input("release year : "))
        masque = steam_data["release_date"] == year
        print_games(steam_data[masque])
    else:
        print("what did you just type? try again!")
    menu(steam_data)

if __name__ == '__main__':
    steam_data = read_data_set()
    menu(steam_data)
