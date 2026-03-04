from philh_myftp_biz.web import download
from philh_myftp_biz.file import temp, ZIP
from philh_myftp_biz.pc import Path, script_dir
from philh_myftp_biz.gui import GUI

from functools import partial

def install(name: str):

    gui.page = Page.install

    Page.install[0]['text'] = name

    dest = Path(f'C:/Program Files/AdobeCrack/{name}')

    tempfile = temp('adobe_download', 'zip')

    download(
        url = f'https://philh.myftp.biz/Media/Programs/Adobe/{name}.zip',
        path = tempfile
    )

    zip = ZIP(tempfile)

    zip.extractAll(dest)

#=============================================
# GUI

gui = GUI()

gui.title = 'Cracked Adobe Installer'

class Page:

    home = gui.Page()
    photoshop = gui.Page()
    premiere_pro = gui.Page()
    install = gui.Page()

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
    text = 'Back',
    page = Page.home
)

Page.photoshop.Button(
    text = 'Install',
    func = partial(install, 'Photoshop')
)

#=============================================
# PAGE: PREMIERE PRO

Page.premiere_pro.Header('Premiere Pro')

Page.premiere_pro.Button(
    text = 'Back',
    page = Page.home
)

Page.premiere_pro.Button(
    text = 'Install',
    func = partial(install, 'Premiere Pro')
)

#=============================================
# PAGE: INSTALL

Page.install.Header()

Page.install.Text('Installing')

Page.install.Text('This may take a while')

#=============================================

gui.page = Page.home

gui.run()