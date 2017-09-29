import shutil, os, exifread
from datetime import datetime,date

# 建立课表，把这里换成自己的课表
mon_courses = {'08:00': "中宏", '10:00': "管理信息系统", '14:20': "组织行为学", '16:20': "战略管理", '19:00': "机制设计"}
tue_courses = {'08:00': "计量经济学", '14:20': "营销管理", '16:20': "房地产投资与融资"}
wed_courses = {'08:00': "中宏", '10:00': "管理信息系统", '14:20': "养老保险", '16:20': "卫生经济", '19:00': "机制设计"}
thu_courses = {'08:00': "计量经济学", '14:20': "跨国投资与兼并", '16:20': "投资项目评估"}
fri_courses = {'08:00': "投资学", '10:00': "就业指导"}
weekdays = [mon_courses, tue_courses, wed_courses, thu_courses, fri_courses]


# 建立时间分类列表
# mon = []
# tues = []
# wed = []
# thu = []
# fri = []
# weekdays = [mon, tues, wed, thu, fri]


# 获取时间信息
def get_info(picture):
    global data
    try:
        tags = exifread.process_file(picture)
        time = tags['EXIF DateTimeOriginal']
        data = datetime.strptime(str(time), '%Y:%m:%d %H:%M:%S')
    except:
        print('无法读取' + filename + '的时间')


# 星期分类
def get_pictures_weekdays(picture,data):
    pic_weekday = data.weekday()
    global weekday_courses
    try:
        weekday_courses = weekdays[int(pic_weekday)]# 改为变量
    except:
        weekday_courses = False


# 判断和移动
def judge_and_move(filename, data, weekday_courses):
    # tags = exifread.process_file(picture)
    # time = tags['EXIF DateTimeOriginal']
    # data = datetime.strptime(str(time), '%Y:%m:%d %H:%M:%S')
    pic_time = str(data.strftime('%H:%M'))
    pic_minute = int(pic_time[0:2])*60 + int(pic_time[3:])
    for course in weekday_courses.keys():
        course_minute = int(course[0:2])*60 + int(course[3:])
        # 算法需要起始时间
        if course_minute <= pic_minute <= course_minute + 110:
            print('已扫描' + filename)
            shutil.move(filename, os.path.join(r"C:\Users\sytj1\Desktop\第五学期课程", weekday_courses[course]))
            # shutil.copy(filename, os.path.join(r"C:\Users\sytj1\Desktop\第五学期课程", weekday_courses[course]))
            print('移动成功')

os.chdir(r"C:\Users\sytj1\Desktop\手机照片")
for folder_name, subfolders, filenames in os.walk(r"C:\Users\sytj1\Desktop\手机照片"):
# filename = r"C:\Users\sytj1\Desktop\手机照片\P70721-134750.jpg"
    for filename in filenames:
        # print(filename)
        picture = open(filename, 'rb')
        get_info(picture)
        if data > datetime.strptime('2017:09:03 00:00:00', '%Y:%m:%d %H:%M:%S'):
            get_pictures_weekdays(picture, data)
            picture.close()
            if weekday_courses:
                try:
                    judge_and_move(filename, data, weekday_courses)
                except:
                    print('移动' + filename + '失败')
        else:
            picture.close()

