from SentimentAnalysis.sentiment_analysis import sentiment_analyzer as sense
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        text_1 = "I love working with Python"
        text_2 = "I hate working with Python"
        text_3 = "I am neutral on Python"
        result_1 = sense(text_1) # Positive
        result_2 = sense(text_2) # Negative
        result_3 = sense(text_3) # Neutral
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')


if __name__ == "__main__":
    unittest.main()
