import requests
import pandas as pd


URL = 'https://api.thecatapi.com/v1/breeds'

def get_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while ingesting data: {e}")
        return None  # Return None in case of error
    
def convert_to_dataframe(data) -> pd.DataFrame:
    try:
        df = pd.json_normalize(data)
        print(type(df))  # Print the type of the DataFrame for verification
        # print(df.head())  # Print the first few rows of the DataFrame for verification
        return df
    except Exception as e:
        print(f"An error occurred while converting data to DataFrame: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

def save_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving data to CSV: {e}")

if __name__ == "__main__":    # Example usage
    raw = get_data_from_api(URL)
    if raw is None:
        print("Failed to ingest data from the API.")
    else:
        print(len(raw))  # Print the length of the raw data for verification
        result = convert_to_dataframe(raw)
        save_to_csv(result, "cat_breeds.csv")

        print("Ingested data:")
        print(result)