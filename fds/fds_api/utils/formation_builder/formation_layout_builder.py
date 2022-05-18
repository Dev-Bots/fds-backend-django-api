


#sorting array of dictionaries
def _sort(dictionary):
    
    for i in range(len(dictionary)):
        min_idx = i
        for j in range(i+1, len(dictionary)):
            min_index = list(dictionary[min_idx].keys())[0]
            min_data = dictionary[min_idx][min_index]

            current_data_index = list(dictionary[j].keys())[0]
            current_data = dictionary[j][current_data_index]
            if min_data > current_data:
                min_idx = j
                    
        dictionary[i], dictionary[min_idx] = dictionary[min_idx], dictionary[i]
    return dictionary


def check_for_ratio(players, equal_distribution=False):
    DEF = []
    MID = []
    STR = []
    GK = []

    for player in players:
        if player.more.playing_possition1 == "DEF":
            DEF.append(player)
        elif player.more.playing_possition1 == 'MID':
            MID.append(player)
        elif player.more.playing_possition1 == 'STR':
            STR.append(player)
        elif player.more.playing_possition1 == 'GK':
            GK.append(player)

    no_of_DEF = len(DEF)
    no_of_MID = len(MID)
    no_of_STR = len(STR)
    no_of_GK =  len(GK)

    position_numbers = [{
        "DEF": no_of_DEF},
        {"MID": no_of_MID},
        {"STR": no_of_STR}
  
        ]



    accending_sorted = _sort(position_numbers)

    required_amounts = {}

    #positions with quantities from min to max
    pos1 = list(accending_sorted[0].keys())[0]
    pos2 = list(accending_sorted[1].keys())[0]
    pos3 = list(accending_sorted[2].keys())[0]

    if equal_distribution is not True:
        if accending_sorted[0][pos1] % 2 != 0:
            accending_sorted[0][pos1] += 1
            required_amounts[pos1] =  1
        else:
            required_amounts[pos1] =  0
        required_amounts[pos2] =  accending_sorted[0][pos1] + accending_sorted[0][pos1] - accending_sorted[1][pos2]
        required_amounts[pos3] = accending_sorted[1][pos2] + accending_sorted[0][pos1] + required_amounts[pos2] - accending_sorted[2][pos3]
        required_amounts['GK'] =  accending_sorted[0][pos1] - no_of_GK
    else:
        if accending_sorted[2][pos3] % 2 != 0:
            accending_sorted[2][pos3] += 1
            required_amounts[pos3] =  1
        else:
            required_amounts[pos3] =  0
        required_amounts[pos2] =  accending_sorted[2][pos3] - accending_sorted[1][pos2]
        required_amounts[pos1] = accending_sorted[2][pos3] - accending_sorted[0][pos1]
        required_amounts['GK'] = accending_sorted[2][pos3]/2 - no_of_GK
        
    return required_amounts

def check_for_the_right_formation(players):
    equally = check_for_ratio(players, True)
    not_equally = check_for_ratio(players)

    equally_sum = 0
    not_equally_sum = 0

    for i in equally:
        equally_sum += equally[i]

    for i in not_equally:
        not_equally_sum += not_equally[i]

    if not_equally_sum <= equally_sum:
        DEF = []
        MID = []
        STR = []
        GK = []

        for player in players:
            if player.more.playing_possition1 == "DEF":
                DEF.append(player)
            elif player.more.playing_possition1 == 'MID':
                MID.append(player)
            elif player.more.playing_possition1 == 'STR':
                STR.append(player)
            elif player.more.playing_possition1 == 'GK':
                GK.append(player)

        no_of_DEF = len(DEF)
        no_of_MID = len(MID)
        no_of_STR = len(STR)
        no_of_GK =  len(GK)

        position_numbers = [{
            "DEF": no_of_DEF},
            {"MID": no_of_MID},
            {"STR": no_of_STR}
    
            ]



        accending_sorted = _sort(position_numbers)

        if list(accending_sorted[0].keys())[0] == "DEF":
            D = 1
        elif list(accending_sorted[1].keys())[0] == "DEF":
            D = 2
        else:
            D=3

        if list(accending_sorted[0].keys())[0] == "MID":
            M = 1
        elif list(accending_sorted[1].keys())[0] == "MID":
            M = 2
        else:
            M = 3

        if list(accending_sorted[0].keys())[0] == "STR":
            S = 1
        elif list(accending_sorted[1].keys())[0] == "STR":
            S = 2
        else:
            S = 3

        
  
        return {"formation": [D,M,S] ,"required_numbers":not_equally}
    
    return {"formation": [2,2,2] ,"required_numbers":equally}









# def make_formation_layout(players):
#     DEF = []
#     MID = []
#     STR = []
#     GK = []

#     for player in players:
#         if player.position == "DEF":
#             DEF.append(player)
#         elif player.position == 'MID':
#             MID.append(player)
#         elif player.position == 'STR':
#             STR.append(player)
#         elif player.position == 'GK':
#             GK.append(player)

#     no_of_DEF = len(DEF)
#     no_of_MID = len(MID)
#     no_of_STR = len(STR)
#     no_of_GK =  len(GK)

#     no_of_games = len(players) // 14

#     extra_player_required = len(players) % 14
#     if extra_player_required > 0:
#         no_of_games += 1

#     #adding dummy player to all positions if needed
#     # if no_of_GK < 7:
#     #     for i in range(7 - no_of_GK):
#     #         dummy = Player(112, "GK")
#     #         GK.append(dummy)
#     #         players.append(dummy)

#     # if no_of_DEF < 7:
#     #     for i in range(7 - no_of_DEF):
#     #         dummy = Player(112, "DEF")
#     #         DEF.append(dummy)
#     #         players.append(dummy)

#     # if no_of_MID < 7:
#     #     for i in range(7 - no_of_MID):
#     #         dummy = Player(112, "MID")
#     #         MID.append(dummy)
#     #         players.append(dummy)

#     if no_of_STR < 7:
#         for i in range(7 - no_of_STR):
#             dummy = Player(112, "STR")
#             STR.append(dummy)
#             players.append(dummy)
    

#     no_of_games = len(players) // 14

#     extra_player_required = 14 - len(players) % 14
#     if extra_player_required > 0:
#         dumy_player = Player(1111, "ANY")
#         for i in range(extra_player_required):
#             players.append(dumy_player)
#         no_of_games += 1

    



    

#     print(extra_player_required)
#     print(no_of_games)
#     print(len(players) / 14)


#     # for i in players:
#     #     print(i.id)



# make_formation_layout(players)

    