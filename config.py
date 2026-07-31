import os

class Config:
    def __init__(self):
        self.env = self.load_env()
        self.db_uri = self.get_db_uri()
        self.api_key = self.get_api_key()

    def load_env(self):
        return os.getenv('ENV', 'development')

    def get_db_uri(self):
        if self.env == 'production':
            return os.getenv('PROD_DB_URI')
        return os.getenv('DEV_DB_URI')

    def get_api_key(self):
        return os.getenv('API_KEY')

config = Config()