AUTHOR = 'Bruno Teles'
SITENAME = "Bruno's Website of Things"
SITEURL = ''


THEME = 'notmyidea'

GITHUB_URL = 'https://github.com/me50/TheHorusHawk'
PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('Twine', 'https://twinery.org/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/bruno-madureira-teles/'),
          ('GitHub', 'https://github.com/TheHorusHawk/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Adding IFs to static path to serve Interactive Fiction HTMLs without modifying them
STATIC_PATHS: [
        'images',
        'IFs',
        ]
# Just for development, forces reloading cache
LOAD_CONTENT_CACHE = False

PAGE_EXCLUDES = ['IFs']
ARTICLE_EXCLUDES = ['IFs']
