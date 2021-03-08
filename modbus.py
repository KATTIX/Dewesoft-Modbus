##CECI EST LE CODE POUR ACCÉDER AU DONNÉES DES CAPTEURS AVEC LE PROTOCOLE MODBUS TCP/IP 

import sys##IMPORTATION DU MODULE SYS.
import os##IMPORTATION DU MODULE OS.
import requests##IMPORTATION DU MODULE REQUESTS.
from easymodbus.modbusClient import ModbusClient##IMPORTATION DE MODULE "easymodbus" en tant que "ModbusClient".
modbusclient = ModbusClient('192.168.0.118', 502)##DEFINITION DE LA VARIABLE "modbusclient" QUI EST = À l'IP DE NOTRE CONCENTRATEUR LoRa ET DU PORT PAR DÉFAUT QUI EST 502.
reponse = None ##DEFINITION DE LA VARIABLE REPONSE SUR NONE. (ELLE N'A PAS DE VALEUR) 

try:                                                                 ########################################################################
    reponse = requests.get("http://mttech_ewattch/")                 ##NOUS TENTONS DE NOUS CONNECTER A L'ADRESSE DE NOTRE CONCENTRATEUR   ##
except:                                                              ##SI IL N'Y ARRIVE PAS IL AFFICHE "CONEXION ECHOUE" ET IL ARRETE LE   ##
    print("CONNEXION ECHOUE")                                        ##PROGRAMME.                                                          ##
    sys.exit                                                         ##                                                                    ##
    os.system("PAUSE")                                               ########################################################################
    
if ( reponse is not None ):                                             ############################################################################################################    
    modbusclient.connect()                                              #SI IL ARRIVE A SE CONNECTER AU CONCENTRATEUR IL SE CONNECTE ALORS AU MODBUS ET AFFICHE "CONNEXION REUSSI";#
    print ("CONNEXION REUSSI")                                          ############################################################################################################
##SYSTEME AMBIANCE V2##                                                  
    presence_ambv2 = modbusclient.read_holdingregisters(13,1)[0]        ## ICI NOUS DEMANDONS AVEC LA VARIABLE "presence_ambv2" LES DONNÉES DE L'ADRESSE 13 SUR 1 OCTET GRACE A "modbusclient.read_holdingregisters(13,1)"ET NOU METTONS A LA FIN [0]POUR NE PAS L'AVOIR ENTRE CROCHET QUAND NOUS ALLONS LE PRINT
    print("Capteur présence ambiance V2", presence_ambv2,"secondes")    ## ICI NOUS PRINTONS DONC NOTRE VARIABLE "presence_ambv2" POUR QUE LE SCRIPT AFFICHER NOS DONNÉES.
    temperature_ambv2 = modbusclient.read_holdingregisters(15,1)[0]/100 ## ICI NOUS AVONS RAJOUTÉ [0]/100 POUR AVOIR UN FACTEUR DE 0,01
    print("Capteur température ambiance V2", temperature_ambv2, "°C")
    co2_ambv2 = modbusclient.read_holdingregisters(17,1)[0]
    print("Capteur Co2 ambiance V2",co2_ambv2,"PPM")
    humidite_ambv2 = modbusclient.read_holdingregisters(19,1)[0]/100    ## ICI AUSSI NOUS AVONS RAJOUT2 [0]/100 POUR AVOIR UN FACTEUR DE 0,01
    print("Capteur humidité ambiance V2", humidite_ambv2,"%")
    luminosite_ambv2 = modbusclient.read_holdingregisters(21,1)[0]
    print("Capteur lumonosité ambiance V2", luminosite_ambv2,"lux")

##SYSTEME AMBIANCE N°1##
    presence_amb1 = modbusclient.read_holdingregisters(23,1)[0]
    print("Capteur présence ambiance (1)", presence_amb1,"secondes")
    temperature_amb1 = modbusclient.read_holdingregisters(25,1)[0]/100
    print("Capteur température ambiance (1)", temperature_amb1,"°C")
    humidite_amb1 = modbusclient.read_holdingregisters(27,1)[0]/100
    print ("Capteur humidité ambiance (1)", humidite_amb1,"%")
    luminosite_amb1 = modbusclient.read_holdingregisters(29,1)[0]
    print("Capteur luminosité ambiance (1)", luminosite_amb1,"Lux")

##SYSTEME AMBIANCE N°2##
    presence_amb2 = modbusclient.read_holdingregisters(31,1)[0]
    print("Capteur présence ambiance (2)", presence_amb2,"secondes")
    temperature_amb2 = modbusclient.read_holdingregisters(33,1)[0]/100
    print("Capteur température ambiance (2)", temperature_amb2,"°C")
    humidite_amb2 = modbusclient.read_holdingregisters(35,1)[0]/100
    print("Capteur humidité ambiance (2)", humidite_amb2,"%")
    luminosite_amb2 = modbusclient.read_holdingregisters(37,1)[0]
    print("Capteur luminosité ambiance (2)", luminosite_amb2,"Lux")

##SYSTEME TYNESS N°1##
    temperature_tyness1 = modbusclient.read_holdingregisters(39,1)[0]/100
    print("Capteur températutre tyness (1)", temperature_tyness1,"°C")

##FIN##
    modbusclient.close()                                                #########################################################################################################################                                               ## ICI NOUS DÉCLARONS LA FIN DE NOTRE PROGRAMME AVEC "modbusclient.close()" POUR NOUS DECONNECTER DES ADRESSES MODBUS. ##
    os.system("PAUSE")                                                  ## NOUS FAISONS AUSSI UN "os.system("PAUSE")" POUR QUE LE SCRIPT NE SE FERME PAS AUTOMATIQUEMENT A LA FIN DU PROGRAMME.## 
                                                                        #########################################################################################################################
