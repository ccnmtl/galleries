# Django settings for galleries project.
import os.path
from ccnmtlsettings.shared import common

project = 'galleries'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'galleries.main',
]

USE_TZ = True

MIDDLEWARE_CLASSES += [  # noqa
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

INSTALLED_APPS += [  # noqa
    'sorl.thumbnail',
    'bootstrap3',
    'bootstrapform',
    'infranil',
    'django_extensions',
    'registration',
    'pagetree',
    'pageblocks',
    'quizblock',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'modelcluster',
    'taggit',

    'galleries.main',
]

PAGEBLOCKS = [
    'pageblocks.TextBlock',
    'pageblocks.HTMLBlock',
    'pageblocks.PullQuoteBlock',
    'pageblocks.ImageBlock',
    'pageblocks.ImagePullQuoteBlock',
    'quizblock.Quiz',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7

WAGTAIL_SITE_NAME = 'galleries'
