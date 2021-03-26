import discord
import random
from discord.ext import commands
from PyDictionary import PyDictionary

dictionary=PyDictionary()

client = commands.Bot(command_prefix = ".", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Definitely not what .Popple is playing'))
    print("We're Golden!")

@client.listen('on_message')
async def on_msg(message):
    substring = "hamburger"
    sub2 = "big mac"
    fullstring = message.content
    if substring in fullstring: 
        await message.channel.send(file=discord.File(r'hamburger.png'))
    if sub2 in fullstring: 
        await message.channel.send(file=discord.File(r'hamburger.png'))

@client.event
async def on_member_remove(memeber):
    channel = member.get.channel
    await message.channel.send(f"Goodbye my dearest {memeber}!")

@client.event
async def on_member_leave(memeber):
    channel = member.get.channel
    await message.channel.send(f"Good morrow my dearest {memeber}!")


# Calcualator
@client.command(alisases = ["calculate"])
async def calc(ctx, arg1, op, arg2):
    if op == "x":
        ans = (int(arg1)) * (int(arg2))
        await ctx.send(f"{(str(arg1))} {(str(op))} {(str(arg2))} = {(str(ans))}")
    if op == "/": 
        ans = (int(arg1))/(int(arg2))
        await ctx.send(f"{(str(arg1))} {(str(op))} {(str(arg2))} = {(str(ans))}")
    if op == "+":
        ans = (int(arg1)) + (int(arg2))
        await ctx.send(f"{(str(arg1))} {(str(op))} {(str(arg2))} = {(str(ans))}")
    if op == "-":
        ans = (int(arg1)) - (int(arg2))
        await ctx.send(f"{(str(arg1))} {(str(op))} {(str(arg2))} = {(str(ans))}")
    if op == "^":
        ans = (int(arg1)) ** (int(arg2))
        await ctx.send(f"{(str(arg1))} {(str(op))} {(str(arg2))} = {(str(ans))}")
# Calculator 

@client.command()
async def poll(ctx, *, message):
    emb=discord.Embed(title="DEMOCRACY TIME!🥳", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
        
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
@commands.has_permissions(administrator=True)
async def admintest(ctx):
    await ctx.send("Only admins can do this!")

@client.command(aliases=["assistance", "commands", "h"])
async def help(ctx):
    await ctx.send("```Check your ping - [.ping]\n\nStart a poll - [.poll (Topic)]\n\nCalculate something [.calc (fisrt number) (operation) (second number)] | [.calc help for operations]\n\nAsk my opinion on something - [.op (question)]\n\nConsult the 8ball - [.8ball (question)]\n\nDictionary - [.dicthelp]```")

@client.command(aliases=["dictionaryhelp"])
async def dicthelp(ctx):
    await ctx.send("""```Dictionary Commands:\n\nMeaning | [.mean "word"]\n\nSynonym | [.syn "word"]\n\nAntonym | [.ant "word]\n\nTranslate | [.translate "word" "laguage(eg. "en", "fr")]```""")

@client.command(alises=["calch", "calculator_help"])
async def calchelp(ctx):
    await ctx.send("```Operations:\n\nAdditon | +\n\nSubtration | -\n\nMultiplaction | x\n\nDivision | /```")


responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    
opinions = [
    "Oh I hate that",
    "Could live without it"
    "Not very cool",
    "Amazing",
    "Are you kidding me, of course I love them",
    "Now that YOU say it, it sounds bad",
    "tbh idc about em",
    "Don't ask me that",
    "idfk lol",
    "lit",
    "My favourite"]

@client.command(aliases=["opinion"])
async def op(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(opinions)}')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=["meaning", "define", "def"])
async def mean(ctx, arg1):
    word = (str(arg1))
    sentence = (dictionary.meaning(word))
    await ctx.send((f"```{sentence}```"))
    
@client.command(aliases=["synonym", "like"])
async def syn(ctx, arg1):
    word = (str(arg1))
    sentence = (dictionary.synonym(word))
    await ctx.send((f"```{sentence}```"))

@client.command(aliases=["translate", "trans"])
async def tra(ctx, arg1, lang):
    word = (str(arg1))
    language = (str(lang))
    sentence = (dictionary.translate(word, lang))
    await ctx.send((f"```{sentence}```"))

@client.command(aliases=["antonym", "opposite"])
async def ant(ctx, arg1):
    word = (str(arg1))
    sentence = (dictionary.antonym(word))
    await ctx.send((f"```{sentence}```"))

#@client.event
#async def on_message(message):
#    if message.author.id == 658859052629098507: 
#        client.msg_var = message.content  
#        await message.channel.send(message.content[::-1])

token = 'ODI0NjYxNDAzMjI2NjAzNTgw.YFynxw.CbFCqgYYjXISx5PD755PNo5hTB0'
client.run(token)

@client.command(aliases=["youtube"])
async def yt(ctx):
    await ctx.send("https://www.youtube.com/channel/UCq4OAL6WbXm9ltmIHorzGUA")

@client.command(aliases=["twt"])
async def twitter(ctx):
    await ctx.send("https://twitter.com/alphatazlol")

@client.command(aliases=["rdt"])
async def reddit(ctx):
    await ctx.send("https://www.reddit.com/r/alphataz/")
