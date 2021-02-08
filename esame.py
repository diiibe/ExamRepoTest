class ExamException(Exception):
       pass

class CSVTimeSeriesFile() :

    def __init__(self, name):
        self.name = name

        if not type(name) == str:
            raise ExamException('non e una stringa')


    def get_data(self):
        values = [] #coppie di valori
        values1 = []
        csv_rows = []  #divisione per riga
        csv_rows1 = []
        elements = [] #linee splittate
        times = [] #solo tempi
        times1 = []
        temp1 = []
        temperatures1 = []  #solo temperature
        temperatures = []
        garbage = []
        valuesf = []
        try:
            my_file = open(self.name, 'r')
        except ExamException as e:
            print('Errore nella lettura del file: "{}"'.format(e))
            return None

        lines = my_file.readlines()


        for line in lines:
            elements = line.split(',')
            chrono  = elements[0]
            temp = elements[1]
            times1.append(chrono)
            temp1.append(temp)
        
        for element in temp1:
            temperatures1.append(element.strip())
        
        
        for element in times1:
            if  isinstance(element, int):           
                times.append(element)
            else :
                try:
                    int(element)
                    times.append(element)
                except:
                    garbage.append(element)
                #print(type(element))

        #print(times)


        for element in temperatures1:
            if  isinstance(element, int) or isinstance(element, float):
                float(element)           
                temperatures.append(element)
            else :
                try:
                    float(element)
                    temperatures.append(element)
                except:
                    garbage.append(element)
                    #print(type(element))


        values1 = list(zip(times, temperatures))


        for item in values1:
            values.extend(item)

        
        
        valuesg = [float(item) for item in values]

        for x in range(len(valuesg)):
            for k in range(len(valuesg)):
                if k % 2 == 0:
                    valuesg[k] = int(valuesg[k])
                else:
                    pass



        n = 2

        valuesf = [valuesg[i:i + n] for i in range(0, len(values), n)]

        
        duplicates = any(times.count(element) > 1 for element in times)
        if duplicates == True :
            raise ExamException('Ci sono duplicati')
        else :
            pass

        if not sorted(times) == times:
            raise ExamException("Non Ordinato")

        #print('tempi:', times)
        #print('temperature:', temperatures)   

        my_file.close()               
        return valuesf


time_series_file = CSVTimeSeriesFile(name = 'data.csv')
time_series = time_series_file.get_data()
print('Dati:', time_series)



def daily_stats(time_series):
    gng = []
    for x in time_series:
        x[0] = int(x[0]) - (int(x[0]) % 86400)
        gng.append(x)
    #print('AAAAA.',gng)

    all_values = [list[0] for list in gng]
    #print('AAAAA:', all_values)
    unique_values = set(all_values)
    ordered_values = sorted(unique_values)
    #print('AAAAA:', ordered_values)


    group_list = []
    for value in ordered_values:
        this_group = []
        for list in time_series:
            if list[0] == value:
                this_group.append(list[1])
        group_list.append(this_group)


    avg = []
    daytotal = []
    daymin = []
    daymax = []
    floats = []

    #print(group_list)

    for i in range(len(group_list)):
        for j in range(len(group_list[i])):

            daymint = min(group_list[i])
            daymaxt = max(group_list[i])
            avg = sum((group_list[i])) / (len(group_list[i]))

        
        daymin.append(daymint)
        daymax.append(daymaxt)
        daytotal.append(avg)

    babylon = []
    arr1 = zip(daymin, daymax, daytotal)
    for item in arr1:
            babylon.extend(item)
    
    n = 3
    jah = []
    jah = [babylon[i:i + n] for i in range(0, len(babylon), n)]

    return jah


efe = daily_stats(time_series)

print('\n\n\nmin max media:',efe)