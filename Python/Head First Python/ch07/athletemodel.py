import pickle

class Athlete(list):
    def __init__(self, name, dob, times):
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        print(self.name + "'s fastest times are: " 
		+ str(sorted(set([sanitize(t) for t in self]))[0:3]))

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()

        data_list = data.strip().split(',')
        
        name = data_list.pop(0)
        dob = data_list.pop(0)
        times = data_list

        return(Athlete(name, dob, times))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)    

def put_to_store(file_list):
    all_athletes = {}

    
    for each_file in file_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_sotre): ' + str(ioerr))

    return (all_athletes)

def get_from_store():
    all_athletes = {}

    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)

    except IOError as ioerr:
        print('File error(get_from_store): ' + str(ioerr))

    return (all_athletes)

dir()

the_files = ['sarah2.txt']
data = put_to_store(the_files)
data
