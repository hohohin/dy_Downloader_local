from DrissionPage import ChromiumPage
from DownloadKit import DownloadKit

page = ChromiumPage()

page.get('https://www.douyin.com/video/7400340892428619042?modeFrom=')

ele1 = page.ele('.xg-video-container')

ele2 = ele1.child('',1).child('',1)

print(ele2.attr('src'))

page.quit()