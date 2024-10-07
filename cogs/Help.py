import discord
from discord.ext import commands

class MyHelpCommand(commands.MinimalHelpCommand):
    #def __init__(self):
        #super().__init__(verify_checks=False)

    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)
        
    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error)
        channel = self.get_destination()
        await channel.send(embed=embed)

class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self
        
        self.bot.role_list_staff = [902656971138805787, 757574079145443378, 797443677449748482, 914201568721653780, 729700409509281793, 1087814453774520410]#div3staff, div2staff, 24/7staff, prachelper, div1staff, zerobuildstaff
        self.bot.role_list_admin = [902656971155599411, 757574077874438265, 938806881013628950, 854739386776289331, 891732525091811399, 1087814453799694540]#div3admin, div2admin, 24/7admin, pracadmin, div1admin, zerobuildadmin
        
    async def cog_unload(self):
        self.bot.help_command = self._original_help_command

    async def cog_check(self, ctx):
        return any(ctx.author.get_role(rid) for rid in self.bot.role_list_staff)


async def setup(bot):
    await bot.add_cog(Support(bot))