import discord
import random
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.typing = False
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Coded by Blue"))
@bot.slash_command(description="Sends the bot's latency.")
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=f"Latency is {bot.latency}",
        color=0x3498db
    )

    await ctx.respond(embed=embed)


@bot.slash_command(description="Flips a Coin")
async def flip(ctx):
    def flip_coin():
        return random.choice(['Heads', 'Tails'])


    result = flip_coin()
    embed = discord.Embed(
        title="Fliped",
        description=f"The coin landed on: {result}",
        color=0x3498db
    )


    embed.set_image(url="https://media.giphy.com/media/V57jUkC3eZFsym7iwE/giphy.gif")

    await ctx.respond(embed=embed)


@bot.slash_command(description="Sends the Link to my Website")
async def website(ctx):
    await ctx.respond("https://blueofphoenix.github.io/me/")

@bot.slash_command(description="Sends the Link to my GitHub")
async def github(ctx):
    await ctx.respond("https://github.com/BlueofPhoenix")

@bot.slash_command(description="Sends Infos about the Bot")
async def help(ctx):
    Blue = await bot.fetch_user(1121889187440889897)
    embed = discord.Embed(
        title="About BBot",
        description=f"Funfact BBot was made by {Blue.mention}",
        color=0x3498db
    )


    embed.add_field(name="Help", value="Its the Command you just used .", inline=True)
    embed.add_field(name="Flip", value="The /flip command flips a Coin.", inline=True)
    embed.add_field(name="Ping", value="The /Ping command sends the current latency of BBot", inline=True)
    embed.add_field(name="Website", value="The /Website command sends my Website in the Channel", inline=True)
    embed.add_field(name="GitHub", value="The /GitHub command sends my GitHub Page in the Channel", inline=True)



    embed.set_image(url="https://i.postimg.cc/wxSX6xZ9/Logo-Discord.webp")
    await ctx.respond(embed = embed)

@bot.slash_command(description="Nicks you")
async def nick(ctx, *, new_nickname: str):
    try:
        await ctx.author.edit(nick=new_nickname)
        await ctx.send(f"Nickname changed to {new_nickname} successfully!")
    except discord.Forbidden:
        await ctx.send("I don't have permission to change your nickname.")


@bot.event
async def on_member_join(member):
                            #Under me is the welcome Channel id
    welcome_channel = bot.get_channel(1163571160072585267)

    if welcome_channel:

        welcome_message = f"Welcome to the server, {member.mention}!"
        await welcome_channel.send(welcome_message)



bot.run("Your Token witout "". ")