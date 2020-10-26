# Import packages
import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """"
     Load the message and categories data and merge them into one 
     
     Args:
     messages_filepath :  string , CSV File path for message file 
     categories_filepath: string , CSV File path for categories file
     
     Returns:
     df: panda dataframe , This dataframe will contain merge data of message and categpries 
     """
    # Load messages dataset
    messages = pd.read_csv(messages_filepath)
    
    # Load categories dataset
    categories = pd.read_csv(categories_filepath)
    
    # Merge datasets
    df = messages.merge(categories, how = 'left', on = ['id'])
    
    return df
     


def clean_data(df):
    """Clean dataframe by removing duplicates and converting categories from strings 
    to binary values.
    
    Args:
    df: dataframe. Dataframe containing merged content of messages and categories datasets.
       
    Returns:
    df: dataframe. after necessary cleaning
    
    """
    # Create a dataframe of the  individual category columns
    categories = df['categories'].str.split(';', expand = True)
    
    # select the first row of the categories dataframe
    row = categories.iloc[0]

    # use this row to extract a list of new column names for categories.
    # applying a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = row.transform(lambda x: x[:-2]).tolist()
    
    # Rename the columns of `categories`
    categories.columns = category_colnames
    
    ## Convert category values to just numbers 0 or 1.
    
    for column in categories:
    # set each value to be the last character of the string
       categories[column] = categories[column].transform(lambda x: x[-1:])
    
    # convert column from string to numeric
       categories[column] = pd.to_numeric(categories[column])
    
    # drop the original categories column from `df`
    df.drop('categories', axis = 1, inplace = True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis = 1)
    
    # drop duplicates
    df.drop_duplicates(inplace = True)
    
    # Remove rows with a related value of 2 from the dataset
    df = df[df['related'] != 2]
    
    ## returning data frame 
    return df  

def save_data(df, database_filename):
    """Save cleaned data into an SQLite database.
    
    Args:
    df: dataframe. Dataframe containing cleaned version of merged message and 
    categories data.
    database_filename: string. Filename for output database.
       
    Returns:
    None
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('Messages', engine, index=False, if_exists='replace')

def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()