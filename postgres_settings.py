DATABASES = {
        'default': {
                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
                    'NAME': 'django_tests',
                    'HOST': 'localhost',
                    'USER': 'hudson',
                    'PASSWORD': 'hudson',
                },
        'other': {
                    'ENGINE': 'django.db.backends.sqlite3',
                }
}

