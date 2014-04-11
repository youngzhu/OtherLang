# -*- coding: gbk -*-
def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return(time_str)
    
    (mins, secs) = time_str.split(splitter)
    return(mins + '.' + secs)
"""
将后面对数据一些的处理整合到方法里
让该方法直接返回一个 字典
"""
def get_coach_data(filename):
    sarah_data = {}
    
    try:
        with open(filename) as f:
            data = f.readline()

        data_list = data.strip().split(',')
        
        sarah_data['Name'] = data_list.pop(0)
        sarah_data['DOB'] = data_list.pop(0)
        sarah_data['Times'] = data_list

        return(sarah_data)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

sarah_data = get_coach_data('sarah2.txt')
#print(sarah)



#print(sarah_data['Times'])

print(sarah_data['Name'] + "'s fastest times are: " 
		+ str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))

#print([sanitize(t) for t in sarah_data['Times']])
