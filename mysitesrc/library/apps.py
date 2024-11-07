'''
Library App module
'''
from django.apps import AppConfig


class LibraryConfig(AppConfig):
    '''
    Application configuration for Library application
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
