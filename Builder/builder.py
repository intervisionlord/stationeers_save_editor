import zipfile
from yaml import full_load as loadyaml
from os import system as runCommand

def getconfig() -> dict:
    """Загружает данные из конфига сборки.

    Returns:
        dict: Список переменных конфига
    """
    try:
        with open('./config.yaml', 'r') as confFile:
            conf: dict = loadyaml(confFile)
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

def makeParamStr(getconfig) -> str:
    """Создает строку параметров сборки из данных конфига.

    Args:
        getconfig (function): Принимает на вход функцию парсинга конфига

    Returns:
        str: Строка с набором параметров сборки
    """
    paramList = []
    for param in getconfig['params']:
        if param == 'windows-product-version':
            param = '{}="{}"'.format(param, getconfig['main']['version'])
        paramList.append(param)
    paramStr = '--' + ' --'.join(paramList)
    return paramStr    

if __name__ == '__main__':
    """Запуск сборки бинарного файла и его упаковка в архив.
    """
    paramsStr = makeParamStr(getconfig())
    plugins = getconfig()['plugins']
    icon = getconfig()['main']['icon']
    runCommand(f'nuitka {paramsStr} --plugin-enable={plugins} --windows-icon-from-ico={icon} --include-data-files=../config.yaml=./ --include-data-files=../imgs/*.ico=imgs/ ../SSE.py')
    zipOutput()