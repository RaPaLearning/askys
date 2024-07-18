import unittest
from merge_asky import merge_paras_with_comments, comment_to_dict

comment_json = '''
[
  {
    "paragraph": "Whatever be your environment, intend to work for Krishna.",
    "comment": "link: 11-55\nshow: मत् कर्म कृत् mat karma kRt dedicates actions Me"
  },
  {
    "paragraph": "Step up, and recognize that you aren&#39;t the only cause of your actions.",
    "comment": "link: 8-14_to_8-15\nshow: अधिष्ठानम् adhiSThAnam base, कर्ता kartA doer करणम् karaNam organs दैवम् daivam Divine"
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

class TestStringMethods(unittest.TestCase):

    def test_comment_converted_to_dict(self):
        source = comment_to_dict("link: 11-55,show: मत् कर्म कृत् mat karma kRt dedicates actions Me मत् परमः mat paramaH")
        self.assertEqual(source['link'], '11-55')
        self.assertEqual(len(source['show']), 13, f"show: {source['show']}")

    def test_comments_are_merged(self):
        lines_mapped_to_comments = merge_paras_with_comments(text_content_with_7_lines, comment_json)
        line_mapping_list = list(lines_mapped_to_comments)
        self.assertEqual(len(line_mapping_list), 7)

        self.assertIn('line', line_mapping_list[0]) # at 0 is "Bring the best in you"
        self.assertNotIn('link', line_mapping_list[0])
        
        self.assertIn('link', line_mapping_list[3]) # at 3 is "Step up,..."
        self.assertIn('show', line_mapping_list[3])
        self.assertEqual('8-14_to_8-15', line_mapping_list[3]['link'])
        self.assertEqual('11-55', line_mapping_list[5]['link']) # at 5 is "Whatever be your environment..."


if __name__ == '__main__':
    unittest.main()
