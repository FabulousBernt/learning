from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('./testfolder/test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./testfolder/test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print("File not found, check file path.")
