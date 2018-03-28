"""
   date: 2018-03-26 23:16 
"""

__author__ = "WXGALY"

import asyncio

import time, uuid

from static.webapp.web.static.orm import Model, StringField, BooleanField, FloatField, TextField, create_pool, \
    close_pool


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


# async def test(loop):
#     # 创建连接池
#     db_dict = {'user': 'root', 'password': '123456', 'db': 'wxg'}
#     await create_pool(loop=loop, **db_dict)
#     u = User(name='Test', email='test@example.com', passwd='12345', image='about:blank')
#     u1 = User(name='aaa', email='aaaa@example.com', passwd='5555', image='about:blank')
#     u2 = User(name='bbb', email='bbb@example.com', passwd='54545', image='about:blank')
#     await u.save()
#     await u1.save()
#     await u2.save()
#     await close_pool()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
