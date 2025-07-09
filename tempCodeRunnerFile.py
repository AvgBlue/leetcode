import unittest
from test.q2 import solution

class TestSolution(unittest.TestCase):
    def test_balanced_moves_returns_true(self):
        self.assertTrue(solution("><^v"))
        self.assertTrue(solution("><^v><^v"))
        self.assertTrue(solution("^>v<"))
        self.assertTrue(solution("^^vv<<>>"))

    def test_unbalanced_moves_returns_false(self):
        self.assertFalse(solution("><^"))
        self.assertFalse(solution("^^vv<<>"))
        self.assertFalse(solution("^^vv<<>>^"))
        self.assertFalse(solution(">v<"))

    def test_no_moves_returns_false(self):
        self.assertFalse(solution(""))

    def test_only_one_direction_returns_false(self):
        self.assertFalse(solution(">>>>"))
        self.assertFalse(solution("vvvv"))
        self.assertFalse(solution("^^^^"))
        self.assertFalse(solution("<<<<"))

    def test_returns_to_origin_before_end_returns_false(self):
        # Returns to origin before the last move
        self.assertFalse(solution(">v<^>v<^"))

    def test_never_returns_to_origin_returns_false(self):
        self.assertFalse(solution(">^>^<v<"))

    def test_minimum_valid_cycle(self):
        self.assertTrue(solution(">v<^"))

    def test_invalid_characters(self):
        # Should ignore or fail gracefully if invalid chars present
        self.assertFalse(solution(">v<^x"))
        self.assertFalse(solution("abcde"))

if __name__ == "__main__":
    unittest.main()