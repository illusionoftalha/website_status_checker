import unittest
from unittest.mock import MagicMock, patch

import requests
import checker


class CheckerTests(unittest.TestCase):
    def client(self, status=200):
        client = MagicMock()
        response = client.get.return_value.__enter__.return_value
        response.status_code = status
        response.text = '<title>Example</title>'
        return client

    def test_success_has_timeout_and_closes_response(self):
        client = self.client()
        status, soup = checker.check_website_status_and_parse('https://example.com', client)
        self.assertEqual(status, 'Up')
        self.assertEqual(soup.title.text, 'Example')
        client.get.assert_called_once_with('https://example.com', timeout=(5, 15))
        client.get.return_value.__exit__.assert_called_once()

    def test_http_failure(self):
        result = checker.check_website_status_and_parse('https://example.com', self.client(503))
        self.assertEqual(result, ('Down (Status Code: 503)', None))

    def test_timeout_returns_down(self):
        client = self.client()
        client.get.side_effect = requests.exceptions.Timeout()
        self.assertEqual(checker.check_website_status_and_parse('https://example.com', client),
                         ('Down (Unable to Connect)', None))

    def test_main_reuses_and_closes_session(self):
        with patch('builtins.input', return_value='https://example.com'), \
                patch('builtins.print'), patch.object(checker.requests, 'Session') as factory, \
                patch.object(checker, 'check_website_status_and_parse', return_value=('Up', None)) as check, \
                patch.object(checker.time, 'sleep', side_effect=[None, KeyboardInterrupt]):
            checker.main()
        self.assertEqual(check.call_count, 2)
        for call in check.call_args_list:
            self.assertIs(call.args[1], factory.return_value.__enter__.return_value)
        factory.return_value.__exit__.assert_called_once()


if __name__ == '__main__':
    unittest.main()
