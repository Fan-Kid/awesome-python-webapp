# -*- coding:utf-8 -*-

' url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

#@get('/')
# async def index(request):
#     users = await User.findAll()
#     return {
#         '__template__' : 'test.html',
#         'users': users
#     }
@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs=[
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something new', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name="Learn Switft", summary=summary, created_at=time.time()-100000)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs':blogs
    }

@get('/api/users')
async def api_get_users():
    # page_index = get_page_index(page)
    # num = yield from User.findNumber('count(id)')
    # p = Page(num, page_index)
    # if num == 0:
    #     return dict(page=p, users=())

    users = await User.findAll(orderBy='`created_at` desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)