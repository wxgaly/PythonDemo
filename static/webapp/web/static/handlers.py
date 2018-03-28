"""
   date: 2018-03-28 0:17 
"""

__author__ = "WXGALY"

' url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from static.webapp.web.static.webcore import get, post

from static.webapp.web.static.models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
