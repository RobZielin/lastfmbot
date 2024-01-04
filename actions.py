import discord
import auth


# if the user message matches an expected input, return the response
async def getResponse(message: discord.Message, user_message):
    from bot import network

    p_message = user_message.lower()
    try:
        _, target = user_message.split(' ', 1)
    except Exception:
        target = None

    if p_message.startswith('connect'):
        try:
            # tries to verify if the username is correct by making an api call with that username
            network.get_user(target).get_now_playing()
            # writes the username into a json connecting it to the user's discord name
            auth.setToken(str(message.author), str(target))
            print('Successfully connected last.fm account ' + target + ' to user ' + str(message.author))
            return 'Your Last.fm account has been successfully connected to Discord!'
        except Exception:
            # username was not found by the last.fm api so it returns this
            return target + ' is not a valid Last.fm account name'

    user = auth.getToken(target)

    if str(user) == 'None':
        return '**' + target + '** has not connected their Last.fm to Discord'
    else:
        if p_message.startswith('playing'):
            track = network.get_user(user).get_now_playing()
            if str(track) == 'None':
                return '**' + user + '** is not currently scrobbling'
            else:
                return user + ' is currently scrobbling to: **' + str(track) + '**'
        elif p_message == 'hello':
            return 'world'
        else:
            return user_message + " is not a recognised command"
