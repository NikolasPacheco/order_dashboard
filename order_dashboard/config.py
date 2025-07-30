import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your-secret-key'  # Change later for security
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'uploads')

# Use the config in app
Config = Config
