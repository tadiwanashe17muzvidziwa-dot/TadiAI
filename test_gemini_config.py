import unittest

from app.services import gemini


class GeminiConfigTest(unittest.TestCase):
    def test_default_model_is_supported(self):
        self.assertIn(gemini.MODEL_NAME, {"gemini-2.0-flash", "gemini-2.5-flash"})


if __name__ == "__main__":
    unittest.main()
