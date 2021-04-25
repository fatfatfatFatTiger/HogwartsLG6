
import os
import configparser


class DB:
    def get_config(self):
        cur_file_path = os.path.realpath(__file__)  # 获取当前脚本的真实路径（右斜杠）
        cur_dir_path = os.path.dirname(cur_file_path)

        cfg_dir_path = os.path.join(cur_dir_path, 'config')
        cfg_file_path = os.path.join(cfg_dir_path, 'config.ini')

        conf = configparser.ConfigParser()
        conf.read(cfg_file_path)
        return conf

    def connect_db(self):
        config = self.get_config()
        username = config.get('db_info', 'username')
        password = config.get('db_info', 'password')
        host = config.get('db_info', 'host')
        dbname = config.get('db_info', 'dbname')
        options = config.get('db_info', 'options')
        uri = f'mysql+pymysql://{username}:{password}@{host}/{dbname}?{options}'
        return uri


if __name__ == '__main__':
    # d = DB()
    # x = d.get_config()
    #
    # print(x.get('db_info', 'username'))

    uri = DB().connect_db()
    print(uri)



