import os
import discord
from dotenv import load_dotenv
import random
import tkinter as tk
import threading as thr

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents=discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
        status.config(text="Bot is online!")


@client.event
async def on_message(message):
    lastreponse = ()
    if message.author == client.user:
        return

    grumpybedtime = [
        "https://starmoon.neocities.org/files/dacomic1.png https://starmoon.neocities.org/files/dacomic2.png", 
        "https://starmoon.neocities.org/files/gb/gb.mp4"
        ]

    jj = ["AUUUUUUUAUAUAUUUU", "Fucker", "<:evildog:1033952582957285377>", "OKAY????", "THE DOGS WILL EXPLODE?", 
          "in gym class once we were doing the macarena and when we were done i said “one maca two maca three macaroni!” and my teacher looked at me seriously and said “in this classroom, we do not mock other people’s cultures.”", 
          "https://starmoon.neocities.org/files/awesomebot/stardusty.jpg","CARE BEARS PLUSH ASS"]

    mimi = ["SO TRUUUUEE", "TRUE", "https://cdn.discordapp.com/attachments/1068764169618329631/1080164534846758922/94BD1BAD-35FD-4490-9EF1-A932AA39BBF4.jpg", "<:weeping:1061527391568154644>"]

    rocket = ["HELP", "🧡", "https://cdn.discordapp.com/attachments/1032727599501283419/1076924951111675934/IMG_4785.gif", "OUGGHGGGHHHH SO TRUUE"]

    zack = [":!;$/$/$/$:$/&&/&:", "I need to be by the dogs jj otherwise they will explode", "Dhfjdjdjdjsjsjs", "❤️❤️❤️"]

    ana = ["ong", "jj can we call", "gay gay gay gay", "My fellow Americans, I am here to decree that JJStarz, of Care Bear fandom fame, is, in fact, gay.", ]

    cb = ["So what kind of clothes does tenderheart bear grumpy bear funshine bear good luck bear share bear wish bear bedtime bear friend bear harmony bear swift heart rabbit playful heart monkey perfect panda polite panda gentle heart lamb proud heart cat loyal heart dog brave heart lion lotsa heart elephant wore clothes before join care bear team (with champ cheer treat heart bright heart) a vest & jacket & cap & more",
        "Don't mind the deleted stuff ^^;\nI've dropped from the whole carebear community drama and finally moved on from it.\nRather not have old memories remind me.",
        "Here is Good Luck with an ArmaLite AR-18 \nhttps://cdn.discordapp.com/attachments/430720562906791946/781162807295082536/but_all_the_time-1.png",
    "https://cdn.discordapp.com/attachments/430720562906791946/780777211195686932/gl_gun.png \nWho gave Good Luck an ArmaLite AR-18",
    "Grumpy is se-i means cute", 
'"The device is almost complete." Said Grumpy.\nWingnut agreed with Grumpy.\nHe nodded to show it.\n"Glad You agree, Wingnut." Replied Grumpy.',
    "GRRRRRRRRRRVERYTIMEYOUREAROUNDMYANKLEGETSHURTDOYOUHATEANKLEAOROSMEHTIFJHAUHAUAH",
    "@CareBearsRock Well Her Belly Back And Feet!","Well I'm Sorry Well Cozy Heart Is Dirty After A Caring Misson!","Well I Change My Message And It's About Cozy Heart To Finally Getting A Girl Friend!",
    "\*PLOOMPH\*","(FUCKBALLS)","Treat Heart had a funny look on her face. You really don t thin fat ass ? she said in a surprised tone of voice.",
    "https://starmoon.neocities.org/files/awesomebot/carlita.png","https://starmoon.neocities.org/files/awesomebot/cheer.jpg",
    "https://starmoon.neocities.org/files/awesomebot/dibble.jpg","https://starmoon.neocities.org/files/awesomebot/nicholas.jpg"]

    danmou = ["https://starmoon.neocities.org/files/awesomebot/pavilion.jpg","https://starmoon.neocities.org/files/awesomebot/silent.jpg"]

    calr = ["Okay, congrats for making Beastly tolerable to look at.","I can only imagine\n \nGrumpy:... Baby lock them doors and turn dem lights down low..",
            "Heh, as dumb as he is, it was pretty clever of him to say he didn't have ONE bear...as in, he caught two bears",
            '"Uncle No-Heart, do you have any advice on how to deal with someone who loves you, despite presenting clear signs that you are a misbegotten demoness?"',
            "https://cdn.discordapp.com/attachments/1062227673050525747/1074471370261536808/IMG_4752.png",
            "If anyone tells you that toys are only for kids, the queue in Build A Bear yesterday was only teens and young adults, so, no, it's not just for kids, enjoy whatever the fuck you want :)",
            "Dude what if Kim Jong Un was a furry and that's why artists over there keep disappearing so the truth doesn't come out/constant stream of furry art",
            "I really don’t like Shreeky. I mean, she’s a villain and she’s meant to be disliked to some extent, but she’s just overexposed in favor of No Heart himself",
            "I hate Streaky SO MUCH\nSteak\nShrieky",
            "I dont like shreeky oersinally","Shreeky is a lil' shit","I HATE SHREEKY AAAAAAAAAAAAAAAAAAAAAA",
            ""]

    utm = ["And also how UTM era is trying to follow trends and how it has become too girly (in my opinion)",
           "as for writing, i see a progression, but this is all my opinion tho \n \naical season 1 was written pretty well, season 2 was meh  \n \nwtcal was meh, there were a few episodes that legit pissed me off slightly \n \ncare bears and cousins was written badly \n \nutm has 0 effort in the writing except the first few episodes",
           "Utm is just such bollocks imo i just. Its because cloudco play to the oversimplification DISEASE","The og utm style is so corporate",
           "You cant save utm just throw the whole thing away","Whiffles are annoying bad crowd are mediocre depthless villains",
           "then there is also how dibble keeps fucking up grumpy's life even when she's told to stop, but when grumpy says anything about it, he's in the wrong"]
    lps = ["MY OTP IS NOW REAL! MINKA DRAW ART NOW!", '"Ack-cckkk...!" I sputtered. "I see...the light!"',"SUNIL IS SICK",
           "https://tenor.com/view/lps-lps2012-sunil-nevla-pepper-clark-gif-26695871","Why can't she hear us talking, Russell?", 
           "Russell, why can't she hear us speak?", "I'M NOT A HUMANARIAN! I AM... AN ANIMAL!!!",
           'When Pepper sings "She came to hear us talking but instead of a song…", her voice sounds a lot higher than usual.'
           "I know. Pepper's the best lookin'."]

    for n in range(1,63):
        grumpybedtime.append(f"https://starmoon.neocities.org/files/gb/{n}.jpg")
    if message.content == 'grumpy bedtime':
        while True:
            response = random.choice(grumpybedtime)
            if response == lastreponse:
                response = random.choice(grumpybedtime)
            else:
                await message.channel.send(response)
                lastreponse = response
                break
    if message.content == 'JJ' or message.content == 'jj':
        while True:
            response = random.choice(jj)
            if response == lastreponse:
                response = random.choice(jj)
            else:
                await message.channel.send(response)
                lastreponse = response
                break
    if message.content == 'MIMI' or message.content == 'mimi':
        while True:
            response = random.choice(mimi)
            if response == lastreponse:
                response = random.choice(mimi)
            else:
                await message.channel.send(response)
                lastreponse = response
                break
    if message.content == 'ZACK' or message.content == 'zack':
        while True:
            response = random.choice(zack)
            if response == lastreponse:
                response = random.choice(zack)
            else:
                await message.channel.send(response)
                lastreponse = response
                break
    if message.content == 'ROCKET' or message.content == 'rocket':
        while True:
            response = random.choice(rocket)
            if response == lastreponse:
                response = random.choice(rocket)
            else:
                await message.channel.send(response)
                lastreponse = response
                break

    if message.content == 'ANA' or message.content == 'ana':
        while True:
            response = random.choice(ana)
            if response == lastreponse:
                response = random.choice(ana)
            else:
                await message.channel.send(response)
                lastreponse = response
                break

    if 'care bears' in message.content or 'CARE BEARS' in message.content:
        while True:
            response = random.choice(cb)
            if response == lastreponse:
                response = random.choice(cb)
            else:
                await message.channel.send(response)
                lastreponse = response
                break
    if 'danger mouse' in message.content or 'DANGER MOUSE' in message.content:
        while True:
            response = random.choice(danmou)
            if response == lastreponse:
                response = random.choice(danmou)
            else:
                await message.channel.send(response)
                lastreponse = response
                break
    if 'CALR' in message.content or 'calr' in message.content:
        while True:
            response = random.choice(calr)
            if response == lastreponse:
                response = random.choice(calr)
            else:
                await message.channel.send(response)
                lastreponse = response
                break

    if 'UTM' in message.content or 'utm' in message.content:
        while True:
            response = random.choice(utm)
            if response == lastreponse:
                response = random.choice(utm)
            else:
                await message.channel.send(response)
                lastreponse = response
                break


    if 'jared' in message.content or 'JARED' in message.content:
        response = "lady. No words"
        await message.channel.send(response)

    if 'LPS' in message.content or 'lps' in message.content or 'littlest pet shop' in message.content or 'LITTLEST PET SHOP' in message.content:
        while True:
            response = random.choice(lps)
            if response == lastreponse:
                response = random.choice(lps)
            else:
                await message.channel.send(response)
                lastreponse = response
                break

    if message.content == "test test test":
        response = 'True\nSo true'
        await message.channel.send(response)

def stopit():
    windah.destroy()
    exit()

def startit(TOKEN):
    client.run(TOKEN)
    return

def run_bot():
    status.config(text="Initializing bot...")
    thr.Thread(target=startit, args=(TOKEN,)).start()

windah = tk.Tk()
windah.geometry("500x200")

startbutt = tk.Button(windah, text="Start Bot", command=run_bot)
startbutt.pack(pady=10)

stopbutt = tk.Button(windah, text="Stop Bot", command=stopit)
stopbutt.pack(pady=10)

status = tk.Label(windah, text="Press 'Start Bot' to start the bot.")
status.pack(pady=10)

windah.mainloop()