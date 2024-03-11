**Introduction**

This Python script provides a data processor tool to read various file formats (CSV, Parquet, Excel), explore the data schema, and convert it into a table before saving it in your chosen path and format (CSV, Parquet, or Excel).

**How to Use**

1.  **Run the Script:**
    ```bash
    python main.py
    ```

2.  **Enter File Path:**
    The script will prompt you to enter the file path of the data you want to process. Ensure the file has a valid extension (CSV, Parquet, Excel).

3.  **Explore Schema (Optional):**
    Once the file is read successfully, you'll have the option to view the data schema (data types of each column).

4.  **Transform to Table:**
    The script transforms the data into a pandas DataFrame for further manipulation (optional).

5.  **Choose Storage Format:**
    Select your preferred output format (CSV, Parquet, or Excel) for saving the processed data.

6.  **Enter Output Details:**
    Provide a name for the output file (without extension) and the desired path to save the file.

**Requirements**

This script relies on the following external libraries:

* pandas
* pyarrow

**Installation**

You can install the required libraries using pip:

```bash
pip install pandas
pip install pyarrow
```

**Example Usage**

Suppose you have a CSV file named `data.csv` located on your desktop. Here's a sample interaction with the script:

```
Enter file path: /Users/your_username/Desktop/data.csv
... (data schema is displayed if you choose to view it)
Choose storage format (CSV, Parquet, or Excel): csv
Enter the name for the output file (without extension): processed_data
Enter the path where you want to save the file: /Users/your_username/Documents
File uploaded successfully.
```

This will process the `data.csv` file, display the schema (if chosen), convert it to a table, and save it as `processed_data.csv` in your Documents folder.

**Further Notes**

* Feel free to modify the script to suit your specific data processing needs.
* For extended functionalities, explore the capabilities of the pandas library.

**requirements.txt**

pandas
pyarrow

This `requirements.txt` file specifies the required library (`pandas`) for running the script. You can install these libraries using `pip install -r requirements.txt`.
