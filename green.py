# -*- coding: UTF-8 -*-
# Author: willv

from base64 import b64decode
from sys import argv, platform, executable
from ctypes import windll
from os import system
from winreg import OpenKey, QueryValueEx, CloseKey, HKEY_LOCAL_MACHINE

path = r''


def defultpath():
    if platform == 'win32':
        key = OpenKey(HKEY_LOCAL_MACHINE, b64decode(
            'U09GVFdBUkVcV09XNjQzMk5vZGVceGxqc2Np').decode('utf-8'))
        value = QueryValueEx(key, 'InstPath')[0]
        CloseKey(key)
        return value
    elif platform == 'darwin':
        return b64decode('L0FwcGxpY2F0aW9ucy/lsI/nu7/psrjoi7HmlofmlofnjK7pmIXor7vlmaguYXBwL0NvbnRlbnRz').decode('utf-8')

def run_as_admin(param=''):
    if platform.startswith('win'):
        try:
            windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)
        except Exception as e:
            return False
        else:
            return True
    return False

def activate(path):
    if path.strip() == '':
        print("\033[1;31m[×] No path input.\033[0m")
        print("[+] Try to find the installation directory...")
        path = defultpath()
        print(f"\033[1;32m[√] Find the installation directory:\033[0m {path}")
    print("[+] Start activating...")
    path += b64decode('L3Jlc291cmNlcy9hcHAvc3JjL3hsanNjaS9pbmRleC5odG1s').decode('utf-8')
    bstr = "CjwhLS0gd2lsbHYgLS0+PHNjcmlwdD4hZnVuY3Rpb24oKXsidXNlIHN0cmljdCI7dmFyIGU9d2luZG93LlhNTEh0dHBSZXF1ZXN0O3dpbmRvdy5YTUxIdHRwUmVxdWVzdD1mdW5jdGlvbigpe3ZhciB0PW5ldyBlO3JldHVybiB0LmFkZEV2ZW50TGlzdGVuZXIoImxvYWQiLCgpPT57aWYoLTEhPT10LnJlc3BvbnNlVVJMLmluZGV4T2YoImhhc1VubG9jayIpKXt2YXIgZT17Y29kZTowLG1zZzoi5pON5L2c5oiQ5YqfIixkYXRhOiEwfTtPYmplY3QuZGVmaW5lUHJvcGVydHkodCwicmVzcG9uc2VUZXh0Iix7d3JpdGFibGU6ITB9KSxPYmplY3QuZGVmaW5lUHJvcGVydHkodCwicmVzcG9uc2UiLHt3cml0YWJsZTohMH0pLHQucmVzcG9uc2U9SlNPTi5zdHJpbmdpZnkoZSksdC5yZXNwb25zZVRleHQ9SlNPTi5zdHJpbmdpZnkoZSl9fSwhMSksdH07dmFyIHQ9ITE7c2V0VGltZW91dChmdW5jdGlvbihlLG4pe2xldCByPWRvY3VtZW50LmdldEVsZW1lbnRzQnlDbGFzc05hbWUoInhsanNjaS1oZWFkZXJfX2xvZ28tLWltZyIpOyh0fHwwIT1yLmxlbmd0aCkmJihyWzBdLnBhcmVudEVsZW1lbnQuaW5uZXJIVE1MPXJbMF0ucGFyZW50RWxlbWVudC5pbm5lckhUTUwrPSI8YSBocmVmPVwiamF2YXNjcmlwdDphbGVydCgnQ3JhY2tlZCBieSBXSUxMX1YnKVwiPndpbGx2IGNyYWNrZWQ8L2E+Iix0PSEwKX0sMWUzKX0oKTs8L3NjcmlwdD4K"
    print(f'[-] Index Path: \033[1;34m{path}\033[0m')
    with open(path, 'r', encoding='utf-8') as file:
        rl = file.readlines()
        for l in rl:
            if '<!-- willv -->' in l:
                print("\033[1;31m[×] Already activated.\033[0m")
                return
    if platform == 'win32' and path.startswith('C:'):
        print("\033[1;33m[+] WARNING: You may need administrator privileges to run this file.\033[0m")
        if not windll.shell32.IsUserAnAdmin():
            print("[-] Try to get administrator privileges...")
            run_as_admin(param=path)
        else:
            print("[-] Already have administrator privileges.")
    try:
        with open(path, 'ab') as file:
            file.write(b64decode(bstr))
            print("\033[1;32m[√] Success.\033[0m")
    except Exception as e:
        print("\033[1;31m[×] Failed.\033[0m")
        print(e)


if __name__ == '__main__':
    print("\nCracked by willv.")
    if platform == 'win32':
        print("NOTICE: If the installation directory is in the C drive, you may need administrator privileges to run this file.\n")
    elif platform == 'darwin':
        print("NOTICE: If you run this file in the terminal, you may need some privileges to run this file.\n")
    if len(argv) <= 1:
        if not path:
            path = input("Please input the installation directory:")
            print("")
        activate(path)
    else:
        activate(argv[1])
    print("\n按任意键退出...")
    system('pause >nul')