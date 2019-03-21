#! /usr/bin/env python3

import mysql.connector
import pandas as pd
import credentials
import watchwords


def select_posts():
    """Finds posts to analyse (from  downloads) and returns a pandas
    dataframe with students names, posts and date.
    """
    posts_path = 'downloads/dummy_blogs.csv'
    df = pd.read_csv(posts_path)
    return df


def store_results(df):
    """Saves relvant data into MySQL database"""
    cnx = mysql.connector.connect(**mysql_config)
    pass


def main():
    select_posts()


if __name__ == '__main__':
    main()
