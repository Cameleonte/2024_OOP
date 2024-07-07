from project.player import Player

from project.guild import Guild

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
player1 = Player('Ristio', 1000, 1000)
player2 = Player('Prycko', 50, 50)
print(player1.add_skill('Iako pyrdene', 100))
print(player2.add_skill('pii bira', 30))
print(player1.player_info())
print(player2.player_info())
guild = Guild("Biren korem")
guild1 = Guild('pi4 ta drynka')
print(guild.assign_player(player1))
print(guild.assign_player(player2))
print(guild1.kick_player('Ristio'))
print(guild.kick_player('Ristio'))
print(guild.guild_info())
