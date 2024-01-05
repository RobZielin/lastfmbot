import discord
import auth


# if the user message matches an expected input, return the response
async def getResponse(message: discord.Message, user_message):
    from bot import network

    p_message = user_message.lower()

    # breaks up the message into a command and a target
    try:
        _, target = user_message.split(' ', 1)
    except Exception:
        target = None

    # this associates a discord user to their specified last.fm account
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

    # first check if the user exists to prevent unnecessary API calls, if the user exists make a call 
    if str(user) != 'None':
        if p_message.startswith('playing'):
            track = network.get_user(user).get_now_playing()
            if str(track) == 'None':
                return '**' + user + '** is not currently scrobbling'
            # add last.fm commands that require a target user here using elif statements
            else:
                return user + ' is currently scrobbling to: **' + str(track) + '**'

    # ordinary bot commands that do not require last.fm, add more under the first if statement as elif statements
    if p_message == 'hello':
        return 'world'
    # else statement that runs in case there was no matching commands, first does a check if a command is referencing a non-existing user, if not defaults to the unrecognized command statement
    # if additional commands are added, this part should be rewritten to perhaps check from a list of commands
    else:
        if target is not None and p_message.startswith('playing'):
            return '**'+ target + '** is not a recognised user'
        else:
            return p_message + ' is not a recongnised command'
