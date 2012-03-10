"""Example dragonfile file"""

from dragons.util import collect_cookies

__version__ = '1'
__all__ = ['SETTINGS', 'start']

SETTINGS = {
    'host': 'dev1.indexmedia.com',
    'protocol': 'http',
    'concurrency': 1,
}

def start(client, context):
    response = client.get('/tag/media/?media_url=http://www.google.com/icon.png')
    collect_cookies(response, client)
    return start