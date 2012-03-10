"""The dragons command line tool"""
__author__ = 'adam'

def collect_cookies(response, client):
    """Collects set-cookie headers, and applies them to an HTTPClient"""

    set_cookies = filter(lambda h: h[0] == 'set-cookie', response.headers)
    set_cookies = map(lambda h: h[1].split('; ')[0], set_cookies)

    if len(set_cookies):
        cookies = client.default_headers.get('Cookie', '').split('; ')
        for new_cookie in set_cookies:
            if new_cookie not in cookies:
                cookies.append(new_cookie)

        cookies = '; '.join(cookies)
        if len(cookies):
            client.default_headers['Cookie'] = cookies
