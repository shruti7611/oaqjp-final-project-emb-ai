
import unittest
from unittest.mock import patch, Mock

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("emotion_detection.requests.post")
    def test_dominant_anger(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.8,
                    "disgust": 0.1,
                    "fear": 0.05,
                    "joy": 0.02,
                    "sadness": 0.03
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am very angry")

        self.assertEqual(result["dominant_emotion"], "anger")
        self.assertEqual(result["anger"], 0.8)
        self.assertIn("disgust", result)
        self.assertIn("fear", result)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)

    @patch("emotion_detection.requests.post")
    def test_bad_request(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])


if __name__ == "__main__":
    unittest.main()
