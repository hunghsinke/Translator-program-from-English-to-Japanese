from translate import Translator

translator = Translator(to_lang = 'ja')
try:
    with open('./test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt', mode = 'w', encoding="utf-8") as write_file:
            write_file.write(translation)
except FileNotFoundError as e:
    print('Check your file path silly!')