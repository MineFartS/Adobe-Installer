from philh_myftp_biz.web import download
from philh_myftp_biz.pc import Path, script_dir
from philh_myftp_biz.gui import GUI
from philh_myftp_biz.file import YAML

#=============================================

config = script_dir(__file__).child('config.yaml')

config = YAML(config).read()

print(f'{config=}')

#=============================================
# GUI

gui = GUI()

gui.title = 'Windows Installer'

gui.Header(config['title'])

gui.Button()

gui.run()