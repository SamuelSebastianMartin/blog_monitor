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
    cnx = mysql.connector.connect(**credentials.mysql_config)
    cnx.close()


def analyse_posts(message):
    """Examines the content of the journal post.
    Returns 'alert' for posts with concerning content;
    Returns 'non-alert' for non-concerning posts.
    """
    return 'alert'


def alert_process(df_row):
    """Raises an alert when a journal post has concerning content."""
    print('Alert Process')
    print(df_row)

def main():
    df = select_posts()
    for n in range(len(df)):
        message = df['Message'][n]
        if analyse_posts(message) == 'non-alert':
            continue
        elif analyse_posts(message) != 'alert':
            raise Exception('Confused alert message: {}: {}'
                    .format(df['Author'][n], df['Date'][n]))
        else:
            alert_process(df.iloc[n])
    store_results(df)

if __name__ == '__main__':
    main()
