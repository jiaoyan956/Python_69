from lemon_69.R_W_EXCEL import reg_data #在lemon_69.R_W_EXCEL文件里面导入reg_data函数
from lemon_69.Demo_8 import http_request
from lemon_69.R_W_EXCEL import write_data
#执行文件
#获取所有的测试数据
Token=None#全局变量，初始值设置为None

def run(file_name,sheet_name,column_1,column_2):
    global Token#在这里声明 函数外的Token和函数内的Token是同一个值
    new_a=reg_data(file_name,sheet_name)
    # print(new_a)
    #执行测试
    #第一条测试用例登录
    # log_new_data=new_a[0]
    # ip="http://120.78.128.25:8766"
    # log_response=http_request(ip+log_new_data[3],eval(log_new_data[4]),token=None,method=log_new_data[2])
    # print('结果为：{}'.format(log_response))
    #充值
    for i in range(len(new_a)):#在http_request进行请求时，判断是否是登录请求
        rec_new_data = new_a[i]
        ip="http://120.78.128.25:8766"
        rec_response = http_request(ip + rec_new_data[4], eval(rec_new_data[5]), token=Token,
                                    method=rec_new_data[3])
        if 'login' in rec_new_data[4]:
            #它就是一个登录用例
            Token ="Bearer "+rec_response['data']['token_info']['token']
        print('结果为：{}'.format(rec_response))

    #登录
    # new_data=new_a[0]
    # method=new_data[2]
    # uri=new_data[3]
    # param=eval(new_data[4])
    # excepted = eval(new_data[5])
    # ip="http://120.78.128.25:8766"
    # url=ip+uri
    # response=http_request(url,param)
    # print(response)
        #开始写入结果
        write_data(file_name,sheet_name,rec_new_data[0]+1, column_1, str(rec_response))
        #进行判断，期望值与实际值是否相等，判断这个用例是否执行通过
        actual={'code':rec_response['code'],'msg':rec_response['msg']}
        if eval(rec_new_data[6])==actual:
            print('测试用例执行通过')
            write_data(file_name,sheet_name, rec_new_data[0] + 1, column_2, 'PASS')
        else:
            print('测试用例执行不通过')
            write_data(file_name,sheet_name, rec_new_data[0] + 1, column_2, 'FAIL')

#执行的充值接口
run('python_69.xlsx','recharge',8,9)
#执行的提现接口
run('python_69.xlsx','withdraw',8,9)
#执行的更新昵称接口
run('python_69.xlsx','name_update',8,9)
#执行的加标接口
run('python_69.xlsx','loan_add',8,9)
#执行的审核接口
run('python_69.xlsx','loan_audit',8,9)
#执行的投资接口
run('python_69.xlsx','invest',8,9)
