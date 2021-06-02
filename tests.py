import unittest
from main import (
    read_file, get_keywords_translation,
    answer_questions, get_price_struct,
) 


class TestFunctions(unittest.TestCase):
    struct = {
        'keywords': [   
            'glob is I',
            'prok is V',
            'pish is X',
            'tegj is L',
        ],
        'questions': [
            'how much is pish tegj glob glob ?',
            'how many Credits is glob prok Silver ?',
            'how many Credits is glob prok Gold ?',
            'how many Credits is glob prok Iron ?',
            'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?',
        ],
        'prices': [    
            'glob glob Silver is 34 Credits',
            'glob prok Gold is 57800 Credits',
            'pish pish Iron is 3910 Credits',
        ],
    }
    answers = [ 
        'pish tegj glob glob is 42',
        'glob prok Silver is 68 Credits',
        'glob prok Gold is 57800 Credits',
        'glob prok Iron is 782 Credits',
        'I have no idea what you are talking about',
    ]
    

    def test_read_file(self):
        file_struct = read_file('input.txt')
        self.assertEqual(file_struct, self.struct)

    def test_get_keywords_translation(self):
        words_index = get_keywords_translation(self.struct.get('keywords'))
        self.assertTrue(words_index)

    def test_get_price_struct(self):
        price_table = get_price_struct(get_keywords_translation(self.struct.get('keywords')), self.struct.get('prices'))
        self.assertTrue(price_table)

    def test_answer_questions(self):
        words_index = get_keywords_translation(self.struct.get('keywords'))
        price_table = get_price_struct(get_keywords_translation(self.struct.get('keywords')), self.struct.get('prices'))
        answers = answer_questions(self.struct.get('questions'), words_index, price_table)
        self.assertEqual(answers, self.answers)


if __name__ == '__main__':
    unittest.main()
