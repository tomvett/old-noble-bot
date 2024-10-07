import datetime
import discord
from discord.ext import commands, tasks

utc = datetime.timezone.utc
time = datetime.time(hour=10, minute=30, tzinfo=utc)

class Management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.autopurgeinvites.start()
    
    def cog_unload(self):
        self.autopurgeinvites.cancel()

    async def cog_check(self, ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command()
    @commands.has_role(854725918857101342)
    async def purgeinvites(self, ctx):
        deletes = 0
        for invite in await ctx.guild.invites():
            if invite.uses < 100:
                await invite.delete()
                deletes += 1
        await ctx.send(embed=discord.Embed(title=f"{deletes} invites successfully deleted!", color=0x030303))

    @tasks.loop(time=time)
    async def autopurgeinvites(self):
        deletes = 0
        for invite in await self.bot.get_guild(854725181384556584).invites():
            if invite.uses < 100:
                await invite.delete()
                deletes += 1
        await self.bot.get_channel(913887627789357056).send(embed=discord.Embed(title=f"**{deletes}** invites successfully deleted!", color=0x030303).set_footer(text="Automated daily invite purge @ 11:30am UTC"))


async def setup(bot):
    await bot.add_cog(Management(bot))