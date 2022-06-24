answer = ""
part = ["mislav", "stanko", "mislav", "ana"]
com = ["stanko", "ana", "mislav"]
	
dictionary = dict()

for player in com:
    if player in dictionary:
        dictionary[player] += 1
    else :
        dictionary[player] = 1

for player in part:
    if player in dictionary:
        dictionary[player] -= 1
    else :
        answer = player
        break

for player, cnt in dictionary.items():
    if cnt < 0:
        answer = player

print(answer)