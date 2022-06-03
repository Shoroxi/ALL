try:
    from config.config import __telegramtoken__, __admin_id__, __database_url__
except ImportError:
    #Heorku stuff
    import os

    __telegramtoken__ = os.environ.get('TELEGRAM_TOKEN')
    __admin_id__ = os.environ.get('ADMIN_ID') #@Shorox
    __database_url__ = os.environ.get('DATABASE_URL')



