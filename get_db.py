from tortoise import Tortoise
from tortoise import run_async
import httpx
from models import Users, Posts

# This code is using once for the creating and filling the DB


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


async def fetch_and_insert_data():
    url_users = 'https://gorest.co.in/public/v2/users'
    url_posts = 'https://gorest.co.in/public/v2/posts'

    async with httpx.AsyncClient() as client:
        response = await client.get(url_users)
        response2 = await client.get(url_posts)

    if response.status_code == 200:
        users_data = response.json()

        for user_data in users_data:
            user = await Users.create(id=user_data.get('id'),
                                      name=user_data.get('name'),
                                      email=user_data.get('email'),
                                      gender=user_data.get('gender'),
                                      status=user_data.get('status'))

    if response2.status_code == 200:
        posts_data = response2.json()

        for post_data in posts_data:
            post = await Posts.create(id=post_data.get('id'),
                                      user_id=post_data.get('user_id'),
                                      title=post_data.get('title'),
                                      body=post_data.get('body'))

run_async(init())
run_async(fetch_and_insert_data())
