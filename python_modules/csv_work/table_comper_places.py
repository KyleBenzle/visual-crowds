import pandas as pd
import csv



def compare_place_to_people_in():
    #print("first")
    s = pd.read_csv('python_modules/csv_work/geo_data.csv')
    Geo = s
    city = Geo.iloc[:,3].values
    #print(city)
    comper = pd.read_csv('python_modules/csv_work/table.csv')
    place = comper.iloc[:,0].values
    capicty_max = comper.iloc[:,1].values
    #print(place)
    x = []
    for i in range(4):
        k = 0
        for j in range(len(city)):
            #print(place[i],city[j])
            if place[i] == city[j]:
                k +=1
        x.append(k)
        
    #print(x)
#list append

    #Comperting
    complete = []
    #print(place)
    #print(x)
    #print(capicty_max)
    for f in range(len(x)):
        if x[f]>capicty_max[f]:
            if f==0:
                #print("overflow in Makka")
                #print("the current number im makka is"+str(x[f]))
                complete.append(("Makka",capicty_max[f],x[f]))
            if f==1:
                #print("overflow in Arafa")
                #print("the current number im Arafa is" +str(x[f]))
                complete.append(("Arafa", capicty_max[f], x[f]))
            if f==2:
                #print("overflow in mena")
                #print("the current number im mena is" + str(x[f]))
                complete.append(("mena", capicty_max[f], x[f]))

            if f==3:
                #print("overflow in muzdalifah")
                #print("the current number im muzdalifah is" + str(x[f]))
                complete.append(("muzdalifah", capicty_max[f], x[f]))

    #print(complete)
    return complete


def find_number_in_city(city_name):
    s = pd.read_csv('python_modules/csv_work/geo_data.csv')
    comper = pd.read_csv('python_modules/csv_work/table.csv')
    place = comper.iloc[:,0].values
    capicty_max = comper.iloc[:,1].values
    load_city = s.iloc[:,3].values
    c=0
    for i in range(len(load_city)):
        if city_name == load_city[i]:
            c+=1
    for x in range(len(place)):

        if place[x]==city_name and capicty_max[x]>=c:
            # NO flow
            return [c,int(capicty_max[x])]
    else:
        return None




#f=find_number_in_city("makka")
#print(f)
#x=compare_place_to_people_in(s)
