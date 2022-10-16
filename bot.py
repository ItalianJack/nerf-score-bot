import discord
import score_mgmt

bot = discord.Client()

@bot.event
async def on_ready():
    print('Bot ready')

@bot.event
async def on_message(message):
    
    if message.author == bot.user or not str(message.channel) == 'kill-count':
        return

    if message.content.startswith('$generate'):
        args = message.content.lower().split(' ')
        args.pop(0)
        score_mgmt.generateScoreSheet(message.guild.id,args)
        await message.channel.send('Score sheet generated for guild '+str(message.guild))

    if 'killed' in message.content.lower():
        score_mgmt.modifyScores(str(message.guild.id)+'_scores.txt',(message.content.lower().split(' ')[2]),'death',1)
        score_mgmt.modifyScores(str(message.guild.id)+'_scores.txt',(message.content.lower().split(' ')[0]),'kill',1)
        await message.channel.send('Kill of '+message.content.split(' ')[2]+' by '+message.content.split(' ')[0]+' successfully logged.')
        await message.channel.send("```"+str(score_mgmt.importScores(str(message.guild.id)+'_scores.txt'))+"```")
        
    if message.content.startswith('$scores'):
        await message.channel.send("```"+str(score_mgmt.importScores(str(message.guild.id)+'_scores.txt'))+"```")

    if message.content.startswith('$help'):
        await message.channel.send('\t\t---Help for NerfBot---\n\t$help - Show this list\n\t$scores - Show stored scores for current session\n\t$generate [name] [name]... - create new scoresheet for server\n\t[name] killed [name] - log kill and update scores accordingly')

    if message.content.startswith('$leaderboard'):
        await message.channel.send('Wip') 
        print(score_mgmt.sortPlace(score_mgmt.importScores(str(message.guild.id)+'_scores.txt')))


bot.run(open("bot_key.txt", "r").read())

