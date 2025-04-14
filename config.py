import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Credentials
ML_CLIENT_ID = os.getenv('ML_CLIENT_ID')
ML_CLIENT_SECRET = os.getenv('ML_CLIENT_SECRET')
ML_REDIRECT_URI = os.getenv('ML_REDIRECT_URI')
ML_ACCESS_TOKEN = os.getenv('ML_ACCESS_TOKEN')
ML_REFRESH_TOKEN = os.getenv('ML_REFRESH_TOKEN')

# Publication IDs
ML_PUBLICATION_1_ID = os.getenv('ML_PUBLICATION_1_ID')
ML_PUBLICATION_2_ID = os.getenv('ML_PUBLICATION_2_ID')

# Sync Configuration
SYNC_INTERVAL = int(os.getenv('SYNC_INTERVAL', 5))  # Default 5 minutes

# API URLs
ML_API_BASE_URL = 'https://api.mercadolibre.com'
ML_AUTH_URL = f'{ML_API_BASE_URL}/oauth/token'
ML_ITEMS_URL = f'{ML_API_BASE_URL}/items' 