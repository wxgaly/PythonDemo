"""
   date: 2018-03-28 0:17 
"""

__author__ = "WXGALY"

' url handlers'

from static.webapp.web.webcore import get

from static.webapp.web.models import User, Blog


# @get('/')
# async def index(request):
#     users = await User.findAll()
#     return {
#         '__template__': 'index.html',
#         'users': users
#     }
@get('/')
async def index(request):
    blogs = await Blog.findAll()
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
