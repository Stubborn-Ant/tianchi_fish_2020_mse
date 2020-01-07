import pandas as pd
import pymysql
import numpy as np

from warnings import filterwarnings
import pymysql as Database
from config import setting as setting

filterwarnings('ignore', category=Database.Warning)


def get_conn(conn_name, db_name):
    conn = pymysql.Connect(
        host=setting.DB_ENV[conn_name]['host'],
        port=setting.DB_ENV[conn_name]['port'],
        user=setting.DB_ENV[conn_name]['user'],
        passwd=setting.DB_ENV[conn_name]['passwd'],
        charset=setting.DB_ENV['charset'],
        db=db_name
    )
    return conn


def get_data(conn_name, db_name, sql):
    conn = get_conn(conn_name, db_name)
    data = pd.read_sql(sql, conn)
    arr = np.array(data)
    conn.close()
    return arr

def get_data_with_session_var(conn_name, db_name, sql,session_sql):
    conn = get_conn(conn_name, db_name)
    cur = conn.cursor()
    cur.execute(session_sql)

    data = pd.read_sql(sql, conn)
    arr = np.array(data)
    conn.close()
    return arr


def save_datas(conn_name, db_name, sql, data_list):
    conn = get_conn(conn_name, db_name)
    cur = conn.cursor()
    # cur.execute('truncate '.format(db_tname))
    # 批量插入数据
    cur.executemany(sql, data_list)
    conn.commit()
    conn.close()


def execute_sql(conn_name, db_name, sql):
    conn = get_conn(conn_name, db_name)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()


def execute_sql_list(conn_name, db_name, sql_list):
    conn = get_conn(conn_name, db_name)
    cur = conn.cursor()
    for sql in sql_list:
        cur.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # 测试防火墙
    print(get_data('report_rcmd_prd', 'rcmd', 'select * from ods_dr2_article_biz limit 1'))
    print(get_data('prd', 'edw', 'select * from ods_dr2_article limit 1'))
