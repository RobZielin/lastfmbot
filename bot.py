import discord
import actions


# parses user messages in actions.py
async def event(message, user_message, privacy):
    try:
        response = await actions.getResponse(message, user_message)
        await message.author.send(response) if privacy else await message.channel.send(response)

    except Exception as e:
        print(e)


# initializes the bot, token must be pasted in token.txt
def run():
    with open("token.txt", "r") as file:
        lines = file.readlines()
        botToken = lines[1].strip()
        FMKey = lines[3].strip()
        FMSecret = lines[5].strip()


    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # upon bot login print success message
    @client.event
    async def on_ready():
        print(f'{client.user} successfully logged in')

    # listen for user messages
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'[{channel}] {username}: {user_message} ')

        if message.content.startswith("!"):
            user_message = message.content[1:].strip()
            await event(message, user_message, privacy=message.channel.type == 'private')

    # runs the client
    client.run(botToken)
