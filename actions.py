import discord

# if the user message matches an expected input, return the response
async def getResponse(message: discord.Message, user_message):
    p_message = user_message.lower()

    if p_message == 'hello':
        return 'world'
    elif p_message == 'auth':
        await message.author.send("http://www.last.fm/api/auth/?api_key=xxx")
        return 'I have sent you instruction on how to connect in your DMs!'
    else:
        return user_message + " is not a recognised command"
