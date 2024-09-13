import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import zscore
import os

def save_insurance_data_to_csv(text_file_path, csv_file_name='insurance_data.csv'):
    """Load insurance data from a text file and save it as a CSV."""
    # Read the text file into a DataFrame
    df = pd.read_csv(text_file_path, delimiter='|')
    
    # Create the path for the 'data' folder one level up
    data_folder = os.path.abspath(os.path.join(os.getcwd(), '..', 'data'))
    os.makedirs(data_folder, exist_ok=True)  # Create 'data' folder if it doesn't exist

    # Define the full path for the CSV file
    csv_file_path = os.path.join(data_folder, csv_file_name)
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"Data saved to {csv_file_path}")

def remove_columns(df, columns_to_remove):
    
    # Check if all columns are in the dataframe
    columns_to_remove = [col for col in columns_to_remove if col in df.columns]
    
    # Drop the columns
    df = df.drop(columns=columns_to_remove)
    
    print(f"Removed columns: {columns_to_remove}")
    
    return df
# Function to display missing values and their percentage in the DataFrame
def missing_values_table(df):
    mis_val = df.isnull().sum()
    
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    
    mis_val_dtype = df.dtypes
    
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis = 1)
    
    mis_val_table_ren_columns = mis_val_table.rename (
        columns={0: 'Missing Values', 1: '% of Total Values', 2: 'DType'}
    )
    
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
            '% of Total Values', ascending=False).round(1)
    
    print ("The dataframe has " + str(df.shape[1]) + "columns.\n"
           "There are " + str(mis_val_table_ren_columns.shape[0]) +
           " columns that have missing values.\n")
           
    return mis_val_table_ren_columns
    
# Function to drop rows with missing values in identifier columns
def handle_missing_identifiers(df, columns):
    for column in columns:
        if column in df.columns:
            initial_rows = df.shape[0]
            df.dropna(subset=[column], inplace=True)
            final_rows = df.shape[0]
            print(f"Dropped {initial_rows - final_rows} rows due to missing values in '{column}'")
    return df

# Function to fill missing values for numerical columns based on a percentage threshold
def handle_missing_numerical(df, columns, threshold=65, fill_strategy='mean'):
    for column in columns:
        if column in df.columns:
            missing_percent = df[column].isnull().sum() * 100 / len(df)
            if missing_percent > threshold:
                df.drop(column, axis=1, inplace=True)
                print(f"Dropped column '{column}' due to {missing_percent:.1f}% missing values")
            else:
                if fill_strategy == 'mean':
                    df[column].fillna(df[column].mean(), inplace=True)
                elif fill_strategy == 'median':
                    df[column].fillna(df[column].median(), inplace=True)
                print(f"Filled missing values in '{column}' using {fill_strategy}")
    return df

# Function to fill missing values for categorical columns with 'Unknown'
def handle_missing_categorical(df, columns, fill_value='Unknown'):
    for column in columns:
        if column in df.columns:
            df[column].fillna(fill_value, inplace=True)
            print(f"Missing values in categorical column '{column}' filled with '{fill_value}'")
    return df

def fix_outlier(df, columns):
    
    for column in columns:
        if column in df.columns:
            # Calculate 95th percentile and median
            percentile_95 = df[column].quantile(0.95)
            median_value = df[column].median()
            
            # Replace values higher than 95th percentile with median
            df[column] = np.where(df[column] > percentile_95, median_value, df[column])
           # print(f"Outliers in column {column} fixed (values above 95th percentile replaced with median).")
    
    return df

def remove_outliers(df, columns_to_process, z_threshold=3):

    for column in columns_to_process:
        if column in df.columns:
            z_scores = zscore(df[column])
            outlier_column = column + '_Outlier'
            
            # Flag rows as outliers
            df[outlier_column] = (np.abs(z_scores) > z_threshold).astype(int)
            
            # Filter out the rows with outliers
            df = df[df[outlier_column] == 0]
            
            # Drop the outlier flag column
            df = df.drop(columns=[outlier_column], errors='ignore')
            #print(f"Outliers removed from column {column} based on Z-score threshold of {z_threshold}.")
    
    return df

# Function to identify categorical columns in a DataFrame
def get_categorical_columns(df):
    categorical_columns = df.select_dtypes(include=['object', 'category','bool']).columns.tolist()
    return categorical_columns

# # Function to get unique values and their counts from categorical columns
# def get_unique_values_count(df, categorical_columns):
#     unique_values_count = {}
    
#     for col in categorical_columns:
#         unique_vals = df[col].value_counts()
#         unique_values_count[col] = unique_vals
    
#     return unique_values_count


# Function to get unique values and their counts from categorical columns
import pandas as pd

def get_unique_values_count(df, categorical_columns):
    result = []
    
    for col in categorical_columns:
        unique_vals = df[col].value_counts(normalize=True)
        
        for value, percentage in unique_vals.items():
            count = int(df[col].eq(value).sum())
            
            result.append({
                'Column': col,
                'Unique Value': value,
                'Count': count,
                'Percentage': round(percentage * 100, 2)
            })
    
    df_result = pd.DataFrame(result)
    
    # Sort by Column and Count descending
    df_result = df_result.sort_values(['Column', 'Count'], ascending=[True, False])
    
    return df_result

def update_gender_based_on_title(df, title_column, gender_column):
    """
    Update the Gender column based on the Title column when Gender is 'Not specified'.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    title_column (str): Name of the column containing titles
    gender_column (str): Name of the column containing genders
    
    Returns:
    pd.DataFrame: Modified DataFrame with updated Gender column
    """
    try:
        # Check if both columns exist in the DataFrame
        if title_column not in df.columns or gender_column not in df.columns:
            raise ValueError(f"Both '{title_column}' and '{gender_column}' must exist in the DataFrame.")
        
        # Create a dictionary mapping titles to genders
        title_gender_map = {
            'Mr': 'Male',
            'Mrs': 'Female',
            'Ms': 'Female',
            'Miss': 'Female'
        }
        
        # Create a mask for rows where Gender is 'Not specified'
        mask = df[gender_column] == 'Not specified'
        
        # Apply the mapping to the masked rows
        df.loc[mask, gender_column] = df.loc[mask, title_column].map(title_gender_map).fillna(df.loc[mask, gender_column])
        
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def update_marital_status_based_on_title(df, title_column, marital_status_column):
    """
    Update the MaritalStatus column based on the Title column when MaritalStatus is 'Not specified'.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    title_column (str): Name of the column containing titles
    marital_status_column (str): Name of the column containing marital statuses
    
    Returns:
    pd.DataFrame: Modified DataFrame with updated MaritalStatus column
    """
    try:
        # Check if both columns exist in the DataFrame
        if title_column not in df.columns or marital_status_column not in df.columns:
            raise ValueError(f"Both '{title_column}' and '{marital_status_column}' must exist in the DataFrame.")
        
        # Create a dictionary mapping titles to marital statuses
        title_marital_map = {
            'Miss': 'Single',
            'Mrs': 'Married'
        }
        
        # Create a mask for rows where MaritalStatus is 'Not specified'
        mask = df[marital_status_column] == 'Not specified'
        
        # Apply the mapping to the masked rows
        df.loc[mask, marital_status_column] = df.loc[mask, title_column].map(title_marital_map).fillna(df.loc[mask, marital_status_column])
        
        return df
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None