import requests
import os
from forms.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

netease_url = "https://netease-cloud-music-api-iota-drab.vercel.app"
qqmusic_url = 'https://qq-music-api-beta.vercel.app'


def get_netease_music_id_name_list(search_name, maxnum):
    resp = requests.get(url=f'{netease_url}/search', params={"keywords": search_name})
    print(resp.json())
    songs_list = []
    for i, song in enumerate(resp.json()['result']['songs']):
        if i < maxnum:
            print(song)
            print(song['name'])
            songs_list.append({'id': song['id'], 'name': f"{song['name']}_{i}_{song['artists'][0]['name']}"})
    return songs_list


def get_qq_music_id_name_list(search_name, maxnum):
    resp = requests.get(url=f'{qqmusic_url}/getSmartbox', params={"key": search_name})
    print(resp.json())
    songs_list = []
    for i, song in enumerate(resp.json()['response']['data']['song']['itemlist']):
        if i < maxnum:
            print(song)
            print(song['name'])
            songs_list.append({'id': song['mid'], 'name': f"{song['name']}_{i}_{song['singer']}"})
    return songs_list


def get_netease_lrc(mid):
    # print(music_info['img1v1Url'])
    resp = requests.get(url=f'{netease_url}/lyric', params={"id": mid})
    print(resp)
    print(resp.json()['lrc']['lyric'])
    return resp.json()['lrc']['lyric']


def get_qqmusic_lrc(mid):
    # print(music_info['img1v1Url'])
    resp = requests.get(url=f'{qqmusic_url}/getLyric', params={"songmid": mid})
    print(resp)
    print(resp.json()['response']['lyric'])
    return resp.json()['response']['lyric']


def save_file(path, name, content):
    name = name.replace('/', '_')
    lrcs_dir = f"{path}/lrcs"
    print(lrcs_dir)
    if not os.path.exists(lrcs_dir):
        os.makedirs(lrcs_dir)

    with open(f"{lrcs_dir}/{name}.lrc", "w", encoding="utf-8") as f:
        f.write(content)


def load_music_list(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw_list = f.readlines()
        music_list = [x.strip() for x in raw_list]
        return music_list


def download_lrc(path, name, maxnum):
    music_id_name_list = get_music_id_name(name, maxnum)
    for music in music_id_name_list:
        content = get_lrc(music['id'])
        save_file(path, music['name'], content)


get_music_id_name = get_qq_music_id_name_list
get_lrc = get_qqmusic_lrc


class MainWindow(QMainWindow):

    def __init__(self):
        # 从文件中加载UI定义
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_file_button.clicked.connect(self.open_file)
        self.ui.choose_output_dir_button.clicked.connect(self.select_output_path)

        self.ui.start_button.clicked.connect(self.download_slot)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, os.getcwd())
        print(filename)
        self.ui.filepath.setText(filename)

    def select_output_path(self):
        filename = QFileDialog.getExistingDirectory(self, os.getcwd())
        print(filename)
        self.ui.output_filepath.setText(filename)

    def download_lrc_list(self, listname):
        global get_music_id_name
        global get_lrc
        down_source = self.ui.down_source.currentIndex()
        option_nums = self.ui.options_num.currentIndex() + 1
        if down_source == 0:
            get_music_id_name = get_netease_music_id_name_list
            get_lrc = get_netease_lrc
        else:
            get_music_id_name = get_qq_music_id_name_list
            get_lrc = get_qqmusic_lrc

        print(down_source, option_nums)
        music_list = load_music_list(listname)
        self.ui.progressBar.setMaximum(len(music_list))

        for i, music in enumerate(music_list):
            download_lrc(self.ui.output_filepath.text(), music, option_nums)
            self.ui.progressBar.setValue(i + 1)

    def download_slot(self):
        if self.ui.filepath.text() == '':
            QMessageBox.critical(self, '错误', '歌曲文件路径不能为空')
        else:
            self.download_lrc_list(self.ui.filepath.text())
            QMessageBox.information(self, '提示', '歌词下载完成')


if __name__ == '__main__':
    download_lrc('D:\PycharmProjects\down_lyric', "星座书上", 3)
