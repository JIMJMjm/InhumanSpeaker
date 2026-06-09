import warnings

warnings.filterwarnings("ignore", message="pkg_resources is deprecated")

import jieba
import sys
import os
from random import sample, shuffle, randint

params = sys.argv[1:]
DB = ['最直接', '最真相', '最不绕弯', '最扎心', '最硬核', '最干脆', '最不墨迹', '最戳痛点', '最不留情面', '最一针见血',
      '最开门见山',
      '最单刀直入', '最不铺垫', '最不客套', '最不煽情', '最不废话', '最不拐弯', '最不磨叽', '最不装', '最不端着',
      '最不啰嗦', '最不拖沓',
      '最不委婉', '最不掩饰', '最不藏着掖着', '最直白', '最露骨', '最实在', '最通透', '最毒辣', '最爽快', '最解气',
      '最上头', '最够劲',
      '最过瘾', '最粗暴', '最有效', '最狠', '最准', '最稳', '最绝', '最顶', '最炸', '最刚', '最烈', '最飒', '最莽',
      '最冲', '最猛',
      '最脆', '最亮', '最透', '最干净', '最利落', '最霸道', '最硬核', '最生猛', '最狂野', '最直白', '最粗暴',
      '最不讲虚的',
      '最不玩套路', '最不搞形式', '最不整虚头巴脑', '最只讲干货', '最只说重点', '最只给结果', '最只聊真相',
      '最只谈核心', '最只戳关键']


def get_CCP_string(ori_string: str) -> str:
    head = '哦欸'
    body = '吼嗷嘿'
    tail = '?!'
    res = ''
    if randint(0, 6) == 0:
        res += sample(head, 1)[0]
    sbody, rbody = sample(body, 2)
    while randint(0, 70) > 21 + (len(res) >= 3)*12 + len(res)*6 - (len(res)<2)*8:
        res += sbody
        if randint(0, 7) == 0:
            res += rbody
            break
    if not res and randint(0, 2) != 0:
        res += head[0]
    if len(res) == 1 and randint(0, 3) == 0:
        res *= 2
    if randint(0, 6) == 0:
        res += sample(tail, 1)[0]

    return ori_string + res


def get_RTS_string(ori_string: str) -> str:
    words = list(jieba.cut(ori_string))
    return ''.join(
        list(f'“{i}......”' for i in words if not i in '，。：；“”‘’？！@#￥%……&*（）【】{}、|\\/《》!$^()[]"\':;<>,.?-——_'))


def get_DBL_string(ori_string: str, dbs: int) -> str:
    """

    :param ori_string:
    :param dbs: less than 71
    :return:
    """
    dbs = max(min(dbs, 71), 1)
    useddb = sample(DB, dbs)
    shuffle(useddb)
    return f'我会用{'、'.join(useddb)}的方式来告诉你：{ori_string}'


def set_mode(mode_) -> None:
    try:
        mode_ = int(mode_)
    except ValueError:
        print('Mode is an integer.')
        sys.exit()
    with open('rts.cfg', 'r+b') as f:
        f.seek(0)
        f.write(bytes([mode_+48]))
    if mode_ == 0:
        print('Switch to Input Mode.')
    if mode_ == 1:
        print('Switch to Executable Mode.')


def set_model(model_) -> None:
    try:
        model_ = int(model_)
    except ValueError:
        print('Model is an integer.')
        sys.exit()
    with open('rts.cfg', 'r+b') as f:
        f.seek(1)
        f.write(bytes([model_+48]))
    if model_ == 0:
        print('Switch to ReinetteTinekerrSpeaker.')
    if model_ == 1:
        print('Switch to DouBaoLikeSpeaker.')
    if model_ == 2:
        print('Switch to CCPSpeaker.')


if __name__ == '__main__':
    if not os.path.exists('rts.cfg'):
        with open('rts.cfg', 'wb') as f:
            f.write(bytes([49]))
            f.write(bytes([48]))

    jieba.setLogLevel(50)
    with open('rts.cfg', 'rb') as cfgfile:
        cfg = cfgfile.read(2)
    mode, model = cfg[0], cfg[1]

    while True:
        if not params:
            break
        oper = params.pop(0)
        res = ''
        if mode == 48:
            ori = input()
            if model == 48:
                ori = get_RTS_string(ori)
            if model == 49:
                ori = get_DBL_string(ori)
            print(ori)
            os.system('pause')
        if oper == '-mode':
            set_mode(params.pop(0))
            continue
        if oper == '-model':
            set_model(params.pop(0))
            continue
        if model == 48:
            res = get_RTS_string(oper)
        if model == 49:
            dbln = '--dbln=5'
            if params:
                dbln = params.pop(0)
            if dbln.startswith('--dbln='):
                try:
                    dbln = int(dbln[7:])
                except ValueError:
                    print('dbln is an integer.')
                    sys.exit()
            res = get_DBL_string(oper, dbln)
        if model == 50:
            res = get_CCP_string(oper)
        print(res)
        os.system('pause')
