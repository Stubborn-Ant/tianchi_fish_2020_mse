# 项目简介
    天池2020智慧海洋-19MSE钓鱼小分队
## 1 依赖的模块
    pip install numpy scipy pandas scikit-learn pymysql simplejson 
## 2 csv转储到数据库步骤
    1.将完整csv数据分别放到tianchi_fish_2020_mse\data\hy_round1_train_20200102和tianchi_fish_2020_mse\data\hy_round1_testA_20200102中
    2.在setting.py中配置数据库连接如：'local': {'host': '127.0.0.1', 'user': 'root', 'passwd': 'Root.8888', 'port': 3306}
    3.create_table.sql 创建trian表
    4.运行csv2mysql.py# tianchi_fish_2020_mse
uname:zhangsan passwd:***
