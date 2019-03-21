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


def analyse_posts(message):
    return 'alert'


def alert_process(db_row):
    print('Alert Process')

def main():
    db = select_posts()
    for n in range(len(db)):
        message = db['Message'][n]
        if analyse_posts(message) == 'non-alert':
            continue
        elif analyse_posts(message) != 'alert':
            raise Exception('Confused alert message: {}: {}'
                    .format(db['Author'][n], db['Date'][n]))
        else:
            alert_process(db.iloc[n])


if __name__ == '__main__':
    main()
