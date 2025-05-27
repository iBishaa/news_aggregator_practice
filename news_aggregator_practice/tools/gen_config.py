import os
import uuid


def generate_config(output_dir=".", student_id_path=None): # Добавлен параметр student_id_path
    try:
        if student_id_path is None:
            # Если путь не указан, используем путь относительно корня проекта
            project_root = os.path.dirname(os.path.dirname(__file__))
            student_id_path = os.path.join(project_root, 'student_id.txt')

        with open(student_id_path, encoding='utf-8-sig') as f:
            student = f.read().strip()
            student_id = f"{student}_{uuid.uuid4().hex[:8]}"
            content = f'''STUDENT_ID = "{student_id}"
SOURCES    = []
'''
        config_path = os.path.join(output_dir, 'config.py')
        with open(config_path, 'w', encoding='utf-8') as cfg:
            cfg.write(content)
        print("Конфиг создан успешно!")
    except FileNotFoundError:
        print("Ошибка: файл student_id.txt не найден!")


# 2. Обновите тест:
def test_config_generated(tmp_path, monkeypatch, gen_config=None):
    monkeypatch.chdir(tmp_path)
    test_student_id = "TestStudent"
    student_id_file = tmp_path / "student_id.txt"
    student_id_file.write_text(test_student_id, encoding="utf-8")

    # Указываем путь к student_id.txt и output_dir
    gen_config.generate_config(
        output_dir=str(tmp_path),
        student_id_path=str(student_id_file))