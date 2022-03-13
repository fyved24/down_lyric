python 3.9.20

打包命令

```bash
nuitka --standalone --mingw64 --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --follow-import-to=mainwindow --follow-import-to=forms  --output-dir=o main.py
```

```bash
# 不弹出控制台
--windows-disable-console
--macos-disable-console
# mac 打包成应用
--macos-create-app-bundle
```

用以上命令打包后会缺少一些包，需要把req.zip（windwos）解压到打包目录
