def friend(peoples):
    friends = []
    for each_individu in peoples:
        if len(each_individu) == 4:
            friends.append(each_individu)
    print(friends)

peoples = ["Ryan", "Kieran", "Jason", "Yous", "Paul"]
friend(peoples)