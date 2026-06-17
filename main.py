import random
import pyttsx3
import discord
from discord.ext import commands
import tips

engine = pyttsx3.init()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# RATE
engine.setProperty('rate', 150)

# VOLUME
engine.setProperty('volume', 1.0)

# VOICE
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def get_tip():
    return random.choice(tips.TIPS)


@bot.command()
async def tip(ctx):
    tip = get_tip()
    await ctx.send(f"**consejo:** {tip}")


@bot.command()
async def comandos(ctx):
    await ctx.send(
        "-----------------------------------------------\n"
        "  Bienvenido al bot de consejos ambientales!\n\n"
        "  Comandos:\n"
        "    !tip - Obtén un consejo ambiental\n"
        "    !comandos - Muestra este mensaje de ayuda\n"
        "-----------------------------------------------"
    )


token2 = "Lri04hEnfDn7pztv91AM2YaBZLuGmvVKcPx7fs"
# Ejecuta el bot con tu token (mantén el token seguro)
bot.run("MTUxNjQ4MjMxOTkwMzQ5MDE1OQ.GvOiXb."+token2)
