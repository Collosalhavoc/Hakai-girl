from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1070396868
    OWNER_USERNAME = "Collosal_havoc"  # my telegram username
    API_KEY = "1202946675:AAG0UtAekqvUZT3A79SpaKkfb0R38ZmoqAs"
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1001410030001'
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1070396868,998193984]  # List of id's for users which have bot.
    LOAD = []
    NO_LOAD = ['translation']
