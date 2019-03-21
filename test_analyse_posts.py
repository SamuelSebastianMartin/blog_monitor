#! /usr/bin/env/ python3

import unittest
import analyse_posts


class TestAnalysePost(unittest.TestCase):

    def test_unhappy(self):
        text = 'I am lonely'
        result = analyse_posts.analyse_posts(text)
        answer = 'alert'
        self.assertEqual(result, answer)

    def test_angry(self):
        text = 'I am angry'
        result = analyse_posts.analyse_posts(text)
        answer = 'alert'
        self.assertEqual(result, answer)

    def test_absolutist(self):
        text = 'All the people say everything to everyone all  \
                the time. Like everyone, every day'
        result = analyse_posts.analyse_posts(text)
        answer = 'alert'
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest(main)
