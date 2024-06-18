import requests
import aiohttp
from pycoingecko import CoinGeckoAPI
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
)

load_dotenv()


#  Obter as 10 principais criptomoedas
async def get_top_10_cryptos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'brl',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                top_10_cryptos = await response.json()
                return top_10_cryptos
            else:
                return None
            
# Para obter as moedas mais vendidas nas últimas 24 horas
async def get_top_coins_24h():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'brl',
        'order': 'volume_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false',
        'date': 'id'  # Filtra para as últimas 24 horas
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                top_coins = await response.json()
                return top_coins
            else:
                return None


# Para obter as moedas mais vendidas nas últimas 7 dias
async def get_top_coins_7d():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'brl',
        'order': 'volume_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                top_coins = await response.json()
                return top_coins
            else:
                return None




# Para obter informações de uma criptomoeda específica
async def get_crypto_info(query):
    url = f"https://api.coingecko.com/api/v3/coins/{query.lower()}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
    
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'brl',
        'ids': query.lower(),
        'order': 'market_cap_desc',
        'per_page': 1,
        'page': 1,
        'sparkline': 'false'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                results = await response.json()
                if results:
                    return results[0]
                else:
                    return None

# Para obter notícias relacionadas a uma criptomoeda
async def get_crypto_news(crypto_name):
    url = f"https://newsapi.org/v2/everything?q={crypto_name}&apiKey={getenv('NEWS_API_KEY')}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                news = await response.json()
                return news["articles"]
            else:
                return None

app = Client(
    'CryptoPedia_bot',
    api_id=getenv('api_id'),
    api_hash=getenv('api_hash'),
    bot_token=getenv('bot_token')
    
)

# Comando /top10 no bot
@app.on_message(filters.command("top10"))
async def top10(client, message):
    cryptos = await get_top_10_cryptos()
    if cryptos:
        response_text = "Top 10 Criptomoedas:\n"
        for crypto in cryptos:
            response_text += f"<b>Nome:</b> {crypto['name']}, <b>Capitalização de Mercado:</b> R${crypto['market_cap']:,}\n"
        await message.reply_text(response_text)
    else:
        await message.reply_text("Erro ao obter dados das criptomoedas.")

    # Mostrar as moedas mais vendidas nas últimas 24 horas
    top_coins_24h = await get_top_coins_24h()
    if top_coins_24h:
        response_text_24h = "\nMoedas mais vendidas nas últimas 24 horas:\n"
        for coin in top_coins_24h:
            if 'name' in coin and 'total_volume' in coin:
                response_text_24h += f"<b>Nome:</b> {coin['name']}, <b>Volume:</b> R${coin['total_volume']:,}\n"
        await message.reply_text(response_text_24h)

    # Mostrar as moedas mais vendidas nas últimas 7 dias
    top_coins_7d = await get_top_coins_7d()
    if top_coins_7d:
        response_text_7d = "\nMoedas mais vendidas nas últimas 7 dias:\n"
        for coin in top_coins_7d:
            if 'name' in coin and 'total_volume' in coin:
                response_text_7d += f"<b>Nome:</b> {coin['name']}, <b>Volume:</b> R${coin['total_volume']:,}\n"
        await message.reply_text(response_text_7d)



# Comando /moeda no bot
@app.on_message(filters.command("moeda"))
async def moeda(client, message):
    try:
        query = message.command[1]
        crypto_info = await get_crypto_info(query)
        if crypto_info:
            response_text = (
                f"<b>Nome:</b> {crypto_info['name']}\n"
                f"<b>Símbolo:</b> {crypto_info['symbol']}\n"
                f"<b>Preço Atual:</b> R${crypto_info['market_data']['current_price']['brl']}\n"
                f"<b>Capitalização de Mercado:</b> R${crypto_info['market_data']['market_cap']['brl']:,}\n"
                f"<b>Volume de 24h:</b> R${crypto_info['market_data']['total_volume']['brl']:,}\n"
            )
            await message.reply_text(response_text)
        else:
            await message.reply_text("Erro ao obter informações da criptomoeda.")
    except IndexError:
        await message.reply_text("Por favor, forneça o nome, símbolo ou ID da criptomoeda. Exemplo: /moeda bitcoin")

# Acessar /notícias no bot
@app.on_message(filters.command("noticias"))
async def noticias(client, message):
    try:
        crypto_name = message.command[1]
        news = await get_crypto_news(crypto_name)
        if news:
            response_text = f"Últimas notícias sobre {crypto_name}:\n\n"
            for article in news[:5]:
                response_text += (
                    f"**Título:** {article['title']}\n"
                    f"**Fonte:** {article['source']['name']}\n"
                    f"**Link:** {article['url']}\n\n"
                )
            await message.reply_text(response_text)
        else:
            await message.reply_text("Erro ao obter notícias da criptomoeda.")
    except IndexError:
        await message.reply_text("Por favor, forneça o nome da criptomoeda. Exemplo: /notícias bitcoin")


# Acessar /callback no bot
@app.on_message(filters.command('callback'))
async def callbacks(client, message):
    inline_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('CoinGecko', url='https://www.coingecko.com/'),
                InlineKeyboardButton('Bot no Discord', url='https://discord.com/oauth2/authorize?client_id=1243954267933507638&permissions=8&scope=bot')
            ]
        ]
    )
    await message.reply('Escolha algo!', reply_markup=inline_markup)



# Comando /help e /start no bot
@app.on_message(filters.command('help') | filters.command('start'))
async def help_command(client, message):
    await message.reply(
        "Olá!🤖💰,Estou aqui para te ajudar com informações sobre criptomoedas\n"
        '**Esse é o menu para pedir ajuda!\n**'
        'Use **/start para iniciar o bot!\n**'
        'Use **/menu para esse menu em teclado!\n**'
        'Use **/help para pedir ajuda!\n**'
        'Use **/callback para acessar links de interesse \n**'
        'Use **/top10 para listar 10 criptomoedas na cotação atual\n**'
        'Use **/moeda (nome, símbolo ou ID) para consultar preço e informações de uma criptomoeda específica\n**'
        'Use **/noticias (nome da moeda) para buscar as últimas notícias relacionadas à criptomoeda**'
    )


# Comando /menu para mostrar botões inline
@app.on_message(filters.command('menu'))
async def menu(client, message):
    menu_buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Top 10 Criptomoedas", callback_data="top10")],
            [InlineKeyboardButton("Moeda Bitcoin", callback_data="moeda bitcoin")],
            [InlineKeyboardButton("Notícias Bitcoin", callback_data="noticias bitcoin")]
        ]
    )
    await message.reply("Escolha uma das opções abaixo:", reply_markup=menu_buttons)







print('rodando!!!')
app.run()