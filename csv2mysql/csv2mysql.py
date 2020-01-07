import csv
import os
import utils.mysql_helper as msh
import datetime


def run(env, dbname, table_name):
    data_dir = r'../data\hy_round1_train_20200102'
    files = os.listdir(data_dir)
    insert_sql = """
    insert into {}(id,x,y,speed,direction,time,type) 
    value(%s,%s,%s,%s,%s,%s,%s)
    """.format(table_name)

    for fname in files:
        sFileName = '{}\{}'.format(data_dir, fname)
        row_list = []
        with open(sFileName, newline='', encoding='UTF-8') as csvfile:
            rows = csv.reader(csvfile)
            line_num = 0
            for row in rows:
                line_num += 1
                if (line_num != 1):
                    row[-2] = datetime.datetime.strptime(row[-2], '%m%d %H:%M:%S')
                    row_list.append(row)
        msh.save_datas(env, dbname, insert_sql, row_list)
        print('{}转储成功'.format(fname))


if __name__ == '__main__':
    env = 'local'
    dbname = 'tianchi'
    table_name = 'train'
    run(env, dbname, table_name)
