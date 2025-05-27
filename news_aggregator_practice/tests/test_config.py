import importlib.util
from tools import gen_config


# Исправленный код в tests/test_config.py
def test_config_generated(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    student_id_file = tmp_path / "student_id.txt"
    student_id_file.write_text("TestStudent", encoding="utf-8")

    # Добавлена закрывающая скобка ')'
    gen_config.generate_config(
        output_dir=str(tmp_path),
        student_id_path=str(student_id_file)
    )# <-- исправлено