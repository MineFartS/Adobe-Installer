from philh_myftp_biz.web import download
from philh_myftp_biz.pc import Path, script_dir
from philh_myftp_biz.gui import GUI
from philh_myftp_biz.file import YAML

from functools import partial

def install(url:str):
    
    gui.clear()

    gui.Button(
        text = 'Back'
    )

#=============================================
# GUI

gui = GUI()

gui.title = 'Cracked Adobe Installer'

class Page:

    home = gui.Page()
    photoshop = gui.Page()
    premiere_pro = gui.Page()

#=============================================
# PAGE: HOME

Page.home.Header('Adobe Installer')

Page.home.Button(
    text = 'Photoshop',
    page = Page.photoshop
)

Page.home.Button(
    text = 'Premiere Pro',
    page = Page.premiere_pro
)

#=============================================
# PAGE: PHOTOSHOP

Page.photoshop.Header('Photoshop')

Page.photoshop.Button(
    text = 'back',
    page = Page.home
)

Page.photoshop.Button(
    text = 'Install',
    func = partial(install, 'https://philh.myftp.biz/Media/Programs/Adobe/Photoshop.zip')
)

#=============================================
# PAGE: PREMIERE PRO

Page.premiere_pro.Header('Premiere Pro')

Page.premiere_pro.Button(
    text = 'back',
    page = Page.home
)

Page.premiere_pro.Button(
    text = 'Install',
    func = partial(install, 'https://philh.myftp.biz/Media/Programs/Adobe/Premiere Pro.zip')
)

#=============================================

gui.page = Page.home

gui.run()