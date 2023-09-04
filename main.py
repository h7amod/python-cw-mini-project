
def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20


def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200


def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5


def padel_game_cost():
    court_type = input("enter court type (indoor or outdoor): ")
    racket_brand = input("enter racket brand (Bullpadel or Nox or Siux): ")
    ball_boxes = int(input("enter how many ball boxes the limit is 3 boxes: "))

    court_cost = padel_court_cost(court_type)
    racket_cost = rackets_cost(racket_brand)
    balls_cost = padel_balls_cost(ball_boxes)

    total_cost = court_cost + racket_cost + balls_cost
    return total_cost
print(padel_game_cost())



