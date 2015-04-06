# _*- coding: utf-8 -*-
import os
import time

# 各项的总数
v_squat_sum=0 # 深蹲
v_push_up_sum=0 # 俯卧撑
v_sit_up_sum=0 # 仰卧起坐
v_plank_sum=0 # 平板支撑 第一组

file_name_daily='./daily.log'

file_content=[]

# 判断文件是否存在
# 如果不存在，则新建一个
if os.path.exists(file_name_daily) :
    # 文件存在
    file_read=open(file_name_daily, 'r')
    file_content=file_read.readlines()
    file_read.close()
    #print(file_content) 
    if len(file_content) > 0 :
        #print(file_content[1].split('/')[1])
        v_squat_sum=int(file_content[1].split('/')[1])
        v_push_up_sum=int(file_content[2].split('/')[1])
        v_sit_up_sum=int(file_content[3].split('/')[1])
        v_plank_sum=int(file_content[4].split('/')[1])
else :
    # 文件不存在
    print '文件不存在！'
    answer=raw_input('确定创建文件吗？（Y|n）')
    if answer == 'Y' :
        # 创建文件
        f=open(file_name_daily, 'w')
        f.close()

# 输入当天的数据
data_today=raw_input('请按以下顺序输入数字，用逗号 `,` 隔开，按回车键结束\n（深蹲, 俯卧撑, 仰卧起坐, 平板支撑（一）, 平板支撑（二））：\n')
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
records.append('深蹲 ' + v_squat + '/' + str(v_squat_sum) + '\n')
records.append('俯卧撑 ' + v_push_up + '/' + str(v_push_up_sum) + '\n')
records.append('仰卧起坐 ' + v_sit_up + '/' + str(v_sit_up_sum) + '\n')
records.append('平板支撑 ' + v_plank_1 + '-' + v_plank_2 + '/' + str(v_plank_sum) + '\n')

records.extend('\n')
records.extend(file_content)

#print(records)
file_obj=open(file_name_daily, 'w')
file_obj.writelines([record for record in records])
file_obj.close()
