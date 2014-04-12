def sanitize(time_str):
    if '-' in time_str:
        splitter = '-'
    elif ':' in time_str:
        splitter = ':'
    else:
        return(time_str)
    
    (mins, secs) = time_str.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()

        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

sarah = get_coach_data('sarah2.txt')
#print(sarah)

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
#print(sarah_data['Times'])

print(sarah_data['Name'] + "'s fastest times are: " 
		+ str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))

#print([sanitize(t) for t in sarah_data['Times']])
