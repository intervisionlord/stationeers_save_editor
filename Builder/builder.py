import zipfile
import yaml
import os

def getconfig() -> dict:
    """Загружает данные из конфига сборки.

    Returns:
        dict: Список переменных конфига
    """
    try:
        with open('./config.yaml', 'r') as confFile:
            conf = yaml.full_load(confFile)
    except FileNotFoundError:
        print('File not found')
    return conf

def zipOutput():
    """Упаковывает готовый файл в архив.
    """
    with zipfile.ZipFile('SSE.zip', 'w',
                         compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as zipArch:
        zipArch.write('SSE.exe')

conf = getconfig()
paramsStr = '--' + ' --'.join(conf['params'])
plugins = conf['plugins']
icon = conf['main']['icon']

if __name__ == '__main__':
    """Запуск сборки бинарного файла и его упаковка в архив.
    """
    os.system(f'nuitka {paramsStr} --plugin-enable={plugins} --windows-icon-from-ico={icon} ../SSE.py')
    zipOutput()