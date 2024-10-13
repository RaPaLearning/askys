import unittest
from merge_asky import merge_paras_with_comments, comment_to_dict

comment_json = '''
[
  {
    "paragraph": "Whatever be your environment, intend to work for Krishna.",
    "comment": "link: 11-55\\nshow: मत् कर्म कृत् mat karma kRt dedicates actions Me"
  },
  {
    "paragraph": "Step up, and recognize that you aren&#39;t the only cause of your actions.",
    "comment": "link: 8-14_to_8-15\\nshow: अधिष्ठानम् adhiSThAnam base, कर्ता kartA doer करणम् karaNam organs दैवम् daivam Divine"
  }
]'''

text_content_with_7_lines = '''
Bring the best in you
Work for Krishna inside you, instead of indulging the demands of your body, or the constraints of your environment. That’s what we explore in these three shlokas.
How do we get to know Krishna?
Step up, and recognize that you aren't the only cause of your actions.
By letting go, you give your best at present, without the limitation of the past.
Whatever be your environment, intend to work for Krishna.
Try it out now. Does it bring out the best in you?
'''

class TestMergeAsky(unittest.TestCase):

    def test_comment_converted_to_dict(self):
        source = comment_to_dict("link: 11-55\nshow: मत् कर्म कृत् [mat karma kRt] dedicates actions Me मत् परमः [mat paramaH]")
        self.assertEqual(source['link'], '11-55')
        self.assertIn('[mat karma kRt]', source['show'])
        self.assertIn('[mat paramaH]', source['show'])
        self.assertEqual(len(source['show']), 10, f"show: {source['show']}")

    def test_comments_are_merged(self):
        merged_para_comments = merge_paras_with_comments(text_content_with_7_lines, comment_json)
        self.assertEqual(len(merged_para_comments), 7)

        self.assertIn('line', merged_para_comments[0]) # at 0 is "Bring the best in you"
        self.assertNotIn('link', merged_para_comments[0])
        
        self.assertIn('link', merged_para_comments[3]) # at 3 is "Step up,..."
        self.assertIn('show', merged_para_comments[3])
        self.assertEqual('8-14_to_8-15', merged_para_comments[3]['link'])
        self.assertEqual('11-55', merged_para_comments[5]['link']) # at 5 is "Whatever be your environment..."

    def test_non_matching_comments_throw_exception(self):
        text_content = '''
first line
second line
'''
        comment_json = '''[{"paragraph": "something else", "comment": "link: 14-14\nshow: found"}]'''
        self.assertRaises(ValueError, lambda: merge_paras_with_comments(text_content, comment_json))


if __name__ == '__main__':
    unittest.main()
