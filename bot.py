import discord, random
from discord.ext import commands


bot = commands.Bot(command_prefix = '!')
copyPastas = ["🆗 son, 🌞 there ain't❌❌a ☝single☝fucking☝person☝ with any intellect👓👓📖who gives a 🎮remote🎮fuck🎮about your extensive vaping💯😎💨 talent. 😂I happen to be quite🎩the🎩intellectual🎩myself, so I can confirm✔✔this fact💯as truth™.👌if👌you👌think👌 that your vape💯😎💨 is going↗to get you hoes👯👯, you are utterly🐄 mistaken❌, fam👪. my pa👨 once taught📖 me the 😏secret😏 of life👍💛, and it was not❌❌ your vape💯😎💨 🆗🆒now listen 👂👂here my chum✌✌, my pa👨 was a man who kept it 💯💯💯💯💯💯. ✋that✋is✋six✋fucking✋hundreds✋ and he never❌🙅🙅 once vaped💯😎💨. The man 🚬smoked🚬some🚬mad🚬cigars🚬 because he wasnt❌the pussy🐱🐱you are🆗⁉❗⁉ he lived to be 💯 because he kept it 💯💯💯💯💯💯 and killed🔫🔪 👌every👌vaping👌fucker👌he👌saw👌🆗🆒😂😂👀👀 so in the spirit👻of me good ol pa👨, I think💭you should kys🔫 they have 🆓 vapes💯😎💨 in hell🔥and🔥it's🔥lit🔥for😂 unintelligent vaping💯😎💨 hooligans like yourself👌😂😂",
            "IM DELETING YOU, DADDY!😭👋 ██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete..... ████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete.... ███████]]]]]]]]]]]]]]]] 60% complete.... ███████████] 99% complete..... 🚫ERROR!🚫 💯True💯 Daddies are irreplaceable 💖I could never delete you Daddy!💖 Send this to ten other 👪Daddies👪 who give you 💦cummies💦 Or never get called ☁️squishy☁️ again❌❌😬😬❌❌ If you get 0 Back: no cummies for you 🚫🚫👿 3 back: you're squishy☁️💦 5 back: you're daddy's kitten😽👼💦 10+ back: Daddy",
            "ACHOO:bangbang:What was that:interrobang::interrobang::smirk::smirk: Uh-oh:hushed: looks like you just got :eyes::eyes: coronavirus :triumph::stuck_out_tongue_winking_eye::stuck_out_tongue_winking_eye:  Don't you know that the coronavirus :thermometer_face: is CUMMING:sweat_drops: to America :flag_um::interrobang::nauseated_face::head_bandage::thermometer_face::drooling_face: The world :earth_asia: HOE Organisation :see_no_evil::tongue: is calling HOE-VID19:date: a POSSIBLE PANTIE-DEMIC:lips::ok_hand::point_left:  No more touching daddy :tired_face::tired_face::older_adult: until you wash:shower::shower: your dirty :nauseated_face::face_vomiting:nasty little :fingers_crossed: fingers:hand_splayed::vulcan::raised_hand:  for :six::nine: secounds with sHOEp :droplet: and water:sweat_drops::droplet::tongue: otherwise it doesn't count :clown::clown::clown:  Time to stop :octagonal_sign: spredding your germs:nauseated_face::thermometer_face::head_bandage: and start spredding :hushed: your legs:footprints::lips::eyes: because everyone :woman::man_teacher::man_construction_worker::merman:is TWERKING:smiling_imp::smiling_imp: from home:house::house_with_garden:  SEND THIS TO :one::zero: coronavirus cunts :point_right::ok_hand: otherwise the coronavirus :scream_cat::scream_cat: is cumming :eggplant::peach::eggplant: for you too :two:"]

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    #if channel == 'bot-development': #and reaction.emoji == 'watermelon':
    roleGamer = discord.utils.get(user.guild.roles, name='gamers')
    await user.add_roles(roleGamer, atomic=False)

@bot.command()
async def ping(cxt):
    await cxt.send('pong')

@bot.command()
async def degen(cxt):
    ranNum = random.randint(0,len(copyPastas)-1)
    await cxt.send(copyPastas[ranNum])


bot.run('TOKEN')
