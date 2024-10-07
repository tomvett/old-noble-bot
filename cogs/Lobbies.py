import sys
import traceback
import discord
from discord.ext import commands

CLOSED_STAFF = [943570529581953065, 757574079145443378, 797443677449748482, 1087814453774520410]

class Lobbies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(*CLOSED_STAFF)
    async def lobby(self, ctx, num):
        num_splits = 6
        if ctx.guild.id == 902656971113644132: #div3
            splits=discord.Embed(description=f"**{num_splits}** Double contested spots max, `Apply Drop/Splits Template` & Select the available Drop/Split.\n\nDownload the **Yunite Client** to track points, https://yunite.xyz/client", color=0x0067ee).set_image(url="https://media.discordapp.net/attachments/934924778622550076/936003208600485888/unknown.png")
            lb=discord.Embed(title="Where's the Leaderboard?", description="The live leaderboard to every session is available on the dropmap website for your session.\nLook for **'Click To Access Yunite Leaderboard'** on the left of the screen.\n\n> Alternatively, view the leaderboard on [Fortnite Tracker](https://fortnitetracker.com/play)", color=0x0067ee).set_image(url="https://media.discordapp.net/attachments/934924778622550076/1060619700582752276/image.png")
            fills=discord.Embed(title="Want to fill in a session?", description="If we need additional teams to participate in this session we will open this channel up. Please **DO NOT DM STAFF** as they will tag everyone and ask for someone to fill when needed.", color=0x0067ee).set_thumbnail(url="https://media.discordapp.net/attachments/934851845661270127/936000501898706964/div3_hq_no_bg.png")
            unreg=discord.Embed(title="Why can't I unreg anymore?", description="**If you sign up for a session, you'll have to play all games out!**\nYou must unreg 15 minutes before the games start and after that you'll have to play all games out to not get banned.\n\nIf you cannot play because of a factor out of your control, you can message staff to see if they can unreg you.\n", color=0x0067ee).set_thumbnail(url="https://media.discordapp.net/attachments/934851845661270127/936000501898706964/div3_hq_no_bg.png")
            rules=discord.Embed(title="Noble Division 3 Rules", description="**Custom Game Rules**\n\n**Early Game**\n• You can fight off spawn if you are contested.\n• If you are uncontested you cannot go to another poi and fight them for surge. (AR tags outside the poi are allowed)\n\n**Mid Game**\n• No fighting after spawn fights - This includes:\n> Boxfights\n> Pushing headshot snipes the other side of the map\n> Pushing players because they are solo/duo\n> Camping on a chest\n• **AR tags for surge are allowed at all times**\n\n**Below Surge?**\n• You can boxfight players if you are below surge and surge is about to be active.\n\n**General Rules**\n• Tweeting or complaining about dumb shit like having to move spots or getting banned\n• No leaking keys\n• No Streamsniping\n• No teaming\n• Take the practice serious for your benefit and everyone else's.", color=0x0067ee).set_thumbnail(url="https://media.discordapp.net/attachments/934851845661270127/936000501898706964/div3_hq_no_bg.png")
            reaction = "<:div3:936738590753456199>"
        elif ctx.guild.id == 757573638995050608: #div2
            splits=discord.Embed(description=f"**{num_splits}** Double contested spots max, `Apply Drop/Splits Template` & Select the available Drop/Split.\n\nDownload the **Yunite Client** to track points, https://yunite.xyz/client", color=0x00ef19).set_image(url="https://media.discordapp.net/attachments/934924778622550076/936003208600485888/unknown.png")
            lb=discord.Embed(title="Where's the Leaderboard?", description="The live leaderboard to every session is available on the dropmap website for your session.\nLook for **'Click To Access Yunite Leaderboard'** on the left of the screen.\n\n> Alternatively, view the leaderboard on [Fortnite Tracker](https://fortnitetracker.com/play)", color=0x00ef19).set_image(url="https://media.discordapp.net/attachments/1040790329827282954/1061769870905200721/image.png")
            fills=discord.Embed(title="Want to fill in a session?", description="If we need additional teams to participate in this session we will open this channel up. Please **DO NOT DM STAFF** as they will tag everyone and ask for someone to fill when needed.", color=0x00ef19).set_thumbnail(url="https://cdn.discordapp.com/attachments/757574096254140569/1022985910696038450/Layer_1.png")
            unreg=discord.Embed(title="Why can't I unreg anymore?", description="**If you sign up for a session, you'll have to play all games out!**\nYou must unreg 15 minutes before the games start and after that you'll have to play all games out to not get banned.\n\nIf you cannot play because of a factor out of your control, you can message staff to see if they can unreg you.\n", color=0x00ef19).set_thumbnail(url="https://cdn.discordapp.com/attachments/757574096254140569/1022985910696038450/Layer_1.png")
            rules=discord.Embed(title="Noble Division 2 Rules", description="**Custom Game Rules**\n\n**Early Game**\n• You can fight off spawn if you are contested.\n• If you are uncontested you cannot go to another poi and fight them for surge. (AR tags outside the poi are allowed)\n\n**Mid Game**\n• No fighting after spawn fights - This includes:\n> Boxfights\n> Pushing headshot snipes the other side of the map\n> Pushing players because they are solo/duo\n> Camping on a chest\n• **AR tags for surge are allowed at all times**\n\n**Below Surge?**\n• You can boxfight players if you are below surge and surge is about to be active.\n\n**General Rules**\n• Tweeting or complaining about dumb shit like having to move spots or getting banned\n• No leaking keys\n• No Streamsniping\n• No teaming\n• Take the practice serious for your benefit and everyone else's.", color=0x00ef19).set_thumbnail(url="https://cdn.discordapp.com/attachments/757574096254140569/1022985910696038450/Layer_1.png")
            reaction = "<:div2:1022985780383195157>"
        elif ctx.guild.id == 797443677403217940: #24/7
            splits=discord.Embed(description=f"**{num_splits}** Double contested spots max, `Apply Drop/Splits Template` & Select the available Drop/Split.\n\nDownload the **Yunite Client** to track points, https://yunite.xyz/client", color=0xf6b501).set_image(url="https://media.discordapp.net/attachments/934924778622550076/936003208600485888/unknown.png")
            lb=discord.Embed(title="Where's the Leaderboard?", description="The live leaderboard to every session is available on the dropmap website for your session.\nLook for **'Click To Access Yunite Leaderboard'** on the left of the screen.\n\n> Alternatively, view the leaderboard on [Fortnite Tracker](https://fortnitetracker.com/play)", color=0xf6b501).set_image(url="https://media.discordapp.net/attachments/1040788149141516378/1061773919763304518/zxW1yZM.png")
            fills=discord.Embed(title="Want to fill in a session?", description="If we need additional teams to participate in this session we will open this channel up. Please **DO NOT DM STAFF** as they will tag everyone and ask for someone to fill when needed.", color=0xf6b501).set_thumbnail(url="https://cdn.discordapp.com/attachments/1040788149141516378/1061773652753907743/247.png")
            unreg=discord.Embed(title="Why can't I unreg anymore?", description="**If you sign up for a session, you'll have to play all games out!**\nYou must unreg 15 minutes before the games start and after that you'll have to play all games out to not get banned.\n\nIf you cannot play because of a factor out of your control, you can message staff to see if they can unreg you.\n", color=0xf6b501).set_thumbnail(url="https://cdn.discordapp.com/attachments/1040788149141516378/1061773652753907743/247.png")
            rules=discord.Embed(title="Noble 24/7 Rules", description="**Custom Game Rules**\n\n**Early Game**\n• You can fight off spawn if you are contested.\n• If you are uncontested you cannot go to another poi and fight them for surge. (AR tags outside the poi are allowed)\n\n**Mid Game**\n• No fighting after spawn fights - This includes:\n> Boxfights\n> Pushing headshot snipes the other side of the map\n> Pushing players because they are solo/duo\n> Camping on a chest\n• **AR tags for surge are allowed at all times**\n\n**Below Surge?**\n• You can boxfight players if you are below surge and surge is about to be active.\n\n**General Rules**\n• Tweeting or complaining about dumb shit like having to move spots or getting banned\n• No leaking keys\n• No Streamsniping\n• No teaming\n• Take the practice serious for your benefit and everyone else's.", color=0xf6b501).set_thumbnail(url="https://cdn.discordapp.com/attachments/1040788149141516378/1061773652753907743/247.png")
            reaction = "<:247:1061772154225573959>"
        elif ctx.guild.id == 1087814453740974131: #zerobuild
            splits=discord.Embed(description=f"**{num_splits}** Double contested spots max, `Apply Drop/Splits Template` & Select the available Drop/Split.\n\nDownload the **Yunite Client** to track points, https://yunite.xyz/client", color=0x21ddf1).set_image(url="https://media.discordapp.net/attachments/934924778622550076/936003208600485888/unknown.png")
            lb=discord.Embed(title="Where's the Leaderboard?", description="The live leaderboard to every session is available on the dropmap website for your session.\nLook for **'Click To Access Yunite Leaderboard'** on the left of the screen.\n\n> Alternatively, view the leaderboard on [Fortnite Tracker](https://fortnitetracker.com/play)", color=0x21ddf1).set_image(url="https://media.discordapp.net/attachments/1088172102529593459/1089528426794328094/image.png")
            fills=discord.Embed(title="Want to fill in a session?", description="If we need additional teams to participate in this session we will open this channel up. Please **DO NOT DM STAFF** as they will tag everyone and ask for someone to fill when needed.", color=0x21ddf1).set_thumbnail(url="https://media.discordapp.net/attachments/1088172102529593459/1088581425361604650/output-onlinepngtools.png?width=811&height=676")
            unreg=discord.Embed(title="Why can't I unreg anymore?", description="**If you sign up for a session, you'll have to play all games out!**\nYou must unreg 15 minutes before the games start and after that you'll have to play all games out to not get banned.\n\nIf you cannot play because of a factor out of your control, you can message staff to see if they can unreg you.\n", color=0x21ddf1).set_thumbnail(url="https://media.discordapp.net/attachments/1088172102529593459/1088581425361604650/output-onlinepngtools.png?width=811&height=676")
            rules=discord.Embed(title="Noble Zero Build Rules", description="> As this is a new server, the rules are constantly changing. You are required to read <#1087814454772772998> __before each session__ to ensure you have seen the latest **rules** and **banned items**.", color=0x21ddf1).set_thumbnail(url="https://media.discordapp.net/attachments/1088172102529593459/1088581425361604650/output-onlinepngtools.png?width=811&height=676")
            reaction = "<:noble_zero_build:1088772152737677392>"

        messages = [[f"lobby-{num}-dropmap", splits], [f"lobby-{num}-chat", lb], [f"lobby-{num}-fill-requests", fills], [f"lobby-{num}-getting-off", unreg], [f"lobby-{num}-code", rules]]
        
        for preset in messages:
            channel = discord.utils.get(ctx.guild.text_channels, name=preset[0])
            msg = await channel.send(embed=preset[1])
        await msg.add_reaction(reaction) 

        embed=discord.Embed(description=f"Presets have been posted in the lobby channels", color=0x030303)
        await ctx.send(embed=embed)

    @lobby.error
    async def lobby_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            ctx.error_handled = True
            embed=discord.Embed(description="The lobby number you entered doesn't exist! No messages were posted.", color=0x030303)
            await ctx.send(embed=embed)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


async def setup(bot):
    await bot.add_cog(Lobbies(bot))