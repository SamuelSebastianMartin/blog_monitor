#! /usr/bin/env/ python3

import unittest
import analyse_posts


class TestAnalysePost(unittest.TestCase):

    def test_unhappy(self):
        text = 'I am suicidal'
        result = analyse_posts.analyse_posts(text)
        answer = 'alert'
        self.assertEqual(result, answer)

    def test_sad(self):
        text = 'I am sad'
        result = analyse_posts.analyse_posts(text)
        answer = 'alert'
        self.assertEqual(result, answer)

    def test_absolutist(self):
        text = 'Everyone is definitely always totally absolute'
        result = analyse_posts.analyse_posts(text)
        answer = 'alert'
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest(main)
