import urllib.request

sites = [
    'http://www.pudim.com.br',
    'https://www.google.com',
    'http://www.sitequenaoexiste123456.com.br',
    'https://www.github.com',
    'http://127.0.0.1:8080',]
for s in sites:
    try:
        t = urllib.request.urlopen(s)
    except urllib.error.URLError:
        print(f'\033[1;31m o site {s} esta  inacessivel\033[m')
    else:
        print(f'\033[1;32m o site {s} esta acessivel \033[m')




