def player_manager(players):
    if not players:
        return []
    players = players.split(", ")
    results = []
    for player in range(0, len(players) - 1, 2):
        updated_info = {}
        updated_info["player"] = players[player]
        updated_info["contact"] = int(players[player + 1])
        results.append(updated_info)

    return results


print(player_manager("John Doe, 8167238327, Jane Doe, 8163723827"))
print(player_manager(None))
print(player_manager(""))
