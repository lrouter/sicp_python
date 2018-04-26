#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import os.path
import shutil
import ThirdPartyAuthAction
import BBBankSocialAccount
import BaseServicesSystemproperties
import IValidatorExceptionConstants
import Constants
import AcmMacBypassHandler
import RadiusRequestUtil
import OnlineUserNewAction
import OnlineUserExporter
import AccountFlag
import core_exception_en_US
import core_exception_pt_BR


# 数据结构
moduleList = [
    "ThirdPartyAuthAction",
    "BBBankSocialAccount",
    "BaseServicesSystemproperties",
    "IValidatorExceptionConstants",
    "Constants",
    "AcmMacBypassHandler",
    "RadiusRequestUtil",
    "OnlineUserNewAction",
    "OnlineUserExporter",
    "AccountFlag",
    "core_exception_en_US",
    "core_exception_pt_BR"
]

# 方法定义
def copy(targetDir, sourceFileName, targetSubFileNameList):
    #1 获得原始文件名
    #2 获得目标的相对路径和文件名，以AgileController开始
    #3 拼接目标文件的全文件名
    #4 获得目标文件的全目录
    #5 创建目录
    #6 复制文件

    count = 0
    for targetSubFileName in targetSubFileNameList:
        targetFileName = os.path.join(targetDir, targetSubFileName)
        targetFullDir = os.path.dirname(targetFileName)
        print("目标路径: " + targetFullDir + "\n")
        if not os.path.exists(targetFullDir):
            os.makedirs(targetFullDir)
        print("源文件名: " + sourceFileName + "\n")
        print("目标文件名: " + targetFileName + "\n")
        shutil.copyfile(sourceFileName, targetFileName)
        count += 1

    return count

# 主要代码逻辑
#  1. 根据当前时间生成目标路径
#  2. 遍历每个模块, 提取源文件和目标文件
#  3. 复制源文件，生成每个目标文件
#  4. 是否遍历了每个模块，如果没有，跳到步骤2
print("开始打包.\n")
targetDir = r"D:\31_SDN\06_开发需求\oauth2.0\补丁打包"
packageDir = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
targetDir = os.path.join(targetDir, packageDir)
print("打包路径为: " + targetDir)
fileCounts = 0
for module in moduleList:
    print("进入 %s 模块\n" %(module))
    sourceFileName = eval(module).sourceFileName
    targetSubFileNameList = eval(module).targetSubFileNameList
    fileCounts += copy(targetDir, sourceFileName, targetSubFileNameList)
    print("退出 %s 模块\n" % (module))
print("完成打包. ")
print("总共复制 %d 文件." %(fileCounts))

