from philh_myftp_biz.gui import GUI, Widget
from philh_myftp_biz.file import temp, ZIP
from philh_myftp_biz.web import download
from philh_myftp_biz.pc import Path

#=============================================

def confirm(name: str):

    dest = Path(f'C:/Program Files/AdobeCrack/{name}')

    Page.confirm += Widget.Header(name)

    Page.confirm += Widget.Text(f'Installation Path: {dest}')

    Page.confirm += Widget.Button(
        text = 'Back',
        onclick = Page.home
    )

    Page.confirm += Widget.Button(
        text = 'Confirm',
        onclick = lambda: install(name, dest)
    )

    gui.page = Page.confirm
    
def install(
    name: str,
    dest: Path
):
    
    Page.install += Widget.Header(name)
    
    tempfile = temp('adobe_download', 'zip')
    url = f'https://philh.myftp.biz/Media/Programs/Adobe/{name}.zip'

    Page.install += Widget.Text(f'Downloading ...\n{url=}\n{tempfile=}')

    gui.page = Page.install

    download(
        url = url,
        path = tempfile
    )

    Page.install[-1]['text'] = f'Extracting ...\n{tempfile=}\n{dest=}'
    gui.page = Page.install

    dest.delete()

    zip = ZIP(tempfile)

    zip.extractAll(dest)

#=============================================
# GUI

gui = GUI()

gui.title = 'Adobe Installer'

class Page:

    home = gui.Page()
    confirm = gui.Page()
    install = gui.Page()

#=============================================
# PAGE: HOME

Page.home += Widget.Header('Adobe Installer')

Page.home += Widget.Button(
    text = 'Photoshop',
    onclick = lambda: confirm('Photoshop')
)

Page.home += Widget.Button(
    text = 'Premiere Pro',
    onclick = lambda: confirm('Premiere Pro')
)

#=============================================

gui.page = Page.home

gui.run()