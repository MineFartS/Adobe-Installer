from philh_myftp_biz.gui import GUI, Widget
from philh_myftp_biz.file import temp, ZIP
from philh_myftp_biz.web import download
from philh_myftp_biz.pc import Path

#=============================================

def install(name: str):

    Page.install[0]['text'] = name

    dest = Path(f'C:/Program Files/AdobeCrack/{name}')

    Page.install[1]['text'] += dest.path

    gui.page = Page.install
    
    return
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

gui.title = 'Adobe Installer'

class Page:

    home = gui.Page()
    photoshop = gui.Page()
    premiere_pro = gui.Page()
    install = gui.Page()

#=============================================
# PAGE: HOME

Page.home += Widget.Header('Adobe Installer')

Page.home += Widget.Button(
    text = 'Photoshop',
    onclick = Page.photoshop
)

Page.home += Widget.Button(
    text = 'Premiere Pro',
    onclick = Page.premiere_pro
)

#=============================================
# PAGE: PHOTOSHOP

Page.photoshop += Widget.Header('Photoshop')

Page.photoshop += Widget.Button(
    text = 'Back',
    onclick = Page.home
)

Page.photoshop += Widget.Button(
    text = 'Install',
    onclick = lambda: install('Photoshop')
)

#=============================================
# PAGE: PREMIERE PRO

Page.premiere_pro += Widget.Header('Premiere Pro')

Page.premiere_pro += Widget.Button(
    text = 'Back',
    onclick = Page.home
)

Page.premiere_pro += Widget.Button(
    text = 'Install',
    onclick = lambda: install('Premiere Pro')
)

#=============================================
# PAGE: INSTALL

Page.install += Widget.Header()

Page.install += Widget.Text('Installation Path: ')

Page.install += Widget.Text('This may take a while')

#=============================================

gui.page = Page.home

gui.run()