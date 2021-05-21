# Install dependencies
def install (name):
  subprocess.call(['pip', 'install', name])

import discord
import os
import random
import subprocess
import wikipedia
from discord.ext import commands
from googletrans import Translator
from keep_alive import keep_alive
from PyDictionary import PyDictionary
install('googletrans==3.1.0a0')

# Initialize dependencies
client = commands.Bot(command_prefix = ".", help_command=None)
translator = Translator()
dictionary = PyDictionary()

# Activate bot
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))
    print("We're Golden!")

# Dead Chat Gif List
deadchatgif = [
  "https://tenor.com/view/dead-chat-gif-18800792",
  "https://tenor.com/view/googas-wet-wet-cat-dead-chat-dead-chat-xd-gif-20820186",
  "https://tenor.com/view/rip-chat-chat-dead-dead-chat-inactive-gif-18754855",
  "https://tenor.com/view/the-dancing-dorito-i-revive-this-chat-dance-gif-14308244",
  "https://tenor.com/view/chat-dead-gif-18627672",
  "https://tenor.com/view/dead-chat-xd-discord-cry-sad-gif-19674247",
  "https://tenor.com/view/cringe-dead-chat-kermit-wtf-gif-20484958",
  "https://tenor.com/view/chats-dead-dead-chat-gif-15061736",
  "https://tenor.com/view/chat-dead-gif-19569291",
  "https://tenor.com/view/dead-chat-dead-chat-xd-alohadance-gif-20439881",
  "https://tenor.com/view/damianek-dead-chat-gif-19862880",
  "https://tenor.com/view/dead-chat-african-black-guy-laughing-discord-gif-20391612",
  "https://tenor.com/view/wtf-dead-chat-cringe-discord-cry-gif-20805838",
  "https://tenor.com/view/dead-chat-gif-20589759",
  "https://tenor.com/view/dead-chat-dead-chat-wtf-dies-of-cringe-gif-20364592",
  "https://tenor.com/view/dead-chat-gif-20130964"
]

# 8 Ball Responses List
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

# Opinions list
opinions = [
    "My favourite",
    "Not the best",
    "Greatest of all time",
    "Completely ovverated",
    "I've seen better",
    "Simply exquisite",
    "Terrible",
    "Debateable",
    "Worst thing I've heard of today"]

# 8ball Command
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Calculator Command 
@client.command(alisases = ["calculate"])
async def calc(ctx, *, content):
  con = (content.translate({ord(" "): None}))
  x = "x"
  try:
    if x in con:
      con = con.replace(x,"*")
    result = eval(con)
    await ctx.send(f"```{content} = {str(result)}```")
  except ZeroDivisionError:
    await ctx.send("Sorry but you can't divide by zero ¯\_(ツ)_/¯")

# Calculator Help Command
@client.command(alises=["calch", "calculator_help"])
async def calchelp(ctx):
    embed = discord.Embed(
      title = "Calculator Command", 
      description = """**Calculate** : ``[.calc "number" "operation" "number"...]``\n\n**Operations** :\nAdditon : ``+``\nSubtraction : ``-``\nMultiplaction : ``x``\nDivision : ``/``\nExponentiation : ``**`` """, 
      color = discord.Colour.green())
    await ctx.send(embed=embed)

# Clear Command 
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit, member: discord.Member=None):
  await ctx.message.delete()
  msg = []
  try:
      limit = int(limit)
  except:
      return await ctx.send("Please pass in an integer as limit")
  if not member:
      await ctx.channel.purge(limit=limit)
      return await ctx.send(f"Purged {limit} messages", delete_after=3)
  async for m in ctx.channel.history():
      if len(msg) == limit:
          break
      if m.author == member:
          msg.append(m)
  await ctx.channel.delete_messages(msg)
  await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)

# Coin Flip Command 
@client.command(aliases=["flip"])
async def flip_coin(ctx):
  coin = ["```Heads```", "```Tails```"]
  await ctx.send(str(random.choice(coin))) 

# Dead Chat Gif Sender
@client.listen('on_message')
async def dead_chat(message):
  dead_chats = ["dead chat", "Dead chat", "DEAD CHAT", "Dead Chat"]
  already_sent = False
  if already_sent == False:
    for word in dead_chats:
      if word in message.content:
        already_sent = True 
        await message.channel.send(random.choice(deadchatgif))
  already_sent = False

# Dice Roll Command
@client.command(aliases=["roll"])
async def roll_dice(ctx):
  val = (random.randint(1, 6))
  await ctx.send(f"```{val}```")

