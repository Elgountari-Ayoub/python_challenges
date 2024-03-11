import pandas as pd
import os


class DataProcessor:
    """
    This class processes data files including reading, schema detection,
    transformation, and uploading to desired storage format.
    """

    def __init__(self):
        """
        Initialize the DataProcessor object with an empty file path and data.
        """
        self.file_path = None
        self.data = None

    def read_file(self):
        """
        Continuously prompts the user for a file path until a valid file is provided.
        Supports CSV, Parquet, and Excel formats.
        """
        while True:
            try:
                file_path = input("Enter file path: ")
                if os.path.isfile(file_path):
                    self.file_path = file_path
                    if self.file_path.endswith('.csv'):
                        self.data = pd.read_csv(self.file_path)
                    elif self.file_path.endswith('.parquet'):
                        self.data = pd.read_parquet(self.file_path)
                    elif self.file_path.endswith('.xlsx'):
                        self.data = pd.read_excel(self.file_path)
                    else:
                        print(
                            "Unsupported file format. Please provide a file with format .csv, .parquet, or .xlsx."
                        )
                        continue
                    break
                else:
                    print("Invalid file path. Please enter a valid file path.")
            except Exception as e:
                print(f"Error reading file: {e}")

    def detect_schema(self):
        """
        Prints the data schema (data types of each column) if data is loaded successfully.
        """
        try:
            print(self.data.dtypes)
        except Exception as e:
            print(f"Error detecting schema: {e}")

    def transform_to_table(self):
        """
        Transforms the loaded data into a pandas DataFrame object.
        """
        try:
            return pd.DataFrame(self.data)
        except Exception as e:
            print(f"Error transforming data to table: {e}")

    def choose_storage_format(self):
        """
        Continuously prompts the user to choose a storage format (CSV, Parquet, or Excel) until a valid choice is made.
        """
        while True:
            try:
                choice = input(
                    "Choose storage format (CSV, Parquet, or Excel): ").lower()
                if choice in ['csv', 'parquet', 'excel']:
                    return choice
                else:
                    print("Invalid choice. Please choose from CSV, Parquet, or Excel.")
            except Exception as e:
                print(f"Error choosing storage format: {e}")

    def upload_file(self, storage_format):
        """
        Prompts the user for a filename (without extension) and path to upload the processed data.
        Supports uploading to the chosen storage format (CSV, Parquet, or Excel).
        """

        file_name = input(
            "Enter the name for the output file (without extension): ")
        while True:
            try:
                file_path = input(
                    "Enter the path where you want to save the file: ")

                if storage_format == 'csv':
                    self.data.to_csv(os.path.join(
                        file_path, file_name + '.csv'), index=False)

                elif storage_format == 'parquet':
                    self.data.to_parquet(os.path.join(
                        file_path, file_name + '.parquet'), index=False)
                elif storage_format == 'excel':
                    self.data.to_excel(os.path.join(
                        file_path, file_name + '.xlsx'), index=False)

                print("File uploaded successfully.")
                break
            except Exception as e:
                print(f"Error uploading file: {e}")
