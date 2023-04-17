import pprint
import random

import twitter_client_builder
from wordpress_requester import get_from_wp

WP_POSTS_PATH = '/wp-json/wp/v2/posts'
WP_MEDIA_PATH = '/wp-json/wp/v2/media'


def main():
    all_posts = []
    page = 1

    while True:
        response = get_from_wp({
            '_fields': 'title, link, featured_media',
            'per_page': 50,
            'page': page,
        }, WP_POSTS_PATH)

        if not response.ok:
            break

        data = response.json()
        all_posts.extend(data)
        page += 1

    # pprint.pprint(all_posts)
    picked = random.choice(all_posts)
    pprint.pprint(picked)

    # response = get_from_wp({
    #     '_fields': 'guid',
    # }, f'{WP_MEDIA_PATH}/{picked["featured_media"]}')
    # data = response.json()
    # pprint.pprint(data)
    #
    # if response.ok:
    #     url = data['guid']['rendered']

    text = f'{picked["title"]["rendered"]} {picked["link"]}'
    client = twitter_client_builder.create_twitter_client()
    response = client.create_tweet(text=text)

    pprint.pprint(response)


if __name__ == '__main__':
    main()
