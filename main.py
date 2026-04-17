import jieba
import sys
import os

params = sys.argv[1:]


def get_string(ori_string: str) -> str:
    words = list(jieba.cut(ori_string))
    return ''.join(list(f'“{i}......”' for i in words))


if __name__ == '__main__':
    jieba.setLogLevel(20)
    with open('rts.cfg', 'rb') as f:
        mode = f.read(1)
    if mode == b'0':
        result = get_string(input())
        print(result)
        os.system('pause')
    if not params or mode != b'1':
        sys.exit()
    if params[0] == '-mode' and params[1]:
        with open('rts.cfg', 'wb') as f:
            mode = f.write(bytes(int(params[1])))
        sys.exit()
    ori_str = get_string(params[0].strip())
    print(ori_str)
    os.system('pause')
