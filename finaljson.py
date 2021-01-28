import requests
import simplejson as json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import time
print ("DÉMARRAGE ... ")
api_user = "?api_key=FndxRe1PIz1QKhjHV7SEP3pPJvmEM5NF&user_id=7e9aa738-ab67-4c79-8b77-5d73d7384b7d"
url = "https://ewattch.cloud/api/V2/structure" + api_user
response = requests.get(url)
data = response.json()
gw = data["gateways"][0]
dataHeader = dict()
nom_des_mois = ["None", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
dataHeader["dates"] = ["now-5h", "now"]
dataHeader["sampling"] = ["live"]
dataHeader[ "structure_uuids"] = ["897b7488-9c70-4e09-93f2-6c933f59e871"]#[data["gateways"][0]["uuid"]]
headers = {'Content-Type' :  'application/json'}
##mng = plt.get_current_fig_manager()
##mng.full_screen_toggle()

fig = plt.figure(1)
plt.subplots_adjust(left=0.1,right=0.9,bottom=0.05,top=0.95,wspace=0.3,hspace=0.3)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
while(True):
    a = requests.post("https://ewattch.cloud/api/V2/datafetch" + api_user, data=None, json=dataHeader, headers=headers)
    fig.clear()
    for i,mesure in enumerate(a.json()):
        ax2 = fig.add_subplot(3,2,i+1)
        ##print("Mesure " + str(i+1) +" :")
        name = mesure ["name"]
        unit = mesure ["unit"]
        minX = np.datetime64(mesure ["series"][0][0])
        maxX = np.datetime64(mesure ["series"][-1][0])
        listValues = list()
        listTimes = list()
        for sample in mesure ["series"]:
            listValues.append(float(sample[1]))
            listTimes.append(np.datetime64(sample[0]))
            [date, heure] = sample[0].split("T")
            [annee, mois, jour] = date.split("-")
            date_str = jour + " "+ nom_des_mois[int(mois)] + " " +  annee
            #print ("Mesure du : " + date_str + " à " + heure + " : " + sample [1] + unit)
        xaxis = np.array(listTimes)
        yaxis = np.array(listValues)
        ax2.set_ylabel(unit)
        ax2.plot(xaxis,yaxis,colors[i], label=name )
        ax2.legend(bbox_to_anchor=(0.5, 1), loc='lower center', borderaxespad=0.)
    plt.ion()
    plt.show()
    plt.pause(180)
    print ("Refresh des données ...")
    plt.clf()
