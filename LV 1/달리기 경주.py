def solution(players, callings):
    rank_players = dict()
    players_rank = dict()
    
    for idx, p in enumerate(players):
        players_rank[p] = idx+1
        rank_players[idx+1] = p
    
    for name in callings:
        rank = players_rank[name]
        switch_player = rank_players[rank-1]
        
        rank_players[rank-1], rank_players[rank] = name, switch_player
        players_rank[name], players_rank[switch_player] = rank-1, rank
        
    return list(rank_players.values())