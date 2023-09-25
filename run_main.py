import os
import pytest
import datetime


def run_all():
    # -s����ʾ�����е����
    # -v���������ϸ������ִ����Ϣ
    # __file__�����ļ�
    # ����YYYY-mm-dd-HHMMSS��ʱ���
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d-%H%M%S")
    # pytest.main(['--alluredir','./report'])
    # �˴����� --alluredir �����˱����ԭʼ�ļ�
    pytest.main(["-vs", "--alluredir", "./Report/{}xml".format(time_str)])
    # �˴����� allure generate ��ǰ�����ɵ�json�ļ�ת��Ϊhtml�ı���
    os.system("allure generate ./Report/{}xml -o ./Report/{}html --clean".format(time_str, time_str))
    # ���ɵı���index.html����ֱ����Chrome�򿪣��򿪺󿴲������ݣ���Ҫ��allure open�򿪲�����Ⱦ����ʽ����ʾ����
    os.system("allure open ./Report/{}html".format(time_str))




if __name__ == '__main__':
    run_all()

