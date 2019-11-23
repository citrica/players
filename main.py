class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


print("Enter a football player's data!! ")
fName = input("Enter a player name: ")
fLastName = input("Enter last name: ")
fHeight = input("Enter height: ")
fWeight = input("Enter weight: ")
goals = input("Enter goals: ")
yellowCards = input("Enter yellow cards: ")
redCards = input("Enter red cards: ")

print("Enter a basketboll player's data!! ")
bName = input("Enter a player name: ")
bLastName = input("Enter last name: ")
bHeight = input("Enter height: ")
bWeight = input("Enter weight: ")
points = input("Enter points: ")
rebounds = input("Enter rebounds: ")
assists = input("Enter assists: ")

new_player_football = FootballPlayer(first_name=fName,
                                     last_name=fLastName,
                                     height_cm=float(fHeight),
                                     weight_kg=float(fWeight),
                                     goals=int(goals),
                                     yellow_cards=int(yellowCards),
                                     red_cards=int(redCards))

new_player_basket = BasketballPlayer(first_name=bName,
                                     last_name=bLastName,
                                     height_cm=float(bHeight),
                                     weight_kg=float(bWeight),
                                     points=int(points),
                                     rebounds=int(rebounds),
                                     assists=int(assists))

with open("football_players.txt", "w") as football_file:
    football_file.write(str(new_player_football.__dict__))

with open("basket_players.txt", "w") as basket_file:
    basket_file.write(str(new_player_basket.__dict__))

print("Football player's data: " + str(new_player_football.__dict__))

print("Basketball player's data: " + str(new_player_basket.__dict__))
