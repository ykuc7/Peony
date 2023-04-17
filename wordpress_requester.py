import json
import os
import pprint

import dotenv
import requests

WP_CATEGORY_PATH = '/wp-json/wp/v2/categories/'
WP_POSTS_PATH = '/wp-json/wp/v2/posts'

dotenv.load_dotenv()


def get_from_wp(payload, path: str):
    base_url = os.environ['WP_BASE_URL']
    auth_user = os.environ['WP_AUTH_USER']
    auth_pass = os.environ['WP_AUTH_PASS']

    headers = {'content-type': "Application/json"}
    res = requests.get(base_url + path, data=json.dumps(payload), headers=headers, auth=(auth_user, auth_pass))

    if res.ok is not True:
        pprint.pprint(res.reason)

    return res


if __name__ == "__main__":
    response = get_from_wp({
        '_fields': 'title, categories',
        'per_page': 100,
    }, WP_POSTS_PATH)
    pprint.pprint(response.json())
