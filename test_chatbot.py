import unittest

from chatbot import extract_video_id


class TestExtractVideoID(unittest.TestCase):
    def test_raw_video_id(self) -> None:
        self.assertEqual(extract_video_id("dQw4w9WgXcQ"), "dQw4w9WgXcQ")

    def test_watch_url(self) -> None:
        self.assertEqual(
            extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
            "dQw4w9WgXcQ",
        )

    def test_short_url(self) -> None:
        self.assertEqual(extract_video_id("https://youtu.be/dQw4w9WgXcQ"), "dQw4w9WgXcQ")

    def test_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            extract_video_id("https://example.com/not-youtube")


if __name__ == "__main__":
    unittest.main()
