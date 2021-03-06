# -*- encoding=utf8 -*-
__author__ = "Snow"

from airtest.core.api import *
import logging
logging.getLogger("airtest").setLevel(logging.INFO)

connect_device("android://127.0.0.1:5037/127.0.0.1:21533?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH")
stop_app("com.igg.android.lordsmobile")
start_app("com.igg.android.lordsmobile")
auto_setup(__file__)
##const
#resources
stone = 0
wood = 0
ore = 0
gold = 0
findSwipe=5

#swipe position
swipeDuration=1.5
swipeSteps=0

##init
resource = [stone, wood, ore, gold]
#building
b1=[(550,240),(700,220),(700,110),(840,120)]

##one
def closeAll():
    print("close all")
    while exists(Template(r"tpl1631618318759.png", record_pos=(0.153, -0.231), resolution=(1280, 720))) != False:
        keyevent("BACK")
        sleep(2.0)


def checkCastleMap():
    if exists(
            Template(r"tpl1631627327541.png", record_pos=(-0.473, 0.172), resolution=(1280, 720))) != False and exists(
        Template(r"tpl1631625805932.png", record_pos=(-0.435, 0.24), resolution=(1280, 720))) == False:
        touch(Template(r"tpl1631627327541.png", record_pos=(-0.473, 0.172), resolution=(1280, 720)))
        sleep(2.0)
        touch(Template(r"tpl1631625805932.png", record_pos=(-0.435, 0.24), resolution=(1280, 720)))
    elif exists(Template(r"tpl1631625805932.png", record_pos=(-0.435, 0.24), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631625805932.png", record_pos=(-0.435, 0.24), resolution=(1280, 720)))


def openLeftBar():
    if exists(Template(r"tpl1631629011572.png", record_pos=(-0.465, -0.13), resolution=(1280, 720))) != False:
        touch((46, 194))
        sleep(2.0)


def closeLeftBar():
    if exists(Template(r"tpl1631630457927.png", record_pos=(-0.465, -0.123), resolution=(1280, 720))) != False:
        touch((46, 194))
        sleep(2)


def present():
    closeAll()
    if exists(Template(r"tpl1631701085679.png", record_pos=(0.057, 0.245), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631701085679.png", record_pos=(0.057, 0.245), resolution=(1280, 720)))
        sleep(1)
        touch(Template(r"tpl1631704236739.png", record_pos=(0.434, -0.148), resolution=(1280, 720)))
        if exists(Template(r"tpl1631701188651.png", record_pos=(-0.001, -0.102), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631701188651.png", record_pos=(-0.001, -0.102), resolution=(1280, 720)))
            sleep(1)
            if exists(Template(r"tpl1631701201936.png", record_pos=(-0.006, 0.193), resolution=(1280, 720))) != False:
                touch(Template(r"tpl1631701201936.png", record_pos=(-0.006, 0.193), resolution=(1280, 720)))
                sleep(1)
                if exists(Template(r"tpl1631474241345.png", record_pos=(-0.115, -0.004),
                                   resolution=(1072, 693))) != False:
                    touch(Template(r"tpl1631474241345.png", record_pos=(-0.115, -0.004), resolution=(1072, 693)))
                    touch(Template(r"tpl1631474427085.png", record_pos=(0.321, -0.179), resolution=(1072, 693)))
    closeAll()


# swipe position
def swipeLeft(count):
    while count > 0:
        swipe((640, 360), (1280,360), duration=swipeDuration, steps=swipeSteps)
        count = count - 1


def swipeRight(count):
    while count > 0:
        swipe((640, 360), (0,360), duration=swipeDuration, steps=swipeSteps)
        count = count - 1


def swipeUp(count):
    while count > 0:
        swipe((640, 360),(640,720), duration=swipeDuration, steps=swipeSteps)
        count = count - 1


def swipeDown(count):
    while count > 0:
        swipe((640, 360), (640,0), duration=swipeDuration, steps=swipeSteps)
        count = count - 1

##loop
def closeTasks():
    closeAll()
    print("close tasks")
    if exists(Template(r"tpl1631366089757.png", record_pos=(0.126, 0.253), resolution=(1300, 753))) != False:
        touch(Template(r"tpl1631366089757.png", record_pos=(0.126, 0.253), resolution=(1300, 753)))
    # ??????????????????
    if exists(Template(r"tpl1631371046420.png", record_pos=(-0.35, -0.162), resolution=(1255, 753))) != False:
        touch(Template(r"tpl1631366552660.png", record_pos=(-0.357, -0.151), resolution=(1277, 753)))
        sleep(1.0)
        while exists(Template(r"tpl1631366975366.png", record_pos=(0.319, 0.045), resolution=(1277, 753))) != False:
            touch(Template(r"tpl1631366975366.png", record_pos=(0.319, 0.045), resolution=(1277, 753)))
            sleep(2.0)

        if exists(Template(r"tpl1631372076337.png", record_pos=(-0.005, -0.069), resolution=(1125, 753))) != False:
            touch(Template(r"tpl1631372076337.png", record_pos=(-0.005, -0.069), resolution=(1125, 753)))
    elif exists(Template(r"tpl1631388182976.png", record_pos=(-0.355, -0.159), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631469639329.png", record_pos=(-0.295, -0.233), resolution=(842, 693)))
        sleep(1.0)
        while exists(Template(r"tpl1631475364822.png", record_pos=(0.32, 0.035), resolution=(1072, 693))) != False:
            touch(Template(r"tpl1631475364822.png", record_pos=(0.32, 0.035), resolution=(1072, 693)))

            sleep(2.0)

        if exists(Template(r"tpl1631372076337.png", record_pos=(-0.005, -0.069), resolution=(1125, 753))) != False:
            touch(Template(r"tpl1631372076337.png", record_pos=(-0.005, -0.069), resolution=(1125, 753)))
    # ???????????? ????????????????
    if exists(Template(r"tpl1631469745417.png", record_pos=(-0.179, -0.188), resolution=(1072, 693))) != False:
        touch(Template(r"tpl1631469745417.png", record_pos=(-0.179, -0.188), resolution=(1072, 693)))
        while exists(Template(r"tpl1631469872801.png", record_pos=(0.315, 0.047), resolution=(1072, 693))) != False:
            touch(Template(r"tpl1631469872801.png", record_pos=(0.315, 0.047), resolution=(1072, 693)))
            sleep(1.0)

    # ???????????? ??????
    if exists(Template(r"tpl1631367979569.png", record_pos=(0.005, -0.151), resolution=(1277, 753))) != False:
        touch(Template(r"tpl1631367997101.png", record_pos=(0.007, -0.152), resolution=(1277, 753)))
        while exists(Template(r"tpl1631368095322.png", record_pos=(0.302, -0.047), resolution=(1277, 753))) != False:
            touch(Template(r"tpl1631368127128.png", record_pos=(0.298, -0.045), resolution=(1277, 753)))
            sleep(1.0)

    # ???????????? ??????????????
    if exists(Template(r"tpl1631368509146.png", record_pos=(0.21, -0.15), resolution=(1277, 753))) != False:
        touch(Template(r"tpl1631368529371.png", record_pos=(0.211, -0.149), resolution=(1277, 753)))
        while exists(Template(r"tpl1631368127128.png", record_pos=(0.298, -0.045), resolution=(1277, 753))) != False:
            touch(Template(r"tpl1631368127128.png", record_pos=(0.298, -0.045), resolution=(1277, 753)))
            sleep(1.0)

    # ?????? ??????????????
    if exists(Template(r"tpl1631366510890.png", record_pos=(0.352, -0.155), resolution=(1277, 753))) != False:
        touch(Template(r"tpl1631366569702.png", record_pos=(0.357, -0.149), resolution=(1277, 753)))
        if exists(Template(r"tpl1631630051759.png", record_pos=(-0.231, 0.002), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631630051759.png", record_pos=(-0.231, 0.002), resolution=(1280, 720)))
            sleep(1.0)
    closeAll()


def guildHelp():
    closeAll()
    if exists(Template(r"tpl1631642702197.png", record_pos=(0.473, 0.144), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631642702197.png", record_pos=(0.473, 0.144), resolution=(1280, 720)))
        sleep(2.0)
        if exists(Template(r"tpl1631644066859.png", record_pos=(-0.002, 0.235), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631644066859.png", record_pos=(-0.002, 0.235), resolution=(1280, 720)))
            sleep(2)
    closeAll()


def openChest():
    closeAll()
    if exists(Template(r"tpl1631368754416.png", record_pos=(0.409, 0.152), resolution=(1255, 753))) != False and exists(
            Template(r"tpl1631623157409.png", record_pos=(0.392, 0.145), resolution=(1280, 720))) == False:
        while exists(Template(r"tpl1631471139884.png", record_pos=(-0.001, 0.158), resolution=(1072, 693))) == False:
            touch(Template(r"tpl1631368754416.png", record_pos=(0.409, 0.152), resolution=(1255, 753)))
            sleep(2.0)
        touch(Template(r"tpl1631471139884.png", record_pos=(-0.001, 0.158), resolution=(1072, 693)))
        sleep(2.0)
    closeAll()


def guildGifts():
    closeAll()
    touch(Template(r"tpl1631385294171.png", record_pos=(-0.03, 0.248), resolution=(1280, 720)))
    if exists(Template(r"tpl1631470836711.png", record_pos=(0.392, -0.153), resolution=(1072, 693))) != False or exists(
            Template(r"tpl1631470809764.png", record_pos=(0.392, -0.153), resolution=(1072, 693))) != False:
        touch(Template(r"tpl1631385839765.png", record_pos=(0.429, -0.132), resolution=(1280, 720)))

        if exists(Template(r"tpl1631384942057.png", record_pos=(0.252, -0.077), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631384942057.png", record_pos=(0.252, -0.077), resolution=(1280, 720)))
            touch(Template(r"tpl1631385018542.png", record_pos=(0.03, -0.092), resolution=(1280, 720)))
            sleep(1.0)
            while exists(
                    Template(r"tpl1631385034677.png", record_pos=(0.364, -0.044), resolution=(1280, 720))) != False:
                touch(Template(r"tpl1631385034677.png", record_pos=(0.364, -0.044), resolution=(1280, 720)))
                sleep(1.0)

            touch(Template(r"tpl1631385397014.png", record_pos=(0.321, -0.163), resolution=(1280, 720)))
            sleep(1.0)
            touch(Template(r"tpl1631385144412.png", record_pos=(0.286, -0.094), resolution=(1280, 720)))
            sleep(1.0)
            while exists(
                    Template(r"tpl1631385034677.png", record_pos=(0.364, -0.044), resolution=(1280, 720))) != False:
                touch(Template(r"tpl1631385034677.png", record_pos=(0.364, -0.044), resolution=(1280, 720)))
                sleep(1.0)
            touch(Template(r"tpl1631385397014.png", record_pos=(0.321, -0.163), resolution=(1280, 720)))
            sleep(1.0)
            touch(Template(r"tpl1631385429596.png", record_pos=(0.466, -0.248), resolution=(1280, 720)))
            sleep(1.0)
    closeAll()


def getHelpFree():
    closeAll()
    openLeftBar()
    if exists(Template(r"tpl1631369514748.png", record_pos=(-0.186, -0.133), resolution=(1255, 753))) != False:
        touch(Template(r"tpl1631369514748.png", record_pos=(-0.186, -0.133), resolution=(1255, 753)))
    if exists(Template(r"tpl1631369849798.png", record_pos=(-0.186, -0.133), resolution=(1255, 753))) != False:
        touch(Template(r"tpl1631369849798.png", record_pos=(-0.186, -0.133), resolution=(1255, 753)))
    closeLeftBar()
    closeAll()


def getChestGran():
    closeAll()
    if exists(Template(r"tpl1631390090200.png", record_pos=(-0.05, 0.004), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631390090200.png", record_pos=(-0.05, 0.004), resolution=(1280, 720)))
        touch(Template(r"tpl1631390117845.png", record_pos=(-0.176, 0.23), resolution=(1280, 720)))
        while exists(Template(r"tpl1631390152719.png", record_pos=(-0.237, 0.106), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631390152719.png", record_pos=(-0.237, 0.106), resolution=(1280, 720)))
            touch((0,0))
            sleep(5.0)
            touch(Template(r"tpl1631390218719.png", record_pos=(0.466, -0.248), resolution=(1280, 720)))
            closeAll()
            return True
    closeAll()
    return False


def shelter():
    closeAll()
    swipeUp(1)
    if exists(Template(r"tpl1631689496537.png", record_pos=(0.113, -0.175), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631689496537.png", record_pos=(0.113, -0.175), resolution=(1280, 720)))
        if exists(Template(r"tpl1631689554781.png", record_pos=(0.06, 0.094), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631689554781.png", record_pos=(0.06, 0.094), resolution=(1280, 720)))
        sleep(1.0)

        touch(Template(r"tpl1631689586915.png", record_pos=(0.002, 0.155), resolution=(1280, 720)))
        sleep(1.0)
        if exists(Template(r"tpl1631689649379.png", record_pos=(-0.184, -0.153), resolution=(1280, 720))) == False:
            touch(Template(r"tpl1631689649379.png", record_pos=(-0.184, -0.153), resolution=(1280, 720)))
            sleep(1.0)
        touch(Template(r"tpl1631694073307.png", record_pos=(0.274, 0.05), resolution=(1280, 720)))
        sleep(1.5)
        touch(Template(r"tpl1631694109424.png", record_pos=(0.07, -0.03), resolution=(1280, 720)))
        sleep(1.5)
        touch(Template(r"tpl1631694123095.png", record_pos=(0.275, 0.166), resolution=(1280, 720)))
        sleep(3.0)
    closeAll()
    swipeDown(1)

##building
def upgradeAllFarms():
    closeAll()
    print("upgrade all farms")
    swipeDown(1)
    for b in b1:
        touch(b)
        sleep(1)
        if upgrade()==True:
            break
    closeAll()
    swipeUp(1)


def upgrade():
    if exists(Template(r"tpl1631698911711.png", record_pos=(0.358, 0.218), resolution=(1280, 720))) != False:
        touch(Template(r"tpl1631698911711.png", record_pos=(0.358, 0.218), resolution=(1280, 720)))
        sleep(2)
        if exists(Template(r"tpl1631699030898.png", record_pos=(0.134, 0.19), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631699030898.png", record_pos=(0.134, 0.19), resolution=(1280, 720)))
            sleep(1)
            if exists(Template(r"tpl1631699109306.png", record_pos=(-0.001, -0.164),
                               resolution=(1280, 720))) != False and exists(
                Template(r"tpl1631699121522.png", record_pos=(-0.009, -0.015), resolution=(1280, 720))) != False:
                touch(Template(r"tpl1631699121522.png", record_pos=(-0.009, -0.015), resolution=(1280, 720)))
                while exists(
                        Template(r"tpl1631699180173.png", record_pos=(0.305, -0.136), resolution=(1280, 720))) != False:
                    touch(Template(r"tpl1631699180173.png", record_pos=(0.305, -0.136), resolution=(1280, 720)))
                    sleep(2)
                if exists(Template(r"tpl1631699030898.png", record_pos=(0.134, 0.19), resolution=(1280, 720))) != False:
                    touch(Template(r"tpl1631699030898.png", record_pos=(0.134, 0.19), resolution=(1280, 720)))
                    sleep(1)
            return True
    closeAll()
    return False

##army
def isTraning():
    try:
        if exists(Template(r"tpl1631878256316.png", record_pos=(0.119, 0.054), resolution=(1280, 720))) == False:
            return True
        closeLeftBar()
        return False
    except:
        print("Unexpected error:", sys.exc_info()[0])


def healArmy():
    closeAll()

def createT2Horse():
    try:
        if isTraning() == False:
            closeAll()
            touch(Template(r"tpl1631878256316.png", record_pos=(0.119, 0.054), resolution=(1280, 720)))
            sleep(2.0)
            if exists(Template(r"tpl1631530398376.png", record_pos=(0.094, -0.037), resolution=(1280, 720))) == False:
                swipe((640, 460), vector=[0, -0.4], duration=1, steps=2)
                sleep(2.0)
            touch(Template(r"tpl1631530398376.png", record_pos=(0.094, -0.037), resolution=(1280, 720)))
            sleep(2.0)

            touch(Template(r"tpl1631878167766.png", record_pos=(0.373, 0.079), resolution=(1280, 720)))
            sleep(2.0)
            touch(Template(r"tpl1631880801599.png", record_pos=(0.364, 0.205), resolution=(1280, 720)))
            sleep(2.0)
            if exists(Template(r"tpl1631879784011.png", record_pos=(0.102, 0.207), resolution=(1280, 720))) != False:
                touch(Template(r"tpl1631879784011.png", record_pos=(0.102, 0.207), resolution=(1280, 720)))
                sleep(1.0)
            closeAll()
    except:
        print("Unexpected error:", sys.exc_info()[0])


##resources
def getFood():
    try:
        closeAll()
        if exists(Template(r"tpl1631534149841.png", record_pos=(-0.051, -0.093), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631534149841.png", record_pos=(-0.051, -0.093), resolution=(1280, 720)))
        else:
            closeAll()
            return False
        if exists(Template(r"tpl1631534435375.png", record_pos=(0.005, -0.03), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631466885882.png", record_pos=(0.007, 0.005), resolution=(1043, 654)))
            touch(Template(r"tpl1631469075929.png", record_pos=(0.185, 0.056), resolution=(1072, 693)))
            touch(Template(r"tpl1631530275158.png", record_pos=(-0.015, 0.022), resolution=(1280, 720)))
            touch(Template(r"tpl1631469164517.png", record_pos=(0.286, 0.187), resolution=(1072, 693)))
            sleep(1)
            closeAll()
            return True
    except:
        print("Unexpected error:", sys.exc_info()[0])


def getStone():
    try:
        closeAll()
        if exists(Template(r"tpl1631532800425.png", record_pos=(-0.087, 0.03), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631532800425.png", record_pos=(-0.087, 0.03), resolution=(1280, 720)))
        elif exists(Template(r"tpl1631532851551.png", record_pos=(-0.237, 0.11), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631532851551.png", record_pos=(-0.237, 0.11), resolution=(1280, 720)))
        elif exists(Template(r"tpl1631532954572.png", record_pos=(-0.095, 0.03), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631532954572.png", record_pos=(-0.095, 0.03), resolution=(1280, 720)))
        else:
            closeAll()
            return False
        if exists(Template(r"tpl1631534435375.png", record_pos=(0.005, -0.03), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631466885882.png", record_pos=(0.007, 0.005), resolution=(1043, 654)))
            touch(Template(r"tpl1631469075929.png", record_pos=(0.185, 0.056), resolution=(1072, 693)))
            touch(Template(r"tpl1631530275158.png", record_pos=(-0.015, 0.022), resolution=(1280, 720)))
            touch(Template(r"tpl1631469164517.png", record_pos=(0.286, 0.187), resolution=(1072, 693)))
            sleep(1.0)
            closeAll()
            return True
    except:
        print("Unexpected error:", sys.exc_info()[0])


def getWood():
    try:
        closeAll()
        if exists(Template(r"tpl1631475534633.png", record_pos=(-0.142, 0.094), resolution=(1072, 693))) != False:
            touch(Template(r"tpl1631475534633.png", record_pos=(-0.142, 0.094), resolution=(1072, 693)))
        elif exists(Template(r"tpl1631529566699.png", record_pos=(-0.064, 0.109), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631529566699.png", record_pos=(-0.064, 0.109), resolution=(1280, 720)))
        elif exists(Template(r"tpl1631529693778.png", record_pos=(-0.023, 0.146), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631529693778.png", record_pos=(-0.023, 0.146), resolution=(1280, 720)))
        else:
            closeAll()
            return False
        if exists(Template(r"tpl1631534435375.png", record_pos=(0.005, -0.03), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631466885882.png", record_pos=(0.007, 0.005), resolution=(1043, 654)))
            touch(Template(r"tpl1631469075929.png", record_pos=(0.185, 0.056), resolution=(1072, 693)))
            touch(Template(r"tpl1631530275158.png", record_pos=(-0.015, 0.022), resolution=(1280, 720)))
            touch(Template(r"tpl1631469164517.png", record_pos=(0.286, 0.187), resolution=(1072, 693)))
            sleep(1.0)
            closeAll()
            return True
    except:
        print("Unexpected error:", sys.exc_info()[0])


def getOre():
    try:
        closeAll()
        if exists(Template(r"tpl1631627092588.png", record_pos=(0.044, 0.056), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631627092588.png", record_pos=(0.044, 0.056), resolution=(1280, 720)))
        elif exists(Template(r"tpl1631627218803.png", record_pos=(-0.202, 0.006), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631627218803.png", record_pos=(-0.202, 0.006), resolution=(1280, 720)))
        else:
            closeAll()
            return
        if exists(Template(r"tpl1631534435375.png", record_pos=(0.005, -0.03), resolution=(1280, 720))) != False:
            touch(Template(r"tpl1631466885882.png", record_pos=(0.007, 0.005), resolution=(1043, 654)))
            touch(Template(r"tpl1631469075929.png", record_pos=(0.185, 0.056), resolution=(1072, 693)))
            touch(Template(r"tpl1631530275158.png", record_pos=(-0.015, 0.022), resolution=(1280, 720)))
            touch(Template(r"tpl1631469164517.png", record_pos=(0.286, 0.187), resolution=(1072, 693)))
            sleep(1.0)
            closeAll()
            return True
        closeAll()
    except:
        print("Unexpected error:", sys.exc_info()[0])


def getGold():
    closeAll()


# change res
def getResources():
    if resource[0] == max(resource):
        if getStone() == True:
            resource[1] = resource[1] - 1
            return True
    if resource[1] == max(resource):
        if getWood() == True:
            resource[1] = resource[1] - 1
            return True
    if resource[2] == max(resource):
        if getOre() == True:
            resource[2] = resource[2] - 1
            return True
    if resource[3] == max(resource):
        if getGold() == True:
            resource[3] = resource[3] - 1
            return True

# find res
def findResources():
    try:
        closeAll()
        if exists(Template(r"tpl1631477984643.png", record_pos=(-0.476, -0.051), resolution=(1072, 693))) == False:
            if exists(Template(r"tpl1631387825373.png", record_pos=(-0.433, 0.234), resolution=(1280, 720))) != False:
                touch(Template(r"tpl1631387825373.png", record_pos=(-0.433, 0.234), resolution=(1280, 720)))
            sleep(5.0)
            touch(Template(r"tpl1631627304207.png", record_pos=(-0.474, 0.171), resolution=(1280, 720)))

            if getResources() == True:
                checkCastleMap()
                return None
            i = 0
            while (i < findSwipe):
                swipeRight(1)
                i = i + 1
                if getResources() == True:
                    checkCastleMap()
                    return None
            touch(Template(r"tpl1631472050044.png", record_pos=(0.316, -0.144), resolution=(1072, 693)))
            i = 0
            while (i < findSwipe):
                swipeLeft(1)
                i = i + 1
                if getResources() == True:
                    checkCastleMap()
                    return None
            touch(Template(r"tpl1631472050044.png", record_pos=(0.316, -0.144), resolution=(1072, 693)))
            i = 0
            while (i < findSwipe):
                swipeUp(1)
                i = i + 1
                if getResources() == True:
                    checkCastleMap()
                    return None
            touch(Template(r"tpl1631472050044.png", record_pos=(0.316, -0.144), resolution=(1072, 693)))
            i = 0
            while (i < findSwipe):
                swipeDown(1)
                i = i + 1
                if getResources() == True:
                    checkCastleMap()
                    return None
            closeAll()
            checkCastleMap()
            #???????????????? ?????? ???????????????? ???????? ?????????????? ???????? ???????????? ???? ??????????
            resource[resource.index(min(resource))]=resource[resource.index(min(resource))]+1
    except:
        print("Unexpected error:", sys.exc_info()[0])


# ???????????????? ????????????????
countChestGran = 5
# ???????????????????? ?????????? n ????????????????

##main
#???????? ???????? ??????????????????????
sleep(3)
while exists(Template("loading.png")) != False:
    sleep(2)
closeAll()
# ???????????????????? ???????? ??????
closeAll()
checkCastleMap()
shelter()
present()
# ?????????????????? ??????????????????
while True:
    # ?????????????????? ?????? ?????? ???????????? ???? ????????????
    closeAll()
    checkCastleMap()
    sleep(1.0)
    getHelpFree()
    sleep(1.0)
    createT2Horse()
    sleep(1)
    upgradeAllFarms()
    sleep(1)
    guildHelp()
    sleep(1.0)
    openChest()
    sleep(1.0)
    closeTasks()
    sleep(1.0)
    # ??????????????
    if countChestGran >= 0:
        # ???????? ??????????????
        if getChestGran() == True:
            countChestGran = countChestGran - 1
    sleep(1.0)
    guildGifts()
    sleep(1.0)
    findResources()














