import requests, json


def usdt_tin_all_min():
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'bnc-uuid': 'f38c5ef6-1629-40d3-8c0a-c37551f43387',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'cookie': 'cid=FPOzrxRj; BNC-Location=; __BNC_USER_DEVICE_ID__={"685cf930488f50c55b2ffc5da440d9c4":{"date":1661834999965,"value":"1661834999320i84c3vhZ9l9EqbezI2T"}}; bnc-uuid=f38c5ef6-1629-40d3-8c0a-c37551f43387; source=referral; campaign=www.binance.com; userPreferredCurrency=RUB_USD; fiat-prefer-currency=RUB; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2235311803%22%2C%22first_id%22%3A%22182edfcebe9177-0b05c255d330f4-26021d51-2073600-182edfcebeaff8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyZWRmY2ViZTkxNzctMGIwNWMyNTVkMzMwZjQtMjYwMjFkNTEtMjA3MzYwMC0xODJlZGZjZWJlYWZmOCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjM1MzExODAzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2235311803%22%7D%2C%22%24device_id%22%3A%22182edfcebe9177-0b05c255d330f4-26021d51-2073600-182edfcebeaff8%22%7D; BNC_FV_KEY=333cc5d3b3eca717b4e7cae75fe414d4d42e4d14; lang=ru; BNC_FV_KEY_EXPIRE=1662119416438; sys_mob=no; common_fiat=RUB; videoViewed=yes; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Sep+02+2022+12%3A16%3A08+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=ff82eeb7-cbf1-442f-9855-98cd8890838b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; showBlockMarket=false',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTQ0MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTM5MiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCs1IiwidGltZXpvbmVPZmZzZXQiOi0zMDAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA0LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImE5Y2ZjMTllIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEludGVsKSIsIndlYmdsX3JlbmRlcmVyIjoiQU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgNjMwIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiQXNpYS9ZZWthdGVyaW5idXJnIiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwNC4wLjAuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6ImIzMmJkYzA3MTNiZDI5OGFlYzZmYmFkN2Q0MWUwZWNkIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTY2MTgzNDk5OTMyMGk4NGMzdmhaOWw5RXFiZXpJMlQifQ==',
        'fvideo-id': '333cc5d3b3eca717b4e7cae75fe414d4d42e4d14',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/TinkoffNew/USDT?fiat=RUB',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-trace-id': '8d3028e6-8460-46b6-b175-56ec316eca88',
        'x-ui-request-trace': '8d3028e6-8460-46b6-b175-56ec316eca88',
    }
    data = '{"proMerchantAds":false,"page":1,"rows":10,"payTypes":["TinkoffNew"],"countries":[],"publisherType":null,"transAmount":"","asset":"USDT","fiat":"RUB","tradeType":"BUY"}'
    response = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, data=data)
    json_data = json.loads(response.text)
    res = float(json_data['data'][0]['adv']['price'])
    print(f"usdt_tin_all_min: {res}")
    return res


def usdt_tin1000_min():
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
        'bnc-uuid': 'f38c5ef6-1629-40d3-8c0a-c37551f43387',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        'cookie': 'cid=FPOzrxRj; BNC-Location=; __BNC_USER_DEVICE_ID__={"685cf930488f50c55b2ffc5da440d9c4":{"date":1661834999965,"value":"1661834999320i84c3vhZ9l9EqbezI2T"}}; bnc-uuid=f38c5ef6-1629-40d3-8c0a-c37551f43387; source=referral; campaign=www.binance.com; userPreferredCurrency=RUB_USD; fiat-prefer-currency=RUB; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2235311803%22%2C%22first_id%22%3A%22182edfcebe9177-0b05c255d330f4-26021d51-2073600-182edfcebeaff8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyZWRmY2ViZTkxNzctMGIwNWMyNTVkMzMwZjQtMjYwMjFkNTEtMjA3MzYwMC0xODJlZGZjZWJlYWZmOCIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjM1MzExODAzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2235311803%22%7D%2C%22%24device_id%22%3A%22182edfcebe9177-0b05c255d330f4-26021d51-2073600-182edfcebeaff8%22%7D; BNC_FV_KEY=333cc5d3b3eca717b4e7cae75fe414d4d42e4d14; lang=ru; BNC_FV_KEY_EXPIRE=1662119416438; sys_mob=no; common_fiat=RUB; videoViewed=yes; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Sep+02+2022+12%3A04%3A41+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=ff82eeb7-cbf1-442f-9855-98cd8890838b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; showBlockMarket=false',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTQ0MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjI1NjAsMTM5MiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUtUlUiLCJ0aW1lem9uZSI6IkdNVCs1IiwidGltZXpvbmVPZmZzZXQiOi0zMDAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA0LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImE5Y2ZjMTllIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEludGVsKSIsIndlYmdsX3JlbmRlcmVyIjoiQU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgNjMwIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiQXNpYS9ZZWthdGVyaW5idXJnIiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwNC4wLjAuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6ImIzMmJkYzA3MTNiZDI5OGFlYzZmYmFkN2Q0MWUwZWNkIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTY2MTgzNDk5OTMyMGk4NGMzdmhaOWw5RXFiZXpJMlQifQ==',
        'fvideo-id': '333cc5d3b3eca717b4e7cae75fe414d4d42e4d14',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/TinkoffNew/USDT?fiat=RUB',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-trace-id': 'ebd466ab-5c95-4be0-949d-8b50049cf093',
        'x-ui-request-trace': 'ebd466ab-5c95-4be0-949d-8b50049cf093',
    }
    data = '{"proMerchantAds":false,"page":1,"rows":10,"payTypes":["TinkoffNew"],"countries":[],"publisherType":null,"transAmount":"1000","asset":"USDT","fiat":"RUB","tradeType":"BUY"}'
    response = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, data=data)
    json_data = json.loads(response.text)
    res = float(json_data['data'][0]['adv']['price'])
    print(f"usdt_tin1000_min: {res}")
    return res
