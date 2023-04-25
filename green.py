# -*- coding: UTF-8 -*-

import base64

path = r''

def activate(path):
    path += base64.b64decode('XHJlc291cmNlc1xhcHBcc3JjXHhsanNjaVxpbmRleC5odG1s').decode('utf-8')
    bstr = "CjxzY3JpcHQ+IWZ1bmN0aW9uKCl7dmFyIGU9d2luZG93LlhNTEh0dHBSZXF1ZXN0O3dpbmRvdy5YTUxIdHRwUmVxdWVzdD1mdW5jdGlvbigpe3ZhciB0PW5ldyBlO3JldHVybiB0LmFkZEV2ZW50TGlzdGVuZXIoImxvYWQiLCgpPT57aWYoLTEhPT10LnJlc3BvbnNlVVJMLmluZGV4T2YoImhhc1VubG9jayIpKXt2YXIgZT17Y29kZTowLG1zZzoi5pON5L2c5oiQ5YqfIixkYXRhOiEwfTtPYmplY3QuZGVmaW5lUHJvcGVydHkodCwicmVzcG9uc2VUZXh0Iix7d3JpdGFibGU6ITB9KSxPYmplY3QuZGVmaW5lUHJvcGVydHkodCwicmVzcG9uc2UiLHt3cml0YWJsZTohMH0pLHQucmVzcG9uc2U9SlNPTi5zdHJpbmdpZnkoZSksdC5yZXNwb25zZVRleHQ9SlNPTi5zdHJpbmdpZnkoZSl9fSwhMSksdH19KCk7PC9zY3JpcHQ+Cg=="
    print(f'Index Path: {path}')
    with open(path, 'ab') as file:
        file.write(base64.b64decode(bstr))
        print("Success.")

if __name__=='__main__':
    if path=='':
        path=input("Please input the installation directory:")
    else:
        activate(path)