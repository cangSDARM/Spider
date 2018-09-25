#------------------------------------------------------------------------------------------------
								Selenium 和 PhantomJS
#Selenium 是web自动化测试工具
#	可以根据指令让浏览器自动加载界面, 获取数据甚至截屏
#PhantomJS 是基于webkit的无界面浏览器
#	通过将网页加载到内存执行js
from selenium import webdriver
from selenium.webdriver.common.keys import Keys	#调用键盘操作

driver = webdriver.PhantomJS()
#driver = webdriver.PhantomJS(execute_path="C:\\Program Files(x86)\\Microsoft Visual Studio\\Shared\\phantom-2.7.1\\bin")

#阻断, 等待界面完全被加载
driver.get("url")

#---------------------------------等待ajax处理异步加载
#In visible
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait			#负责循环等待
from selenium.webdriver.support import expected_conditions as ec	#条件触发
eler = WebDriverWait(driver, 10).until(
	ec.presence_of_element_located((By.ID, "sde"))	#等待特殊id出现
)
#Un visible
driver.implicitly_wait(10)	#10s
#------------------------------------------------

#----------------------------------查找节点和发送键盘消息
#JS有的方法, selenium应该都有
#获取内容
data = driver.find_element_by_id("war").text
#发送字符串
ele0 = driver.find_element_by_name("kw").send_keys(u"ss")
#发送组合键
ele1 = driver.find_element_by_tag_name("sd").send_keys(Keys.CONTROL, "a")
#发送点击事件
ele = driver.find_element_by_xpath("//div[@class='d']").click()

#拖曳 ele1 -> ele2
ActionChains(driver).drag_and_drop(ele1, ele2).perform()

#鼠标
ActionChains(driver).move_to_element(ele).double_click(ele).perform()	#双击
ActionChains(driver).move_to_element(ele).click_and_hold(ele).perform()	#左键hold
ActionChains(driver).move_to_element(ele).context_click(ele).perform()	#右键单击

#下拉框类
from selenium.webdriver.support.ui import Sslect

driver.page_source()
driver.get_cookies()
driver.current_url
title = driver.title
#------------------------------------------------------

#多页面
for handle in driver.window_handles:
	driver.switch_to_window(handle)	#窗口切换

#弹窗
alert = driver.switch_to_alert()

#前进后退
driver.forword()
driver.back()
	
#执行JS
driver.execute_script(js)	

#捕捉网页快照
snapshot = driver.save_screenshot("xxx.png")

#关闭页面. 一个页面同时关闭浏览器
driver.close()

#关闭浏览器
driver.quit()