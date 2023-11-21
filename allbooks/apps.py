from django.apps import AppConfig


class AllbooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'allbooks'

    def ready(self):
        import allbooks.signals  
    
