#!/usr/bin/env python3
import platform, gspread
from datetime import datetime, timezone, timedelta

from binance_coin import usdt_tin_all_min, usdt_tin1000_min
from binance_api import usdtrub, btcrub



def now_time_msk():
    msk = ""
    if platform.system() == "Windows":
        msk = datetime.now(timezone(timedelta(hours=3))).strftime('%#H:%M:%S')
    elif platform.system() == "Linux":
        msk = datetime.now(timezone(timedelta(hours=3))).strftime('%-H:%M:%S')
    return f"Обновлено в: {msk} по МСК."


def get_sum_on_the_card():
    gc = gspread.service_account(filename='./sacc.json')
    sh = gc.open("Crypto")
    worksheet = sh.sheet1
    resp = worksheet.acell('D5').value
    return int(resp)


def set_color(value):
    res = None
    if value <= 0:
        return {"backgroundColor": {"red": 1, "green": 1, "blue": 1}}
    elif 0 < value < 100:
        return {"backgroundColor": {"red": .9, "green": 1, "blue": .9}}
    elif 100 <= value < 200:
        return {"backgroundColor": {"red": .8, "green": 1, "blue": .8}}
    elif 200 <= value < 300:
        return {"backgroundColor": {"red": .7, "green": 1, "blue": .7}}
    elif 300 <= value < 400:
        return {"backgroundColor": {"red": .6, "green": 1, "blue": .6}}
    elif 400 <= value < 500:
        return {"backgroundColor": {"red": .5, "green": 1, "blue": .5}}
    elif 500 <= value < 600:
        return {"backgroundColor": {"red": .4, "green": 1, "blue": .4}}
    elif 600 <= value < 700:
        return {"backgroundColor": {"red": .3, "green": 1, "blue": .3}}
    elif 700 <= value < 800:
        return {"backgroundColor": {"red": .2, "green": 1, "blue": .2}}
    elif value >= 800:
        return {"backgroundColor": {"red": .1, "green": 1, "blue": .1}}


def save_update_sheets():
    gc = gspread.service_account(filename='./sacc.json')
    sh = gc.open("Crypto")
    worksheet = sh.sheet1
    worksheet2 = sh.worksheet("Лист2")
    worksheet.update('B5', usdtrub)
    worksheet.update('B6', btcrub)
    worksheet2.update('I3', usdt_tin_all_min())
    worksheet2.update('I4', usdt_tin1000_min())
    val = float(worksheet.acell('B13').value.replace(",", ".").strip())
    worksheet.format("B13", set_color(val))
    worksheet.update('A2', now_time_msk())


print(f"Start: {now_time_msk()}")
start = datetime.now()
save_update_sheets()
print(f"[ + ] {datetime.now() - start}")
print()
