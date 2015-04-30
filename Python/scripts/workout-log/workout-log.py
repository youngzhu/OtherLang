# _*- coding: utf-8 -*-
import os
import time
import calendar

# 各项的总数
v_squat_sum=0 # 深蹲
v_push_up_sum=0 # 俯卧撑
v_sit_up_sum=0 # 仰卧起坐
v_plank_sum=0 # 平板支撑 第一组

file_name_daily='./daily.log'

file_content_daily=[]

# 判断文件是否存在
# 如果不存在，则新建一个
if os.path.exists(file_name_daily) :
    # 文件存在
    file_read=open(file_name_daily, 'r')
    file_content_daily=file_read.readlines()
    file_read.close()
    #print(file_content_daily) 
    if len(file_content_daily) > 0 :
        #print(file_content_daily[1].split('/')[1])
        v_squat_sum=int(file_content_daily[1].split('/')[1])
        v_push_up_sum=int(file_content_daily[2].split('/')[1])
        v_sit_up_sum=int(file_content_daily[3].split('/')[1])
        v_plank_sum=int(file_content_daily[4].split('/')[1])
else :
    # 文件不存在
    print u'文件不存在！'
    print u'确定创建文件吗？（Y|n）'
    answer=raw_input()
    if answer == 'Y' :
        # 创建文件
        f=open(file_name_daily, 'w')
        f.close()

# 输入当天的数据
print(u'请按以下顺序输入数字，用逗号 `,` 隔开，按回车键结束\n')
print(u'（深蹲, 俯卧撑, 仰卧起坐, 平板支撑（一）, 平板支撑（二））：\n')
data_today=raw_input()
#print data_today

list_today=data_today.split(',')
#print list_today
v_squat=list_today[0] # 深蹲
v_push_up=list_today[1] # 俯卧撑
v_sit_up=list_today[2] # 仰卧起坐
v_plank_1=list_today[3] # 平板支撑 第一组
v_plank_2=list_today[4] # 平板支撑 第二组

v_squat_sum+=int(v_squat)
v_push_up_sum+=int(v_push_up)
v_sit_up_sum+=int(v_sit_up)
v_plank_sum+=int(v_plank_1) + int(v_plank_2)

records=[] # 将要写入文件的内容（记录）

# 获取当前时间
v_now=time.strftime('%Y-%m-%d %X', time.localtime())
records.append(v_now + '\n')
records.append('深蹲 '+ v_squat + '/' + str(v_squat_sum) + '\n')
records.append('俯卧撑 '+ v_push_up + '/' + str(v_push_up_sum) + '\n')
records.append('仰卧起坐 '+ v_sit_up + '/' + str(v_sit_up_sum) + '\n')
records.append('平板支撑 ' + v_plank_1 + '-' + v_plank_2 + '/' + str(v_plank_sum) + '\n')

records.extend('\n')
records.extend(file_content_daily)

#print(records)
file_obj=open(file_name_daily, 'w')
file_obj.writelines([record for record in records])
file_obj.close()

################################## 日结结束 #############################

################################## 月结开始 #############################
'''
完成月结需要解决三个问题：
1 每月的总天数
    有现成的方法吗？
    如果没有，可以通过当月一号和下月一号之间的天数来计算。

2 每月锻炼的总天数
    遍历文件，有一条 yyyy-MM 就加一。

3 如何判断今天是否是本月的最后一天
    有现成的方法吗？
    如果没有，+1天后还在本月，说明不是。

    有现成的 方法获得当月的天数，则可通过今天的日期是否等于当月的总天数来判断。

'''

# 当天的年/月/日
v_year=int(time.strftime('%Y', time.localtime()))
v_mon=int(time.strftime('%m', time.localtime()))
v_day=int(time.strftime('%d', time.localtime()))
'''
print v_year 
print v_mon
print v_day
'''

# 当月的天数
days_of_mon=calendar.monthrange(v_year, v_mon)[1]
#print days_of_mon

last_day = (v_day == days_of_mon) # 是否是本月最后一天

file_name_monthly='./monthly.log'

# 如果是当月最后一天，则执行
if last_day :
    #print "是最后一天。"

    #### 创建文件monthly.log
    # 判断文件是否存在
    # 如果不存在，则新建一个
    if not os.path.exists(file_name_monthly) :
        # 文件不存在
        print file_name_monthly + u'文件不存在！'
        print u'确定创建文件吗？（Y|n）'
        answer=raw_input()
        if answer == 'Y' :
            # 创建文件
            f=open(file_name_monthly, 'w')
            f.close()
    # 遍历 daily.log 的内容，统计当月锻炼的天数
    v_counter=0 #计数器，当月的锻炼天数
    # yyyy-MM 当月，为了和遍历的文件内容做比较，
    # 方便统计当月的数据
    year_and_mon=time.strftime('%Y-%m', time.localtime())
    v_length=len(records)
    index=0
    while index < v_length:
        #print str(records[index])[:10] + '---' + str(records[index])
        #print year_and_mon + '--' + (str(records[index])[:7])
        if year_and_mon == (str(records[index])[:7]):
            v_counter+=1
            #print v_counter
            #print str(index) + '--' + str(v_length)
            index += 6 # 跳过锻炼的数据，只看时间数据
        else:
            #print str(index)
            break
    # 写入文件
    file_obj=open(file_name_monthly, 'a')
    file_obj.write(time.strftime('%B', time.localtime())+ '\n')
    file_obj.write('\tDAYS: ' + str(v_counter) + '/' + str(days_of_mon) + '\n')
    file_obj.close()
