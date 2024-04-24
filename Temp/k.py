from DrissionPage import ChromiumPage
from DrissionPage.common import Actions

page = ChromiumPage()
page.set.window.max()
ac = Actions(page)
page.get('https://www.taobao.com/')
# ac.move_to('xpath://*[@id="J_Search"]/div/ul')
# page.ele('text:店铺').click()
page.ele('xpath://*[@id="J_Search"]/div/ul/li[3]/span').click()
page.ele('xpath://*[@id="J_Search"]/div/ul/li[3]/span').click()
page.ele('xpath://*[@id="q"]').input('弘达汽车用品店')
page.ele('xpath://*[@id="J_TSearchForm"]/div[1]/button').click()
page.ele('xpath://*[@id="list-container"]/li[1]/ul/li[2]/h4/a[1]').click()

