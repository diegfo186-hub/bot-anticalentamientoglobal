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

# Lista de tips
tips.TIPS = [
    "Lava la ropa con agua fría para ahorrar energía.",
    "Tiende la ropa al aire libre en lugar de usar secadora.",
    "Desconecta cargadores y equipos cuando no estén en uso.",
    "Usa regletas con interruptor para evitar consumo fantasma.",
    "Planifica tus compras para reducir el desperdicio de alimentos.",
    "Consume frutas y verduras de temporada siempre que puedas.",
    "Lleva una botella reutilizable y evita comprar plástico.",
    "Usa bolsas reutilizables al hacer tus compras.",
    "Prefiere tren o autobús frente a vuelos de corta distancia.",
    "Comparte herramientas que solo se usan de forma ocasional.",
    "Reduce el uso de papel mediante documentos digitales.",
    "Imprime solo lo necesario y usa ambas caras de la hoja.",
    "Mantén los neumáticos bien inflados para ahorrar combustible.",
    "Agrupa varios recados en un solo desplazamiento.",
    "Instala paneles solares si son viables para tu hogar.",
    "Elige productos con menos embalaje y empaques reciclables.",
    "Compra artículos fabricados con materiales reciclados.",
    "Participa en jornadas de limpieza de espacios públicos.",
    "Aprovecha la ventilación natural antes del aire acondicionado.",
    "Apoya proyectos locales de energía renovable y conservación."
]


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


token2 = ""
# Ejecuta el bot con tu token (mantén el token seguro)
bot.run(""+token2)
