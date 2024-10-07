import sys
import traceback
import datetime
import csv
import discord
import typing
from discord.ext import commands

STAFF = [902656971138805787, 757574079145443378, 797443677449748482, 914201568721653780, 729700409509281793, 1087814453774520410]
ADMIN = [902656971155599411, 757574077874438265, 938806881013628950, 854739386776289331, 891732525091811399, 1087814453799694540]

class Blacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('noblebot/blacklist.csv', "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reversed(list(reader)):
                if row[1] == str(member.id):
                    if row[0] == "BLACKLIST":
                        await member.ban(reason="noblebot blacklisted member")

                        embed=discord.Embed(title="Blacklisted User Joined", color=0x030303)
                        embed.add_field(name="User:", value=f"{member.mention} // ``{member.id}``", inline=False)
                        embed.add_field(name="Server:", value=member.guild.name)
                        embed.timestamp = datetime.datetime.now()

                        await self.bot.get_channel(1090349569621119036).send("<@321703710596136961>", embed=embed)
                        break
                    else:
                        break

    @commands.command()
    @commands.has_any_role(*ADMIN)
    async def blacklist(self, ctx, user: discord.User, *, reason):
        for guild in self.bot.guilds:
            await guild.ban(user, reason="noblebot blacklist")

        with open('noblebot/blacklist.csv', "a", newline='') as csv_file:
             writer = csv.writer(csv_file)
             row = ["BLACKLIST", user.id, reason, ctx.author, datetime.date.today()]
             writer.writerow(row)

        embed=discord.Embed(description=f"Successfully blacklisted {user}", color=0xFF0000)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role(*ADMIN)
    async def unblacklist(self, ctx, user: discord.User, *, reason):
        for guild in self.bot.guilds:
            await guild.unban(user, reason="noblebot blacklist")

        with open('noblebot/blacklist.csv', "a", newline='') as csv_file:
             writer = csv.writer(csv_file)
             row = ["UNBLACKLIST", user.id, reason, ctx.author, datetime.date.today()]
             writer.writerow(row)

        embed=discord.Embed(description=f"Successfully unblacklisted {user}", color=0x00FF00)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_any_role(*STAFF)
    async def list(self, ctx, user: typing.Optional[discord.User] = None):
        if user is not None:
            flag = True
            blacklist = []
            with open('noblebot/blacklist.csv', "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                for row in reader:
                    if row:
                        if str(user.id) == row[1]:
                            blacklist.append([row[0], row[2], row[3], row[4]])#type, text, author, date
                            flag = False
                if flag == True:
                    embed=discord.Embed(description=f"{user} does not have any blacklists", color=0x030303)
                else:
                    embed=discord.Embed(title=f"Blacklists for {user} ({user.id})", color=0x030303)
                    for i in reversed(blacklist):
                        embed.add_field(name=i[0], value=f"**Moderator:** {i[2]}\n**Reason:** {i[1]} - {i[3]}", inline=False)
                await ctx.send(embed=embed)

    @blacklist.error
    async def blacklist_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            ctx.error_handled = True
            embed=discord.Embed(description="The bot does not have permission to blacklist that user!", color=0x030303)
            await ctx.send(embed=embed)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @unblacklist.error
    async def unblacklist_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            ctx.error_handled = True
            embed=discord.Embed(description="That user is not blacklisted!", color=0x030303)
            await ctx.send(embed=embed)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


async def setup(bot):
    await bot.add_cog(Blacklist(bot))