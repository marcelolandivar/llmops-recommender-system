import pandas as pd

class DataLoader:
    def __init__(self, original_csv_path: str, processed_csv_path: str):
        self.original_csv_path = original_csv_path
        self.processed_csv_path = processed_csv_path

    def load_data(self) -> pd.DataFrame:
        """Load data from a CSV file.
            Sets encoding to 'utf-8' and skips bad lines.
        """
        try:
            data = pd.read_csv(self.original_csv_path, 
                               encoding='utf-8', 
                               on_bad_lines='skip').dropna()
            required_columns = ['Name', 'Genres', 'synopsis']
            
            missing_columns = [col for col in required_columns if col not in data.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")

            # Create combined_info column
            data['combined_info'] = ("Title: " + data['Name'].astype(str) + ". Overview: " + 
                                   data['synopsis'].astype(str) + ". Genres: " + data['Genres'].astype(str))
            
            data[['combined_info']].to_csv(self.processed_csv_path, index=False, encoding='utf-8')
            print("Data loaded successfully.")
            return self.processed_csv_path
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
        
