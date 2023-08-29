import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set bot permissions
intents = discord.Intents.none()
intents.members = True
intents.guild_messages = True
intents.message_content = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.guild_reactions = True
intents.guild_typing = True
intents.messages = True
intents.reactions = True
intents.typing = True

# Set ! as the prefix for commands
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Ready the bot
@bot.event
async def on_ready():
    try:
        print("Synced commands")
    except Exception as e:
        print(e)

# Tell the server users what commands are available
@bot.command(name="help")
async def help(ctx):
    message = "```--Bot commands--\n!greeting: Greet a user with a random greeting.\n!happy: Sends words of encouragement.\n!dragon: Post a random picture of a dragon.\n/vent: Send a private vent message to the bot, and it will send private words of encouragement back. ```"

    await ctx.send(message)

# Send a random greeting with the "!greeting" command
@bot.command(name="greeting")
async def greet(ctx):
    greetings = ["Hello", "Hi", "Howdy", "Top of the mornin' to ya", "Greetings", "Yo"]

    await ctx.send(f"{random.choice(greetings)} {ctx.author}!", ephemeral=False)

# Sent words of encouragement
@bot.command(name="happy")
async def happy(ctx):
    encouragement = ["Everything gets easier with time.", "I know you can pull through!", "You're wonderful and strong", "We're all here for you", 
            "Time heals everything, you can make it!", "I love you ❤️", "We all love you!!"]

    await ctx.send(random.choice(encouragement))

# Send words of encouragement after a user vents using "/vent"
# This message will only be visible to the user who sent the command
@bot.tree.command(name="vent")
async def vent(interaction: discord.Interaction, args: str):
    sympathy = ["I hope things get better soon", "I know you can pull through", "you're strong and will get through this", "we're all here for you", 
            "time heals everything, you can make it"]
    
    await interaction.response.send_message(f"I'm sorry {interaction.user.mention}, {random.choice(sympathy)}!", ephemeral=True)

# Send a random picture of a
@bot.command(name="dragon")
async def dragon(ctx):

    dragon = ["https://static.wikia.nocookie.net/shrek/images/1/19/Dragon_Forever_After_transparent.png/revision/latest?cb=20210624203030", 
          "https://i.pinimg.com/550x/d7/67/e5/d767e5cb6e86ec741149cb373b0e16d8.jpg",
          "https://static1.cbrimages.com/wordpress/wp-content/uploads/2022/05/Mulan--Mushu-grin-1400.jpg",
          "https://i.pinimg.com/236x/89/76/52/897652e527b8e8f3cad925d532bf73d1--dragon-costume-funny-horses.jpg",
          "https://i.pinimg.com/736x/2c/18/e3/2c18e3bc7ec682b89265b9dde3322629--maleficent-dragon-disney-sleeping-beauty.jpg",
          "https://i.pinimg.com/236x/69/6a/a9/696aa9b94c967e8d4daa5d85d410f266.jpg"]

    await ctx.send(random.choice(dragon))

bot.run(TOKEN)