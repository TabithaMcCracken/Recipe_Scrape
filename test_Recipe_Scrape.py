import unittest
from unittest.mock import patch
import Recipe_Scrape

class TestRecipe_Scrape(unittest.TestCase):

    # Test get_user_ingredients function
    @patch('builtins.input', side_effect=['tomato', 'N'])
    def test_get_user_ingredients(self, mock_input):
        result = Recipe_Scrape.get_user_ingredients()
        self.assertEqual(result, ['tomato'])

    # Test scrape_website function
    @patch('requests.get')
    def test_scrape_website(self, mock_get):
        class MockResponse:
            status_code = 200
            text = "test content"
        
        mock_get.return_value = MockResponse()
        saved_content = Recipe_Scrape.scrape_website("https://testurl.com")
        
        print(saved_content)

        self.assertEqual(saved_content, "test content")

    # Test if content is saved to the file
    def test_save_to_file(self):
        test_content = "<html><body>Test Content</body></html>"

        # Call the function to save content to file
        Recipe_Scrape.save_to_file(test_content)
        
        # Read the saved file
        with open('scraped_content.html', 'r') as file:
            saved_content = file.read()
        
        # Assert that the saved content matches the test content
        self.assertEqual(saved_content, test_content)

    # Test get_links function
    @patch('requests.get')
    def test_get_links(self, mock_get):
        mock_response = """
        <html>
            <body>
                <a href="link1.html"></a>
                <a href="link2.html"></a>
            </body>
        </html>
        """

        mock_get.return_value.content = mock_response.encode()
        result = Recipe_Scrape.get_links("https://testurl.com")
        expected_links = [
            "https://codingnomads.github.io/recipes/link1.html",
            "https://codingnomads.github.io/recipes/link2.html"
        ]
        self.assertEqual(result, expected_links)

    # Test scrape_links function (this is a simplified test and might not cover all scenarios)
    @patch('requests.get')
    def test_scrape_links(self, mock_get):
        class MockResponse:
            content = "<html><body>tomato potato</body></html>".encode()

        mock_get.return_value = MockResponse()
        result = Recipe_Scrape.scrape_links(
            ["https://codingnomads.github.io/recipes/test.html"], ["tomato", "potato"])
        self.assertEqual(result, ["https://codingnomads.github.io/recipes/test.html"])


if __name__ == '__main__':
    unittest.main()
