import pandas as pd
import json

class SocialShieldLoader:
    def __init__(self, dataset_path="socialshield/datasets"):
        self.dataset_path = dataset_path

    def load_scams(self, filename="scams.csv"):
        """
        Load scam data from a CSV file.

        Parameters:
        - filename (str): The name of the CSV file.

        Returns:
        - pd.DataFrame: A Pandas DataFrame containing the loaded data.
        """
        file_path = f"{self.dataset_path}/{filename}"
        try:
            df = pd.read_csv(file_path)
            print(f"Scam data loaded successfully from {file_path}")
            return df
        except FileNotFoundError:
            print(f"Error: {filename} not found at {file_path}")
            return None

    def load_binetwork(self, filename="BiNetwork50.json"):
        """
        Load BiNetwork data from a JSON file.

        Parameters:
        - filename (str): The name of the JSON file.

        Returns:
        - dict: A dictionary containing the loaded data.
        """
        file_path = f"{self.dataset_path}/{filename}"
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                print(f"BiNetwork data loaded successfully from {file_path}")
                return data
        except FileNotFoundError:
            print(f"Error: {filename} not found at {file_path}")
            return None


if __name__ == "__main__":
    social_shield_loader = SocialShieldLoader()

    # Load scam data
    scam_data = social_shield_loader.load_scams()
    if scam_data is not None:
        print(scam_data.head())

    # Load BiNetwork data
    binetwork_data = social_shield_loader.load_binetwork()
    if binetwork_data is not None:
        # Do something with the loaded BiNetwork data
        print(binetwork_data)