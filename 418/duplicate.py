import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    # Read the CSV
    df = pd.read_csv('ecommerce_transactions.csv')

    # Find duplicate Transaction_IDs
    duplicates = df[df['Transaction_ID'].duplicated(keep='first')]


    # Log duplicate information
    logger.info(f"Found {len(duplicates)} duplicate rows")
    logger.info("\nDuplicate Transaction IDs:")
    logger.info(duplicates[['Transaction_ID', 'Date', 'Customer_ID', 'Product_ID']].to_string())

    # Remove duplicates and keep first occurrence
    df_clean = df.drop_duplicates(subset=['Transaction_ID'], keep='first')

    # Log results
    logger.info(f"\nOriginal dataset rows: {len(df)}")
    logger.info(f"Clean dataset rows: {len(df_clean)}")
    logger.info(f"Removed {len(df) - len(df_clean)} duplicate rows")

    # save cleaned dataset
    df_clean.to_csv('ecommerce_transactions_clean.csv', index=False)

except Exception as e:
    logger.error(f"Error processing file: {str(e)}")