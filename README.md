1.将完整csv数据分别放到tianchi_fish_2020_mse\data\hy_round1_train_20200102
和tianchi_fish_2020_mse\data\hy_round1_testA_20200102中
2.setting.py 配置数据库连接如：
'local': {'host': '127.0.0.1', 'user': 'root', 'passwd': 'Root.8888', 'port': 3306}
3.create_table.sql 创建trian表
4.运行csv2mysql.py# tianchi_fish_2020_mse
