import roman
import argparse


def read_file(input_file):
    file_struct = {
        'keywords': [],
        'questions': [],
        'prices': [],
    }
    with open(input_file) as file:
        for i in file:
            line = i.strip()
            if '?' in line:
                file_struct.get('questions').append(line)
            elif 'Credits' in line[-7:] and 'is' in line:
                file_struct.get('prices').append(line)
            elif line[-1] in 'IVXLCDM' and 'is' in line:
                file_struct.get('keywords').append(line)
            else:
                file_struct.get('errors').append(line)
    return file_struct


def get_keywords_translation(keywords: list[str]):
    keywords_list = [i.split(' is ') for i in keywords]
    return keywords_list


def translate_number(number_list: list[str], words_index: list[list]):
    new_number = ''
    for number in number_list:
        for i, j in words_index:
            number = number.replace(i, j)
        new_number += number
    return roman.fromRoman(new_number)


def get_price_struct(words_index: list[dict], baseprices: list[dict]):
    price_list = [
        {
            'price': translate_number(i.split(' is')[0].split()[:-1], words_index), 
            'total_credits': i.split(' is')[1].split()[0],
            'type': i.split(' is')[0].split()[-1]
        } for i in baseprices
    ]
    return {i.get('type'): float(i.get('total_credits'))/float(i.get('price')) for i in price_list}


def answer_questions(questions: dict, words_index: list[list], price_table: dict):
    answers = []
    for question in questions:
        if 'how much is' in question:
            alien_number = question.split()[3:-1]
            number = translate_number(alien_number, words_index)
            answers.append(f"{' '.join(alien_number)} is {number}")
        elif 'how many Credits' in question:
            alien_number = question.split()[4:-2]
            number = translate_number(alien_number, words_index)
            current_coin = question.split()[-2]
            current_price = price_table.get(current_coin)
            answers.append(f"{' '.join(alien_number)} {current_coin} is {(number*current_price):.0f} Credits")
        else:
            answers.append('I have no idea what you are talking about')
    return answers


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file path input goes here")
    args = parser.parse_args()
    try:
        struct = read_file(args.file)
    except Exception:
        raise Exception('Error reading file, please verify if file is correct')
    words_index = get_keywords_translation(struct.get('keywords'))
    price_table = get_price_struct(words_index, struct.get('prices'))
    answers = answer_questions(struct.get('questions'), words_index, price_table)
    for answer in  answers:
        print(answer)


if __name__ == '__main__':
    run()
