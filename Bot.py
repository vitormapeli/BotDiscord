import discord

# Definindo os intents necessários
intents = discord.Intents.default()
intents.typing = False  # Desativando eventos de digitação (opcional)
intents.presences = False  # Desativando eventos de presença (opcional)

# Criando o cliente do Discord com os intents
client = discord.Client(intents=intents)


# Evento de inicialização do bot
@client.event
async def on_ready():
  print('Estou online como {0.user}'.format(client))
  channel_id = CANAL DA SUA SALA  # ID do canal onde deseja enviar a mensagem
  channel = client.get_channel(channel_id)

  if channel:
    await channel.send('Olá! Esta é uma mensagem enviada pelo bot.')


# Evento de mensagem recebida
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Olá!')


# Token de autenticação do bot (substitua pelo seu próprio token)
client.run(
    'TOKEN')
