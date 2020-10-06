import unittest

from com.dakshata.autotrader.api.AutoTrader import AutoTrader

class TestAutoTrader(unittest.TestCase):

    __PROD_SERVER = 'https://stocksdeveloper.in:9017/'
    
    __TEST_SERVER = 'http://localhost:9017'

    def test_place_regular_order(self):
        """
        Test placing a regular order.
        """
        api = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        
        result = api.place_regular_order('159401', 'NSE', 'WIPRO', 'BUY', 'LIMIT', 'INTRADAY', 1, 330.35, 0.0)
        
        # print(result)
        
        self.assertTrue(result.success())
        
        self.assertIsNotNone(result.result)
        
        self.assertNotEqual('', result.result)

    def test_place_bracket_order(self):
        """
        Test placing a bracket order.
        """
        api = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        
        result = api.place_bracket_order('159401', 'NSE', 'WIPRO', 'SELL', 'LIMIT', 1, 326.35, 0.0, 1, 1, 0)
        
        # print(result)
        
        self.assertTrue(result.success())
        
        self.assertIsNotNone(result.result)
        
        self.assertNotEqual('', result.result)
        

    def test_place_cover_order(self):
        """
        Test placing a cover order.
        """
        api = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        
        result = api.place_cover_order('159401', 'NSE', 'SBIN', 'SELL', 'LIMIT', 1, 188.15, 190.0)
        
        # print(result)
        
        self.assertTrue(result.success())
        
        self.assertIsNotNone(result.result)
        
        self.assertNotEqual('', result.result)
        
    def test_read_platform_margins(self):
        """
        Test reading margins data.
        """
        api = AutoTrader.create_instance('b25f5e2f-93cb-430e-a81d-f960a490034f', TestAutoTrader.__TEST_SERVER)
        
        result = api.read_platform_margins('159401')
        
        # print(result)
        
        print(*result.result, sep = "\n") 
    
if __name__ == '__main__':
    unittest.main()