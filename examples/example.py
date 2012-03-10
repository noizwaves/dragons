"""Example dragonfile file"""

from dragons.util import collect_cookies

def start(client, context):
    response = client.get('/api/')
    collect_cookies(response, client)

    return start # recurse