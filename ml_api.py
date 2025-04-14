import requests
from loguru import logger
from config import (
    ML_CLIENT_ID,
    ML_CLIENT_SECRET,
    ML_ACCESS_TOKEN,
    ML_REFRESH_TOKEN,
    ML_AUTH_URL,
    ML_ITEMS_URL
)

class MercadoLibreAPI:
    def __init__(self):
        self.access_token = ML_ACCESS_TOKEN
        self.refresh_token = ML_REFRESH_TOKEN
        self.client_id = ML_CLIENT_ID
        self.client_secret = ML_CLIENT_SECRET

    def refresh_access_token(self):
        """Refresh the access token using the refresh token."""
        try:
            data = {
                'grant_type': 'refresh_token',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'refresh_token': self.refresh_token
            }
            response = requests.post(ML_AUTH_URL, data=data)
            response.raise_for_status()
            
            tokens = response.json()
            self.access_token = tokens['access_token']
            self.refresh_token = tokens['refresh_token']
            logger.info("Access token refreshed successfully")
            return True
        except Exception as e:
            logger.error(f"Error refreshing access token: {str(e)}")
            return False

    def get_item_stock(self, item_id):
        """Get the current stock of an item."""
        try:
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.get(f'{ML_ITEMS_URL}/{item_id}', headers=headers)
            response.raise_for_status()
            
            item_data = response.json()
            return item_data.get('available_quantity', 0)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                if self.refresh_access_token():
                    return self.get_item_stock(item_id)
            logger.error(f"Error getting item stock: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error getting item stock: {str(e)}")
            return None

    def update_item_stock(self, item_id, new_stock):
        """Update the stock of an item."""
        try:
            headers = {
                'Authorization': f'Bearer {self.access_token}',
                'Content-Type': 'application/json'
            }
            data = {'available_quantity': new_stock}
            response = requests.put(f'{ML_ITEMS_URL}/{item_id}', headers=headers, json=data)
            response.raise_for_status()
            
            logger.info(f"Stock updated successfully for item {item_id}: {new_stock}")
            return True
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                if self.refresh_access_token():
                    return self.update_item_stock(item_id, new_stock)
            logger.error(f"Error updating item stock: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Error updating item stock: {str(e)}")
            return False 