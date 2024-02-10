import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      dataPoint = (quote.get('stock'), quote.get('top_bid').get('price'), quote.get('top_ask').get('price'), (quote.get('top_ask').get('price') + quote.get('top_bid').get('price'))/2)
      self.assertEqual(getDataPoint(quote),dataPoint)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      dataPoint = (quote.get('stock'), quote.get('top_bid').get('price'), quote.get('top_ask').get('price'), (quote.get('top_ask').get('price') + quote.get('top_bid').get('price'))/2)
      self.assertEqual(getDataPoint(quote),dataPoint)

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatioBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      if(quote['top_bid']['price'] == 0):
        Ratio = None
      else:
        Ratio = quote['top_ask']['price']/quote['top_bid']['price']
      self.assertEqual(getRatio(quote['top_ask']['price'],quote['top_bid']['price']),
                       Ratio)

  def test_getRatio_calculateRatioBidPriceZero(self):
    quotes = [
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      if(quote['top_bid']['price'] == 0):
        Ratio = None
      else:
        Ratio = quote['top_ask']['price']/quote['top_bid']['price']
      self.assertEqual(getRatio(quote['top_ask']['price'],quote['top_bid']['price']),
                       Ratio)

  def test_getRatio_calculateRatioAskPriceZero(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    ]
    for quote in quotes:
      if(quote['top_bid']['price'] == 0):
        Ratio = None
      else:
        Ratio = quote['top_ask']['price']/quote['top_bid']['price']
      self.assertEqual(getRatio(quote['top_ask']['price'],quote['top_bid']['price']),
                       Ratio)


if __name__ == '__main__':
    unittest.main()
