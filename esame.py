#Lorenzo Di Bernardo esame di Laboratorio di Programmazione 09/02/21

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

        ##/QUESTO FILTREREBBE LE RIGHE ED ELIMINEREBBE IL PROBLEMA DELLE LINEE INCOMPLETE MA SE LE TEMPERATURE POSSONO ESESERE DI QUALSIASI LUNGHEZZA SALTA TUTTO, SE POI LI CONTROLLO UNA VOLTA SEPARATI NON SO COME RIACCOPPIARLI GIUSTI
        

        ##/lines = list(filter(lambda x : len(x) == 17 , lines1))
        

        for line in lines:                      #DIVIDE I DATI PER IL CONTROLLO
            elements = line.split(',')           
            chrono  = elements[0]
            temp = elements[1]
            times1.append(chrono)
            temp1.append(temp)
        
        for element in temp1:
            temperatures1.append(element.strip()) #TOGLIE LA N ALLA FINE DI OGNI RIGA
        
        
        for element in times1:                    #CONTROLLO E CONVERSIONE EPOCH
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
            else :                                          #CONTROLLO E CONVERSIONE TEMPERATURE
                try:
                    float(element)
                    temperatures.append(element)
                except:
                    garbage.append(element)
                    #print(type(element))

        #print('\n\n\nGarbage:', garbage)


        values1 = list(zip(times, temperatures))            #RIUNISCE I DATI FILTRATI


        for item in values1:
            values.extend(item)                             #CREA LISTA CON I DATI

        
        
        valuesg = [float(item) for item in values]          #CONVERTE IN FLOAT PER OPERAZIONI

        for x in range(len(valuesg)):                       #CONVERTE  NUOVAMENTE LE EPOCH IN INT
            for k in range(len(valuesg)):
                if k % 2 == 0:
                    valuesg[k] = int(valuesg[k])
                else:
                    pass
                                              

        valuesf = [valuesg[i:i + 2] for i in range(0, len(values), 2)]  #SUDDIVIDE IN ARRAY DI ARRAY

        
        duplicates = any(times.count(element) > 1 for element in times)
        if duplicates == True :
            raise ExamException('Ci sono duplicati')          #CONTROLLO PER DUPLICATI
        else :                                      
            pass

        if not sorted(times) == times:                        #CONTROLLO ORDINE CRONOLOGICO
            raise ExamException("Non Ordinato")

        #print('tempi:', times)
        #print('temperature:', temperatures)   

        my_file.close()               
        return valuesf


time_series_file = CSVTimeSeriesFile(name = 'name')
time_series = time_series_file.get_data()
#print('Dati:', time_series)



def daily_stats(time_series):
    gng = []
    for x in time_series:
        x[0] = int(x[0]) - (int(x[0]) % 86400)     #CREA LISTA CON TEMPERATURE E EPOCH UGUALI PER STESSO GIORNO  
        gng.append(x)                                     #TENENDO CONTO DELLA MEZZANOTTE
    #print('AAAAA.',gng)

    all_values = [list[0] for list in gng]                #INDIVIDUA I SINGOLI GIORNI DIVERSI
    #print('AAAAA:', all_values)                          
    unique_values = set(all_values)
    ordered_values = sorted(unique_values)
    #print('AAAAA:', ordered_values)


    group_list = []
    for value in ordered_values:                                                                                         
        this_group = []                                 #RAGGRUPPA TEMPERATURE PER LO
        for list in time_series:                        #STESSO GIORNO
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
        for j in range(len(group_list[i])):                        #OPERAZIONI SULLE TEMPERATURE DELLO 
            daymint = min(group_list[i])                           #STESSO GIORNO
            daymaxt = max(group_list[i])
            avg = sum((group_list[i])) / (len(group_list[i]))

        
        daymin.append(daymint)
        daymax.append(daymaxt)
        daytotal.append(avg)

    babylon = []
    arr1 = zip(daymin, daymax, daytotal)                           #RIUNISCE I DATI IN LISTA
    for item in arr1:
            babylon.extend(item)
    
    n = 3
    jah = []
    jah = [babylon[i:i + n] for i in range(0, len(babylon), n)]     #SUDDIVIDE IN ARRAY DI ARRAY 

    return jah


rastafari = daily_stats(time_series)

#print('\n\n\nmin max media:',rastafari)
