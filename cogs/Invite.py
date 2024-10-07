import sys
import traceback
import datetime
import discord
import asyncio
import csv
from discord.ext import commands

DIV3 = 902656971113644132
LOGS = 1090349569621119036

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #async def cog_check(self, ctx):
        #return any(ctx.author.get_role(rid) for rid in self.bot.role_list_admin)

    @commands.command()
    @commands.has_role(902656971155599411)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def create(self, ctx, user: discord.User, *, reason):
        link = await self.bot.get_guild(DIV3).text_channels[0].create_invite(max_age = 86400, max_uses = 1, unique = True)
        dmchannel = await ctx.message.author.create_dm()

        embed=discord.Embed(title="Command Successful", color=0x030303)
        embed.add_field(name="Invite Link", value=link, inline=False)
        embed.timestamp = datetime.datetime.now()
        await dmchannel.send(embed=embed)

        embed2 =discord.Embed(title="Invite Created", color=0x00FF00)
        embed2.add_field(name="Creator:", value=ctx.message.author.mention, inline=True)
        embed2.add_field(name="Reason:", value=reason, inline=True)
        embed2.add_field(name="For:", value=f"{user.mention} // ``{user.id}``", inline=False)
        embed2.add_field(name="Invite Link:", value=link, inline=False)
        embed2.timestamp = datetime.datetime.now()
        await self.bot.get_channel(LOGS).send(embed=embed2)

        await ctx.message.add_reaction("👍")

    @commands.command()
    @commands.has_any_role(902656971155599411, 854739386776289331)
    async def delete(self, ctx, invite: discord.Invite, *, reason):
        if invite.inviter == self.bot.get_user(1036704661253673041):
            await self.bot.delete_invite(invite)
            embed=discord.Embed(description=f"{invite} succesfully deleted!", color=0x030303)

            embed2 =discord.Embed(title="Invite Deleted", color=0xFF0000)
            embed2.add_field(name="Destroyer:", value=ctx.message.author.mention, inline=True)
            embed2.add_field(name="Reason:", value=reason, inline=True)
            embed2.add_field(name="Invite Link:", value=invite, inline=False)
            embed2.timestamp = datetime.datetime.now()
            await self.bot.get_channel(LOGS).send(embed=embed2)
        else:
            embed=discord.Embed(description="You are only able to delete invites created by this bot!", color=0x030303)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role(854739386776289331)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def win(self, ctx, users: commands.Greedy[discord.User]):
        embed=discord.Embed(description=f"In perfect conditions, all the invites will be sent out in **{len(users) * 0.5}** minutes", color=0x030303)
        await ctx.send(embed=embed)

        errors = []
        guild = self.bot.get_guild(DIV3)
        for user in users:
            await asyncio.sleep(30)
            link = await guild.text_channels[0].create_invite(max_age = 86400, max_uses = 1, unique = True)

            try:
                if guild.get_member(user.id) is None and ctx.guild.get_member(user.id) is not None:
                    embed1=discord.Embed(title="Division 3 Invite", description="Congratulations on winning one of our practice scrim matches!", color=0x030303)
                    embed1.add_field(name="Single use invite:", value=link, inline=True)
                    embed1.set_footer(text="This is an automated message sent from Noble Practice Scrims. Please contact an administrator if the invite link expires.")
                    await user.send(embed=embed1)

                    embed2=discord.Embed(title="Invite Created", color=0xFFD700)
                    embed2.add_field(name="Creator:", value=ctx.message.author.mention, inline=True)
                    embed2.add_field(name="Reason:", value="RANKED WINNER", inline=True)
                    embed2.add_field(name="For:", value=f"{user.mention} // ``{user.id}``", inline=False)
                    embed2.add_field(name="Invite Link:", value=link, inline=False)
                    embed2.timestamp = datetime.datetime.now()
                    await self.bot.get_channel(LOGS).send(embed=embed2)
                else:
                    errors.append(user.id)
            except discord.errors.Forbidden:
                errors.append(user.id)

        if errors:
            error_user = "\n".join(str(x) for x in errors)
            embed3=discord.Embed(title="ERROR!", description=f'The following users were unable to recieve an invite:\n``{error_user}``', color=0xFF0000).set_footer(text="These users are likely to already be in div3 or aren't in opens or have their DMs closed which means they don't get an invite")
            await ctx.send(embed=embed3)
        embed4=discord.Embed(description=f"**{len(users)-len(errors)}** users have successfully recieved their invites", color=0x030303)
        await ctx.send(embed=embed4)

    @commands.command()
    @commands.has_role(854739386776289331)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def level(self, ctx, user: discord.User):
        error = False
        guild = self.bot.get_guild(DIV3)
        link = await guild.text_channels[0].create_invite(max_age = 86400, max_uses = 1, unique = True)

        try:
            if guild.get_member(user.id) is None and ctx.guild.get_member(user.id) is not None:
                embed=discord.Embed(title="Division 3 Invite", description="Congratulations on winning one of our practice scrim matches!", color=0x030303)
                embed.add_field(name="Single use invite:", value=link, inline=True)
                embed.set_footer(text="This is an automated message sent from Noble Practice Scrims. Please contact an administrator if the invite link expires.")
                dmchannel = await user.create_dm()
                await dmchannel.send(embed=embed)

                embed1 =discord.Embed(title="Invite Created", color=0xFFD700)
                embed1.add_field(name="Creator:", value=ctx.message.author.mention, inline=True)
                embed1.add_field(name="Reason:", value="LEVEL20 OPENS", inline=True)
                embed1.add_field(name="For:", value=f"{user.mention} // ``{user.id}``", inline=False)
                embed1.add_field(name="Invite Link:", value=link, inline=False)
                embed1.timestamp = datetime.datetime.now()
                await self.bot.get_channel(LOGS).send(embed=embed1)
            else:
                error = True
        except discord.errors.Forbidden:
            error = True

        if error:
            embed2=discord.Embed(title="ERROR!", description=f'Unable to invite **{user.name}** (``{user.id}``)', color=0xFF0000).set_footer(text="This user is likely to already be in div3 or aren't in opens or have their DMs closed which means they don't get an invite")
            await ctx.send(embed=embed2)
        else:
            embed3=discord.Embed(description=f"Successfully sent the invite to **{user.name}**", color=0x030303)
            await ctx.send(embed=embed3)

    @commands.command()
    @commands.has_role(1090294582329229482)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def twitinv(self, ctx, uses):
        link = await self.bot.get_guild(DIV3).text_channels[0].create_invite(max_age = 10800, max_uses = uses, unique = True)
        dmchannel = await ctx.message.author.create_dm()

        embed=discord.Embed(title="Command Successful", color=0x030303)
        embed.add_field(name="Invite Link", value=link, inline=False)
        embed.timestamp = datetime.datetime.now()
        await dmchannel.send(embed=embed)

        embed2 =discord.Embed(title="Invite Created", color=0x00acee)
        embed2.add_field(name="Creator:", value=ctx.message.author.mention, inline=True)
        embed2.add_field(name="Reason:", value="TWITTER", inline=True)
        embed2.add_field(name="Uses:", value=uses, inline=False)
        embed2.add_field(name="Invite Link:", value=link, inline=False)
        embed2.timestamp = datetime.datetime.now()
        await self.bot.get_channel(LOGS).send(embed=embed2)

        await ctx.message.add_reaction("👍")

    @delete.error
    async def delete_error(self, ctx, error):
        if isinstance(error, commands.BadInviteArgument):
            ctx.error_handled = True
            embed=discord.Embed(description="The invite link provided does not exist!", color=0x030303)
            await ctx.send(embed=embed)
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


async def setup(bot):
    await bot.add_cog(Invite(bot))
