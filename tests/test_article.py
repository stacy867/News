import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    test class to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_article= Article('Jennings Brown','What to Do When You Receive','https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','On Monday, YouTube filed a lawsuit against one of its users for  extorting others','2019-08-21T20:31:00Z','https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        self.assertEqual(self.new_article.author,"Jennings Brown")
        self.assertEqual(self.new_article.tittle,"What to Do When You Receive")
        self.assertEqual(self.new_article.imageurl,"https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png")
        self.assertEqual(self.new_article.description,"On Monday, YouTube filed a lawsuit against one of its users for  extorting others")
        self.assertEqual(self.new_article.time,"2019-08-21T20:31:00Z")
        self.assertEqual(self.new_article.url,"https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816")    

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        ''' 
        Article.articles= []   
    
# if __name__ == '__main__':
#     unittest.main()