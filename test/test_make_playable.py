import unittest
from make_playable import make_playable_dir_name

class TestPlayable(unittest.TestCase):

    def test_playable_dir_name(self):
        dir_name = make_playable_dir_name([{
            'line': 'Bring the best in you',
        }])
        self.assertEqual(dir_name, 'bring_the_best_in_you')

    def test_playable_dir_name_with_punctuation(self):
        dir_name = make_playable_dir_name([{
            'line': 'Why hesitate?',
        }])
        self.assertEqual(dir_name, 'why_hesitate')
