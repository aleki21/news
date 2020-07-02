import unittest
from models import news
News = news.News

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(null,'Chain Reaction - Kelvin Koh: Spartan Group\'s Relentless Search For Alpha','https://letstalkbitcoin.com/blog/post/chain-reaction-kelvin-koh-spartan-group-relentless-search-alpha?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheDailyBitcoinShow+%28Let%27s+Talk+Bitcoin+Network+Feed%29','https://letstalkbitcoin.com/files/blogs/8726-9222833e43001ded1ce1ef00ab4a7766057648848b08956768e52505cf654a5e.jpg','2020-07-02T14:26:00Z')

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()