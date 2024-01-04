import json

def setToken(user, token):
    user_tokens = {}

    # load existing tokens from json
    try:
        with open('user_tokens.json', 'r') as file:
            user_tokens = json.load(file)
    except FileNotFoundError:
        pass  # if file does not exist, create it

    user_tokens[user] = token

    # save tokens to json
    with open('user_tokens.json', 'w') as file:
        json.dump(user_tokens, file)

def getToken(user):
    with open('user_tokens.json', 'r') as file:
        user_tokens = json.load(file)

    # get token from json
    token = user_tokens.get(user)

    return token
