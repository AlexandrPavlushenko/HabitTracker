from .settings import *

SECRET_KEY = 'ci-test-secret-key-123!@#'  # Временный ключ для тестов
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.sqlite3'),
    }
} # Используем временную базу данных