# https://gist.github.com/gpocentek/bd4c3fbf8a6ce226ebddc4aad6b46c0a

import os
import re
import sys
import requests
import gitlab

gitlab_endpoint = os.environ.get("GITLAB_ENDPOINT")

URL = 'https://{}'.format(gitlab_endpoint)
SIGN_IN_URL = 'https://{}/users/sign_in'.format(gitlab_endpoint)
LOGIN_URL = 'https://{}/users/sign_in'.format(gitlab_endpoint)

session = requests.Session()

def auth(username, password):
    sign_in_page = session.get(SIGN_IN_URL).content
    for line in sign_in_page.split('\n'):
        match = re.search('name="authenticity_token" value="([^"]+)"', line)
        if match:
            break

    token = None
    if match:
        token = match.group(1)

    if not token:
        print('Unable to find the authenticity token')
        return False

    data = {
        'user[login]': username,
        'user[password]': password,
        'authenticity_token': token
    }
    result = session.post(LOGIN_URL, data=data)
    if result.status_code != 200:
        print('Failed to log in')
        return False

    gitlab_api = gitlab.Gitlab(URL, api_version=4, session=session)
    return gitlab_api
