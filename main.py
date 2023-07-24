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
        print(f'Get articles from WordPress: page = {page}')
        response = get_from_wp({
            '_fields': 'title, link, featured_media',
        }, f'{WP_POSTS_PATH}?per_page={50}&page={page}')

        if not response.ok:
            print('No data.')
            break

        data = response.json()
        print(f'Data length is {len(data)}')
        # pprint.pprint(data)

        all_posts.extend(data)
        page += 1

    picked = random.choice(all_posts)
    pprint.pprint(picked)

    text = f'{picked["title"]["rendered"]} {picked["link"]}'
    client = twitter_client_builder.create_twitter_client()
    response = client.create_tweet(text=text)

    pprint.pprint(response)


if __name__ == '__main__':
    main()
