import discord
import actions


async def event(message, user_message, privacy):
    try:
        response = await actions.get_response(message, user_message)
        await message.author.send(response) if privacy else await message.channel.send(response)

    except Exception as e:
        print(e)


def run():
    with open("token.txt", "r") as file:
        token = file.read()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} successfully logged in')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if message.content.startswith("!"):
            user_message = message.content[1:].strip()
            await event(message, user_message, privacy=message.channel.type == 'private')

    client.run(token)
