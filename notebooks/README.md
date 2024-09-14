Data Processing Script
This script provides a set of functions for processing and cleaning insurance data in CSV and text file formats. It includes functionalities to handle missing values, outliers, and to update certain columns based on the values of other columns.

Table of Contents
Functions
Usage
Requirements
Contributing
Functions

1. save_insurance_data_to_csv(text_file_path, csv_file_name='insurance_data.csv')
   Description: Loads insurance data from a text file and saves it as a CSV file.
   Parameters:
   text_file_path: Path to the text file with insurance data.
   csv_file_name: Name of the output CSV file (default: 'insurance_data.csv').
2. remove_columns(df, columns_to_remove)
   Description: Removes specified columns from the DataFrame.
   Parameters:
   df: The input DataFrame.
   columns_to_remove: List of columns to be removed.
3. missing_values_table(df)
   Description: Displays a table of missing values and their percentage in the DataFrame.
   Parameters:
   df: The input DataFrame.
   Returns: DataFrame with columns showing the missing values, percentage of total values, and data types.
4. handle_missing_identifiers(df, columns)
   Description: Drops rows with missing values in specified identifier columns.
   Parameters:
   df: The input DataFrame.
   columns: List of identifier columns to check for missing values.
5. handle_missing_numerical(df, columns, threshold=65, fill_strategy='mean')
   Description: Handles missing values in numerical columns based on a percentage threshold. Can either drop columns with excessive missing values or fill them with mean or median values.
   Parameters:
   df: The input DataFrame.
   columns: List of numerical columns to process.
   threshold: Percentage threshold above which columns will be dropped (default: 65).
   fill_strategy: Strategy to fill missing values ('mean' or 'median', default: 'mean').
6. handle_missing_categorical(df, columns, fill_value='Unknown')
   Description: Fills missing values in categorical columns with a specified value.
   Parameters:
   df: The input DataFrame.
   columns: List of categorical columns to process.
   fill_value: Value to replace missing values (default: 'Unknown').
7. fix_outlier(df, columns)
   Description: Replaces outliers in specified columns with the median value of the column.
   Parameters:
   df: The input DataFrame.
   columns: List of columns to process.
8. remove_outliers(df, columns_to_process, z_threshold=3)
   Description: Removes rows with outliers in specified columns based on Z-score threshold.
   Parameters:
   df: The input DataFrame.
   columns_to_process: List of columns to check for outliers.
   z_threshold: Z-score threshold above which rows will be considered outliers (default: 3).
9. get_categorical_columns(df)
   Description: Identifies categorical columns in a DataFrame.
   Parameters:
   df: The input DataFrame.
   Returns: List of categorical columns.
10. get_unique_values_count(df, categorical_columns)
    Description: Gets unique values and their counts from categorical columns.
    Parameters:
    df: The input DataFrame.
    categorical_columns: List of categorical columns to process.
    Returns: DataFrame with unique values, their counts, and percentages.
11. update_gender_based_on_title(df, title_column, gender_column)
    Description: Updates the Gender column based on the Title column when Gender is 'Not specified'.
    Parameters:
    df: The input DataFrame.
    title_column: Column name containing titles.
    gender_column: Column name containing genders.
    Returns: Modified DataFrame with updated Gender column.
12. update_marital_status_based_on_title(df, title_column, marital_status_column)
    Description: Updates the MaritalStatus column based on the Title column when MaritalStatus is 'Not specified'.
    Parameters:
    df: The input DataFrame.
    title_column: Column name containing titles.
    marital_status_column: Column name containing marital statuses.
    Returns: Modified DataFrame with updated MaritalStatus column.
