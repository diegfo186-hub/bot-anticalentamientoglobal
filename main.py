import random
import pyttsx3
import discord
from discord.ext import commands
from googletrans import Translator
import tips

engine = pyttsx3.init()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
translator = Translator()

# RATE
engine.setProperty('rate', 150)

# VOLUME
engine.setProperty('volume', 1.0)

# VOICE
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
language = 'es'  # Idioma predeterminado


def get_tip():
    return random.choice(tips.TIPS)


async def on_ready():
    print("-----------------------------------------------\n")
    print("botsito en línea")
    print(f'Bot conectado como {bot.user.name}')
    print("Lista de comandos:")
    for command in bot.commands:
        print(f"  - {command.name}")
    print("-----------------------------------------------\n")


@bot.command()
async def tip(ctx):
    tip = get_tip()
    translated = translator.translate(tip, dest=language)
    await ctx.send(f"**consejo:** {translated.text}")


@bot.command()
async def comandos(ctx):
    await ctx.send(
        "-----------------------------------------------\n"
        "  Bienvenido al bot de consejos ambientales!\n\n"
        "  Comandos:\n"
        "    !tip - Obtén un consejo ambiental\n"
        "    !comandos - Muestra este mensaje de ayuda\n"
        "    !lang - Cambia el idioma del bot\n"
        "    !langlist - Muestra una lista de idiomas disponibles\n"
        "-----------------------------------------------"
    )


@bot.command()
async def langlist(ctx):
    await ctx.send(
        "-----------------------------------------------\n"
        "    Idiomas disponibles:\n"
        "    es = Español\n"
        "    en = Inglés\n"
        "    fr = Francés\n"
        "    pt = Portugués\n"
        "    de = Alemán\n"
        "    it = Italiano\n"
        "    zh-CN = Chino (Simplificado)\n"
        "    zh-TW = Chino (Tradicional)\n"
        "    ja = Japonés\n"
        "    ko = Coreano\n"
        "    ar = Árabe\n"
        "    ru = Ruso\n"
        "    hi = Hindi\n"
        "-----------------------------------------------"
    )


@bot.command()
async def lang(ctx, lang_code):
    global language
    language = lang_code
    await ctx.send(f"Idioma cambiado a: {language}")


token2 = ""
# Ejecuta el bot con tu token (mantén el token seguro)
bot.run(""+token2)
