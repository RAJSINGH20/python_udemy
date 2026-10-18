import unittest

from main import build_payload


class BuildPayloadTests(unittest.TestCase):
    def test_build_payload_contains_system_and_user_messages(self):
        payload = build_payload("hello", "You are helpful.")

        self.assertEqual(payload["model"], "deepseek-r1:1.5b")
        self.assertFalse(payload["stream"])
        self.assertEqual(
            payload["messages"],
            [
                {"role": "system", "content": "You are helpful."},
                {"role": "user", "content": "hello"},
            ],
        )


if __name__ == "__main__":
    unittest.main()
