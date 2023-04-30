import re


def create_list_from_text_file(path):
    list_from_file = []
    try:
        with open(path, 'r', encoding='utf8') as file_handle:
            for line in file_handle:
                line = line.strip().lower()
                my_list = line.split(' ')
                for word in my_list:
                    word = re.sub(r'[\W_]+', '', word)
                    if word != '':
                        list_from_file.append(word)
    except FileNotFoundError as err:
        print(err)
        return False
    return list_from_file


if __name__ == '__main__':
    words = create_list_from_text_file('pan-tadeusz.txt')
    print(words[0], words[1])
