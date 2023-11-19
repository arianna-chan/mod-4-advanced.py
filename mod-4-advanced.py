def relationship_status(from_member="joaquin", to_member="chums", social_graph=None):
    if social_graph is None:
        social_graph = {
            "@bongolpoc": {"first_name": "Joselito", "last_name": "Olpoc", "following": []},
            "@joaquin": {"first_name": "Joaquin", "last_name": "Gonzales", "following": ["@chums", "@jobenilagan"]},
            "@chums": {"first_name": "Matthew", "last_name": "Uy",
                       "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]},
            "@jobenilagan": {"first_name": "Joben", "last_name": "Ilagan",
                             "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]},
            "@joeilagan": {"first_name": "Joe", "last_name": "Ilagan",
                            "following": ["@eeebeee", "@jobenilagan", "@chums"]},
            "@eeebeee": {"first_name": "Elizabeth", "last_name": "Ilagan",
                         "following": ["@jobenilagan", "@joeilagan"]}
        }

    if to_member in [user for user in social_graph if from_member in social_graph[user]["following"]]:
        if from_member in [user for user in social_graph if to_member in social_graph[user]["following"]]:
            return "friends"
        else:
            return "followed by"
    else:
        if from_member in [user for user in social_graph if to_member in social_graph[user]["following"]]:
            return "follower"
        else:
            return "no relationship"


def tic_tac_toe(board=None):
    if board is None:
        board = [
            ['X', 'X', 'O'],
            ['O', 'X', 'O'],
            ['X', '', 'O'],
        ]

    grid = len(board)
    for row in board:
        if len(set(row)) == 1:
            return f"{set(row).pop()} is the winner"

    if len(set([board[x][x] for x in range(grid)])) == 1:
        return f"{set([board[x][x] for x in range(grid)]).pop()} is the winner"

    if len(set([board[grid - 1 - y][y] for y in range(grid)])) == 1:
        return f"{set([board[y][y] for y in range(grid)]).pop()} is the winner"

    vertical_board = [z for z in zip(*board)]
    for column in vertical_board:
        if len(set(column)) == 1:
            return f"{set(column).pop()} is the winner"

    return "NO WINNER"


def eta(first_stop="upd", second_stop="admu", route_map=None):
    if route_map is None:
        route_map = {
            ("upd", "admu"): {"travel_time_mins": 10},
            ("admu", "dlsu"): {"travel_time_mins": 35},
            ("dlsu", "upd"): {"travel_time_mins": 55}
        }

    travel_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for leg, info in route_map.items():
            if leg[0] == current_stop:
                travel_time += info["travel_time_mins"]
                current_stop = leg[1]
                break

    return f"Estimated Time of Arrival: {travel_time} mins"


# Test the functions with the provided sample data
print(relationship_status("joaquin", "chums"))
print(tic_tac_toe([
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', 'O'],
]))
print(eta("upd", "admu"))
