import requests
import os
from forms.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtNetwork import QTcpSocket

# from dialog import Dialog


base_url = "https://netease-cloud-music-api-iota-drab.vercel.app"

search_name = "海阔天空"


def get_music_id_name(search_name):
    resp = requests.get(url=f'{base_url}/search', params={"keywords": search_name})
    print(resp.json())
    music_info = resp.json()['result']['songs'][0]
    print(music_info)
    print(music_info['name'])
    return music_info['id'], music_info['name']


def get_lrc(id):
    # print(music_info['img1v1Url'])
    resp = requests.get(url=f'{base_url}/lyric', params={"id": id})
    print(resp)
    print(resp.json()['lrc']['lyric'])
    return resp.json()['lrc']['lyric']


def save_file(name, content):
    current_dir = os.getcwd()
    lrcs_dir = f"{current_dir}/lrcs"
    if not os.path.exists(lrcs_dir):
        os.makedirs(lrcs_dir)

    with open(f"lrcs/{name}.lrc", "w", encoding="utf-8") as f:
        f.write(content)


def load_music_list(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw_list = f.readlines()
        music_list = [x.strip() for x in raw_list]
        return music_list


def download_lrc(name):
    music_id, music_name = get_music_id_name(name)
    content = get_lrc(music_id)
    save_file(music_name, content)


def download_lrc_list(listname):
    music_list = load_music_list(listname)
    for music in music_list:
        download_lrc(music)


class MainWindow(QMainWindow):

    def __init__(self):
        # 从文件中加载UI定义
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.choose_file_button.clicked.connect(self.open_file)
        self.ui.start_button.clicked.connect(self.download_slot)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, os.getcwd())
        print(filename)
        self.ui.filepath.setText(filename)

    def download_slot(self):
        if self.ui.filepath.text() == '':
            QMessageBox.critical(self, '错误', '歌曲文件路径不能为空')
        else:
            download_lrc_list(self.ui.filepath.text())
            QMessageBox.information(self, '提示', '歌词下载完成')

# main()
