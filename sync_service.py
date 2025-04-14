import time
import schedule
from loguru import logger
from ml_api import MercadoLibreAPI
from config import ML_PUBLICATION_1_ID, ML_PUBLICATION_2_ID, SYNC_INTERVAL

class StockSynchronizer:
    def __init__(self):
        self.api = MercadoLibreAPI()
        self.publication_1_id = ML_PUBLICATION_1_ID
        self.publication_2_id = ML_PUBLICATION_2_ID

    def sync_stock(self):
        """Synchronize stock between two publications."""
        try:
            # Get current stock for both publications
            stock_1 = self.api.get_item_stock(self.publication_1_id)
            stock_2 = self.api.get_item_stock(self.publication_2_id)

            if stock_1 is None or stock_2 is None:
                logger.error("Failed to get stock information")
                return

            # If stocks are different, update both to the lower value
            if stock_1 != stock_2:
                new_stock = min(stock_1, stock_2)
                logger.info(f"Stock mismatch detected: {stock_1} vs {stock_2}. Synchronizing to {new_stock}")

                # Update both publications to the new stock value
                success_1 = self.api.update_item_stock(self.publication_1_id, new_stock)
                success_2 = self.api.update_item_stock(self.publication_2_id, new_stock)

                if success_1 and success_2:
                    logger.success(f"Stock synchronized successfully to {new_stock}")
                else:
                    logger.error("Failed to synchronize stock")
            else:
                logger.info(f"Stocks are already synchronized at {stock_1}")

        except Exception as e:
            logger.error(f"Error during stock synchronization: {str(e)}")

def main():
    """Main function to run the stock synchronization service."""
    logger.info("Starting Mercado Libre Stock Synchronization Service")
    
    synchronizer = StockSynchronizer()
    
    # Schedule the sync task
    schedule.every(SYNC_INTERVAL).minutes.do(synchronizer.sync_stock)
    
    # Run initial sync
    synchronizer.sync_stock()
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main() 