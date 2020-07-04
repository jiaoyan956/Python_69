import requests #第三方库  模块名

def http_request(url,data,token=None,method='POST'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
                'Authorization': token}
    if method=='GET':
        result = requests.get(url,json=data,headers=header)
    elif method == 'PATCH':
        result = requests.patch(url, json=data, headers=header)
    else:
        result = requests.post(url, json=data, headers=header)

    return  result.json()#return返回指定的结果

if __name__ == '__main__':
    # #注册
    # reg_url = "http://120.78.128.25:8766/futureloan/member/register"
    # reg_data = {'mobile_phone': '17788889996','pwd': 'lemon123456', 'type': '0'}
    # reg_data = {'mobile_phone': '17788889995','pwd': 'lemon6666', 'type': '1'}
    # reg_response =http_request(reg_url, reg_data)
    # print(reg_response)

    # #登录
    log_url = "http://120.78.128.25:8766/futureloan/member/login"
    log_data = {'mobile_phone': '17788889996', 'pwd': 'lemon123456'}
    log_response = http_request(log_url, log_data)
    print(log_response)

    #充值
    token=log_response['data']['token_info']['token']
    rec_url = "http://120.78.128.25:8766/futureloan/member/recharge"
    rec_data = {'member_id': log_response['data']['id'], 'amount': '50000'}
    rec_response = http_request(rec_url, rec_data,'Bearer ' +token)
    print(rec_response)

    # 提现
    wit_url = "http://120.78.128.25:8766/futureloan/member/withdraw"
    wit_data = {'member_id': log_response['data']['id'], 'amount': '0.01'}
    wit_response = http_request(wit_url, wit_data, 'Bearer ' +token)
    print(wit_response)

    #更新昵称
    upd_url = "http://localhost:8080/futureloan/member/update"
    upd_data = {'member_id': log_response['data']['id'], 'reg_name':'智慧美貌于一身的檬檬'}
    upd_response = http_request(upd_url, upd_data,'Bearer ' +token)
    print(upd_response)

    # 加标
    add_url = "http://120.78.128.25:8766/futureloan/loan/add"
    add_data = {'member_id': log_response['data']['id'], 'title': '购买全栈测试课程_1', 'amount': 1000.00,
                'loan_rate': 1, 'loan_term': 1, 'loan_date_type': 1, 'bidding_days': 1}
    add_response = http_request(add_url, add_data,'Bearer ' +token)
    print(add_response)

    # #审核
    aud_url = "http://120.78.128.25:8766/futureloan/loan/audit"
    aud_data = {'loan_id': add_response['data']['id'], 'approved_or_not': 'true'}
    aud_response = http_request(aud_url,aud_data, 'Bearer ' +token)
    print(aud_response)

    # 投资
    inv_url = "http://120.78.128.25:8766/futureloan/member/invest"
    inv_data = {'member_id': log_response['data']['id'], 'loan_id': add_response['data']['id'], 'amount': '100'}
    inv_response = http_request(inv_url,inv_data, 'Bearer ' +token)
    print(inv_response)