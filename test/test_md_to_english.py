import unittest
from md_to_english import md_to_english, md_paras_to_english_list


class TestMDtoEnglish(unittest.TestCase):

    def test_chapter_heading_removal(self):
        chapter_english = md_to_english('''# Chapter 6
Till now, The Lord spoke
''')
        self.assertIn('Till now, The Lord spoke', chapter_english)
        self.assertNotIn('Chapter 6', chapter_english)
    
    def test_shloka_meaning_extraction(self):
        shloka_english = md_to_english('''## 6-1

```shloka-sa
कार्यम् कर्म करोति यः ।
```
```shloka-sa-hk
kAryam karma karoti yaH |
```
`यः` `[yaH]` The person who `कर्म करोति` `[karma karoti]` does the work​ `कार्यम्` `[kAryam]` that's to be done''')
        self.assertEqual("The person who does the work that's to be done", shloka_english)

    def test_md_paras_to_english_list(self):
        english_paras = md_paras_to_english_list('''A person who isn’t driven by outcomes does his work as activity, 
even without the expectation that good deeds will do him good in return.
                                                 
This person works with an attitude- ‘I do this to worship the Supreme Lord’
''')
        self.assertEqual(len(english_paras), 2)


if __name__ == '__main__':
    unittest.main()
