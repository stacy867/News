import unittest
from app.models import source
Source =source.Source


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
        
        
if __name__ == '__main__':
    unittest.main()