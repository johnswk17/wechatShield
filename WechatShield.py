import datetime
import os
from stat import S_IREAD, S_IRGRP, S_IROTH
#文件夹路径
playerPath = 'C:\\Users\\Administrator\\AppData\\Roaming\\Tencent\\WeChat\\log\\player/'
logPath = 'C:\\Users\\Administrator\\AppData\\Roaming\\Tencent\\WeChat\\log/'
webPath = 'C:\\Users\\Administrator\\AppData\\Roaming\\Tencent\\WeChat\\log\\xweb/'
filePath = 'C:\\Users\\Administrator\\AppData\\Roaming\\Tencent\\WeChat\\log\\WeChatXFile/'

date = datetime.datetime.now()
for i in range(1, 10):
    modified_date = (date + datetime.timedelta(days=i)).strftime("%Y%m%d")
#文件名称--设置和微信产生的一摸一样
    playName = 'player_'+modified_date+'.xlog'
    logName = 'MM_'+modified_date+'.xlog'
    webName = 'xweb_'+modified_date+'.xlog'
    fileName = 'xfile_'+modified_date+'.xlog'
#具体的每个文件路径
    player = playerPath+playName
    log = logPath + logName
    web = webPath + webName
    file = filePath + fileName
#创建新文件，阻止微信自动创建文件
    playF = open(player, "a")
    logF = open(log, "a")
    webF = open(web, "a")
    fileF = open(file, "a")
#写入空值
    playF.write("")
    logF.write("")
    webF.write("")
    fileF.write("")

    playF.close()
    logF.close()
    webF.close()
    fileF.close()
#修改文件的属性为只读，阻止微信写入信息
    os.chmod(player, S_IREAD | S_IRGRP | S_IROTH)
    os.chmod(log, S_IREAD | S_IRGRP | S_IROTH)
    os.chmod(web, S_IREAD | S_IRGRP | S_IROTH)
    os.chmod(file, S_IREAD | S_IRGRP | S_IROTH)