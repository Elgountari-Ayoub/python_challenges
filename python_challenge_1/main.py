from utils.data_processor import DataProcessor

def main():
    data_processor = DataProcessor()
    data_processor.read_file()
    if data_processor.data is not None:
        schema = data_processor.detect_schema()
        table = data_processor.transform_to_table()
        storage_format = data_processor.choose_storage_format()
        if storage_format is not None:
            data_processor.upload_file(storage_format)

if __name__ == "__main__":
    main()
