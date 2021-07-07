DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=djangoone'
        },
        'NAME': 'localdb',
        'USER': 'Louise',
        'PASSWORD': 'Louise',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}