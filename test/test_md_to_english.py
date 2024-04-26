import unittest
from md_to_english import md_to_english, md_paras_to_english_list, mds_to_english_dict


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
कार्यम् कर्म करोति यः ।।
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

    def test_removal_of_anchor_and_explanation(self):
        english = md_to_english('''He also asks about the conduct of a person who is firm in wisdom.

<a name='sthitaprajna_xlat'></a>
_Being 'firm in wisdom' is to be engaged in an inquiry into the Self, cultivating true knowledge. The term 'firm in wisdom' is used as the translation for 
`स्थितप्रज्ञ` `[sthitaprajJa]`.
Other ways of translating the word 
`स्थितप्रज्ञ` `[sthitaprajJa]`
 are: 'one whose consciousness is fully realized'_
''')
        self.assertEqual('He also asks about the conduct of a person who is firm in wisdom.', english.strip())

    def test_retention_of_hyperlink_text(self):
        english_list = md_paras_to_english_list('''We call it ‘
[yoga](6-20_to_6-23.md#yoga_state_of_being)
’. This is explained as [Karmayoga](2-40.md#karmayoga).''')
        self.assertEqual('We call it ‘ yoga ’. This is explained as Karmayoga.', english_list[0].strip())

    def test_md_files_to_english_list_in_dict(self):
        english_dict = mds_to_english_dict('test')
        self.assertIsInstance(english_dict, dict)
        self.assertIn('6-1.md', english_dict)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
