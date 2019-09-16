import unittest
from app.models import Source
# Source =source.Source


class SourceTest(unittest.TestCase):
    '''
    test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Source(1,'ABC News','us','https://abcnews.go.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
    def test_init(self):
        def test_init(self):
            self.assertEqual(self.new_source.id,1)
            self.assertEqual(self.new_source.name,"ABC News")
            self.assertEqual(self.new_source.description,"us")
            self.assertEqual(self.new_article.sourceurl,"https://abcnews.go.com")

        
       
        
# if __name__ == '__main__':
#     unittest.main()