# Dictionary Antonym Command
@client.command(aliases=["antonym", "opposite"])
async def ant(ctx, arg1):
    word = (str(arg1))
    sentence = (dictionary.antonym(word))
    embed = discord.Embed(
      title = f"{arg1}", 
      description = f"```{(str(sentence)[1:-1])}```", 
      color = discord.Colour.red())
    await ctx.send(embed=embed)

# Dictionary Help Command
@client.command(aliases=["dictionaryhelp"])
async def dicthelp(ctx):
    embed = discord.Embed(
      title = "Dictionary Commands", 
      description = """\n\n**Meaning** : ``[.mean "word"]``\n\n**Synonym** : ``[.syn "word"]``\n\n**Antonym** : ``[.ant "word"]``\n\n**Translate** : ``[.trans "language code" "message"]``""", 
      color = discord.Colour.red())
    await ctx.send(embed=embed)

# Dictionary Meaning Command
@client.command(aliases=["meaning", "define", "def"])
async def mean(ctx, arg1):
    word = (str(arg1))
    sentence = (dictionary.meaning(word))
    embed = discord.Embed(
      title = f"{arg1}", 
      description = f"```{sentence}```", 
      color = discord.Colour.red())
    await ctx.send(embed=embed)

# Dictionary Synonym Command
@client.command(aliases=["synonym", "like"])
async def syn(ctx, arg1):
    word = (str(arg1))
    sentence = (dictionary.synonym(word))
    sen = (str(sentence)[1:-1])
    embed = discord.Embed(
      title = f"{arg1}", 
      description = f"""```{sen}```""", 
      color = discord.Colour.red())
    await ctx.send(embed=embed)

# Dictionary Translate Command
@client.command(aliases=["translate", "trans"])
async def tra(ctx, lang, *, sentence):
  translation = translator.translate(sentence, dest=lang)
  embed = discord.Embed(
    title = f"({translation.src}) --> ({translation.dest})", 
    description = (f"```Original: {translation.origin} ({translation.src})\n\nTranslation: {translation.text} ({translation.dest})```"), 
  color = discord.Colour.red())
  await ctx.send(embed=embed)

# Hamburger Image Sender
@client.listen('on_message')
async def on_msg(message):
  substring = "hamburger"
  sub2 = "big mac"
  fullstring = message.content
  if substring in fullstring: 
    await message.channel.send(file=discord.File(r'hamburger.png'))
  if sub2 in fullstring: 
      await message.channel.send(file=discord.File(r'hamburger.png'))
        
# Help Command
@client.command(aliases=["h"])
async def help(ctx):
    embed = discord.Embed(
      title = "Command Help", 
      description = """**Ask my opinion ** : ``[.op "something"]``
      \n**Calculate some numbers** : ``[.calchelp]``
      \n**Consult the 8ball**  :  ``[.8ball "question"]``
      \n**Use a Dictionary** : ``[.dicthelp]``
      \n**Flip a coin**  :  ``[.flip]``
      \n**Random Number Generator** : ``[.rng "minimum" "maximum"]``
      \n**Roll a die** : ``[.roll]``
      \n**Send poll question**  :  ``[.poll "mentions" "topic"]``
      \n**Search anything on Wikipedia**  :  ``[.search "topic"]``
      \n**See the staff commands** : ``[.staffcommands]``""", 
      color = discord.Colour.blue())
    await ctx.send(embed=embed)

# Meow Deleter
@client.listen('on_message')
async def on_msg2(message):
  dalist = [736979328050659328, 658859052629098507]
  blocked_words = ["meow", "Meow", "MEOW"]
  if message.author.id in dalist:
    for word in blocked_words:
      if word in message.content:
        await message.delete()

# Opinion Command 
@client.command(aliases=["opinion"])
async def op(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(opinions)}')

# Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

# Poll Command
@client.command()
@commands.has_permissions(mention_everyone=True)
async def poll(ctx, mentions, *, message):
  emb = discord.Embed(title=f"{message}", 
  color = discord.Colour.green())
  msg=await ctx.channel.send(embed=emb)
  await msg.add_reaction("👍")
  await msg.add_reaction("👎")
  await message.delete()

# Random Number Generator 
@client.command(aliases=["rng"])
async def rand(ctx, minimum, maximum):
    min = (int(minimum))
    max = (int(maximum))
    num = random.randint(min, max)
    await ctx.send((str(num)))

# Wikipedia Search Command
@client.command(alisases = ["wiki"])
async def search(ctx, *, content):
  try:
    summary = wikipedia.summary(content, sentences=2)
    embed = discord.Embed(
      title = f"{content}", 
      description = f"""``{summary}``""", 
      color = discord.Colour.red())
    await ctx.send(embed=embed)
  except:
    await ctx.send("Try re-wording that.")

# Keep Bot Alive
keep_alive()
client.run(os.getenv('TOKEN'))
