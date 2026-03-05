from philh_myftp_biz.gui import GUI, Widget
from philh_myftp_biz.process import Start
from philh_myftp_biz.web import download
from philh_myftp_biz.pc import tempdir
from philh_myftp_biz.file import ZIP

#=============================================

def confirm(name:str) -> None:

    Pages.confirm[0]['text'] = name

    Pages.confirm[2]['command'] = lambda: install(name)

    gui.page = Pages.confirm
    
def install(name:str) -> None:
    
    gui.page = Pages.install

    zip = tempdir.child(f'adobe_download.zip')
    dir = tempdir.child(f'/adobe_download/')
    url = f'https://philh.myftp.biz/Media/Programs/Adobe/{name}.zip'
    
    Pages.install[0]['text'] = name
    Pages.install[1]['text'] = f'Downloading ...\n{url=}\n{zip=}'
    gui.reload()

    download(url, zip)

    Pages.install[-1]['text'] = f'Extracting ...\n{zip=}\n{dir=}'
    gui.reload()

    dir.delete()
    ZIP(zip).extractAll(dir)

    zip.delete()

    Pages.install[-1]['text'] = f"Running 'autoplay.exe'"
    gui.reload()

    for file in dir.descendants:

        if file.seg() == 'autoplay.exe':
            
            Start(file)

            break

    Pages.install[-1]['text'] = f"Please continue in the newly opened window"
    
    Pages.install += Widget.Button(
        text = 'Back',
        onclick = Pages.home
    )

    gui.reload()

#=============================================
# GUI

gui = GUI()

gui.title = 'Adobe Installer'

gui.size = (1000, 500)

class Pages:

    home = gui.Page()
    confirm = gui.Page()
    install = gui.Page()

#=============================================
# PAGE: HOME

Pages.home += Widget.Header('Adobe Installer')

Pages.home += Widget.Button(
    text = 'Photoshop',
    onclick = lambda: confirm('Photoshop')
)

Pages.home += Widget.Button(
    text = 'Premiere Pro',
    onclick = lambda: confirm('Premiere Pro')
)

#=============================================
# PAGE: CONFIRM

Pages.confirm += Widget.Header()

Pages.confirm += Widget.Button(
    text = 'Back',
    onclick = Pages.home
)

Pages.confirm += Widget.Button(
    text = 'Download'
)

#=============================================
# PAGE: INSTALL

Pages.install += Widget.Header()

Pages.install += Widget.Text()

#=============================================

gui.page = Pages.home

gui.run()