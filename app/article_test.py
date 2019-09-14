import unittest
from models import article
Article=article.Article

class ArticleTest(unittest.TestCase):
    '''
    test class to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_article= Article(1,'Douglas Charles','Kendall Jenner Now Linked To Kelly Oubre; Donovan Mitchell Beefs With Trolls; And More News You Can Use','We can not cover every story','https://brobible.files.wordpress.com/2019/09/todays-best-links-internet-091319.jpg?quality=90&w=650')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
if __name__ == '__main__':
    unittest.main()