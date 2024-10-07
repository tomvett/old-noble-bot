import sys
import traceback
import discord
from discord.ext import commands

TOKEN = ""

class NobleBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$', intents=discord.Intents(messages=True, message_content=True, guilds=True, invites=True, members=True, bans=True))
        self.initial_extensions = [
            'cogs.Help',
            'cogs.Invite',
            'cogs.Blacklist',
            'cogs.Lobbies',
            'cogs.Management',
            'cogs.Randomiser',
        ]

    async def setup_hook(self):
        print("Bot is starting")
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def on_command_error(self, ctx, exception) -> None:
        if hasattr(ctx, 'error_handled'):
            return
        if isinstance(exception, commands.MissingRequiredArgument):
            await ctx.send_help(ctx.command)
        elif isinstance(exception, commands.UserNotFound):
            embed=discord.Embed(description="The user provided does not exist!", color=0x030303)
            await ctx.send(embed=embed)
        elif isinstance(exception, commands.CommandOnCooldown):
            embed=discord.Embed(description="You are using commands too quickly, slow down!", color=0x030303)
            await ctx.send(embed=embed)
        elif isinstance(exception, commands.CommandInvokeError):
            embed=discord.Embed(description="The bot cannot send messages to this user.", color=0x030303)
            await ctx.send(embed=embed)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)

bot = NobleBot()
bot.run(TOKEN)