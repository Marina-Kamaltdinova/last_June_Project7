import zipfile
import pytest
import os
from script_os import FOLDER_DIR, FILES_DIR, ZIP_DIR
import shutil


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(FOLDER_DIR):  # проверяем существует ли папка
        os.mkdir(FOLDER_DIR)  # создаем папку если её нет
    with zipfile.ZipFile(ZIP_DIR, 'w') as zf:  # создаем архив
        for file in os.listdir(FILES_DIR):  # добавляем файлы в архив
            zf.write(os.path.join(FILES_DIR, file), file)  # добавляем файл в архив

    yield
    shutil.rmtree(FOLDER_DIR)


