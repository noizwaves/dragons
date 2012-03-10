"""The dragons command line tool"""

from geventhttpclient import HTTPClient

def process(dragonfile, settings):
    """
    Performs processing of 1 concurrent user

    settings (dict) - contains the settings to be applied.
    """

    entry_method = dragonfile.start
    host = settings['host']

    while True:
        current_method, context = entry_method, {}
        client = HTTPClient.from_url(host)
        while True:
            current_method = current_method(client, context)
            if not current_method:
                break



