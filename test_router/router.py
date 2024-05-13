import sys
import re
import importlib
import pathlib as pl
from django.urls import path


route_dir = pl.Path(__file__).parent
sys.path.append(str(route_dir.resolve()))
print(route_dir)

func_pat = re.compile(r'def (\w+)')

url_fmt = lambda x: x[1:] if x[0] == '/' else x

def get_route(text: str):
    ok = False
    url = ''
    text_list = text.split(' ')
    for i in text_list:
        if not i:
            continue

        if i == '#@router':
            ok = True
            continue

        if ok:
            url = i
            break
    return ok, url


def parse(f):
    url_map = []
    for i in f:
        i = i.strip()
        if not i.startswith('#@router'):
            continue

        ok, url = get_route(i)
        if ok:
            next_line = next(f)
            func_name = func_pat.search(next_line)
            if func_name:
                # print(func_name.group(1))
                url_map.append([url_fmt(url), func_name.group(1)])

    # print(url_map)
    return url_map

def route_map(urlpatterns):
    maps = []
    for i in route_dir.glob('*/views.py'):
        print(i)
        with i.open('r') as f:
            url_map = parse(f)
            for url, func in url_map:
                maps.append([url, f'{i.parent.name}.views', func])

    for url, package, func in maps:
        urlpatterns.append(path(url, importlib.import_module(package).__dict__[func]))
    # print(maps)
    return maps


if __name__ == '__main__':
    a = []
    route_map(a)
