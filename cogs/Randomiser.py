import random
import datetime
import discord
from discord.ext import commands

team_channels1 = [1087523920225239050, 1087706381634777099, 1087706401662570518, 1087706550086414376, 1087706565538218024, 1087706586207756309, 1087706603408605236, 1087706620773011506, 1087706639014051892, 1087706655036284979, 1087706689769320488, 1087745779139096617, 1087745800718798939, 1087745820113244160, 1087745835254694009, 1087745853139189830, 1087745876786692116, 1087745901101068319, 1087745919639887973, 1087745935989276683, 1087746260892663818, 1087746276914909195, 1087746292735823922, 1087746307684323478, 1087746326650945536]
team_channels2 = [1087746430577422406, 1087746447174275154, 1087746464182182009, 1087746489268318268, 1087746515549827213, 1087747366565724200, 1087747381279334480, 1087747395208609964, 1087747410412961853, 1087747428091961535, 1087747443799642143, 1087747470789980182, 1087747485172248587, 1087747499000856707, 1087747516721795112, 1087747751032410203, 1087747764496126023, 1087747786113548349, 1087747799845707786, 1087747813649158214, 1087747828996132884, 1087747845060317306, 1087747859773935647, 1087747878568595638, 1087747898571235408]

class Randomiser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command()
    @commands.has_role(891732525091811399)
    async def make_teams(self, ctx, game_num, *players):
        player_list = list(players)
        half_len = len(player_list) // 2
        random.shuffle(player_list)
        list1 = player_list[:half_len]
        list2 = player_list[half_len:]

        teams1 = [list1[u:u+2] for u in range(0, len(list1), 2)]
        teams2 = [list2[k:k+2] for k in range(0, len(list2), 2)]

        embed1 = discord.Embed(title=f"Game __{game_num}__ Teams", color=0xffd600)
        embed2 = discord.Embed(title=f"Game __{game_num}__ Teams", color=0xffd600)

        for i1, team1 in enumerate(teams1):
            team_string = ' + '.join(team1)
            embed1.add_field(name=f'<#{team_channels1[i1]}>', value=f'{team_string}', inline=True)
        embed1.timestamp = datetime.datetime.now()

        for i2, team2 in enumerate(teams2):
            team_string = ' + '.join(team2)
            embed2.add_field(name=f'<#{team_channels2[i2]}>', value=f'{team_string}', inline=True)
        embed2.timestamp = datetime.datetime.now()
        
        await ctx.send(embeds=[embed1, embed2])

async def setup(bot):
    await bot.add_cog(Randomiser(bot))