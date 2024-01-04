import discord
import auth

# if the user message matches an expected input, return the response
async def getResponse(message: discord.Message, user_message):
    from bot import FMKey

    p_message = user_message.lower()

    if p_message.startswith('token'):
        _, token = p_message.split(' ', 1)
        auth.setToken(str(message.author), str(token))
        print('Successfully connected token ' + token + ' to user ' + str(message.author))
        return 'Your Last.fm account has been successfully connected to Discord!'

    elif p_message == 'auth':
        print("Sending authentication instructions to "+str(message.author))
        await message.author.send("http://www.last.fm/api/auth/?api_key="+FMKey)
        return 'I have sent you instructions on how to connect in your DMs!'
    elif p_message == 'hello':
        return 'world'
    else:
        return user_message + " is not a recognised command"
