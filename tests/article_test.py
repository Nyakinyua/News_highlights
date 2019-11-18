import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_article=Articles((id,name,author,title,description,url,urlToImage,publishedAt,content))
