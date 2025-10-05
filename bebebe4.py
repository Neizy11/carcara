import base64
import os

def encode_python_script(file_path):
    """
    Зчитує вміст файлу Python, кодує його в Base64
    і створює новий, виконуваний файл, який містить
    розшифрований код.
    """
    if not os.path.exists(file_path):
        print(f"Помилка: Файл за шляхом '{file_path}' не знайдено.")
        return

    try:
        with open(file_path, 'rb') as f:
            code_bytes = f.read()
        
        # Кодування коду в Base64
        encoded_bytes = base64.b64encode(code_bytes)
        encoded_string = encoded_bytes.decode('utf-8')

        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        new_file_path = os.path.join(dir_name, f"encoded_{base_name}")

        # Створення нового файлу з кодом-завантажувачем
        obfuscated_code = (
            "import base64\n"
            "import os\n"
            "import subprocess\n"
            "import sys\n"
            "try:\n"
            f"    exec(base64.b64decode('{encoded_string}'))\n"
            "except Exception as e:\n"
            "    print(f'An error occurred: {e}')"
        )
        
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        
        print(f"✅ Файл успішно закодовано. Збережено як: {new_file_path}")

    except Exception as e:
        print(f"❌ Сталася помилка: {e}")

if __name__ == "__main__":
    input_path = input("Введіть повний шлях до файлу Python для кодування: ")
    encode_python_script(input_path)



