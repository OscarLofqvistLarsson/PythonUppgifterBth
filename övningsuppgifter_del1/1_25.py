import random

player_1 = str(input("Player 1, whats your name?"))
player_2 = str(input("Player 2, whats your name?"))

player_1_throw = random.randint(1,6)
player_2_throw = random .randint(1,6)

if player_1_throw > player_2_throw:
    print(player_1, "won with",player_1_throw,"as", player_2, "got" ,player_2_throw)

if player_1_throw < player_2_throw:
    print(player_2, "won with",player_2_throw, "as", player_1, "got", player_1_throw )

if player_1_throw == player_2_throw:
    print(player_1, "and",player_2, "both got", player_1_throw)

print("quitting program")