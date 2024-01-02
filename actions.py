import discord

async def get_response(message: discord.Message, user_message: str) -> str:
    p_message = user_message.lower()

    if p_message == 'hello':
        return 'world'
    else:
        return ''