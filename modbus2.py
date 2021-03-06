##CECI EST LE CODE POUR ACCÉDER AU DONNÉES DU CAPTEUR AMBIANCE V2 AVEC LE PROTOCOLE MODBUS TCP/IP

##AUTHOR Vincent SIRET##
##LAST UPDATE 28/01/2021##
                                                                        #############################################################################################################################
import sys                                                              ## IMPORTATION DU MODULE SYS.                                                                                              ##                                         
import os                                                               ## IMPORTATION DU MODULE OS.                                                                                               ##
import requests                                                         ## IMPORTATION DU MODULE REQUESTS.                                                                                         ##                                                                   
from easymodbus.modbusClient import ModbusClient                        ## IMPORTATION DE MODULE "easymodbus" EN TANT QUE "ModbusClient".                                                          ##  
modbusclient = ModbusClient('192.168.0.118', 502)                       ## DEFINITION DE LA VARIABLE "modbusclient" QUI EST = À l'IP DE NOTRE CONCENTRATEUR LoRa ET DU PORT PAR DÉFAUT QUI EST 502.##
reponse = None                                                          ## DEFINITION DE LA VARIABLE REPONSE SUR NONE. (ELLE N'A PAS DE VALEUR)                                                    ##  
                                                                        #############################################################################################################################

try:                                                                    #######################################################################
    reponse = requests.get("http://192.168.0.118/")                     ## NOUS TENTONS DE NOUS CONNECTER A L'ADRESSE DE NOTRE CONCENTRATEUR ##
except:                                                                 ## SI IL N'Y ARRIVE PAS IL AFFICHE "CONEXION ECHOUE" ET IL ARRETE LE ##
    print("CONNEXION ECHOUE")                                           ## PROGRAMME AVEC (sys.exit)                                         ##
    sys.exit                                                            ##                                                                   ##
    os.system("PAUSE")                                                  #######################################################################
    
if ( reponse is not None ):                                             ###############################################################################################################    
    modbusclient.connect()                                              ## SI IL ARRIVE A SE CONNECTER AU CONCENTRATEUR IL SE CONNECTE ALORS AU MODBUS ET AFFICHE "CONNEXION REUSSI".##
    print ("CONNEXION REUSSI")                                          ###############################################################################################################

##SYSTEME AMBIANCE V2##                                                 ##############################################################################################################################################################################################################################################    
    presence_ambv2 = modbusclient.read_holdingregisters(13,1)[0]        ## ICI NOUS DEMANDONS AVEC LA VARIABLE "presence_ambv2" LES DONNÉES DE L'ADRESSE 13 SUR 1 OCTET GRACE A "modbusclient.read_holdingregisters(13,1)"ET NOUS METTONS A LA FIN [0]POUR NE PAS L'AVOIR ENTRE CROCHET QUAND NOUS ALLONS LE PRINT  ##
    print("Capteur présence ambiance V2", presence_ambv2,"secondes")    ## ICI NOUS PRINTONS DONC NOTRE VARIABLE "presence_ambv2" POUR QUE LE SCRIPT AFFICHE NOS DONNÉES.                                                                                                                                           ##   
    temperature_ambv2 = modbusclient.read_holdingregisters(15,1)[0]/100 ## ICI NOUS DEMANDONS AVEC LA VARIABLE "temperature_ambv2" LES DONNÉES DE L'ADRESSE 15 SUR 1 OCTET GRACE A "modbusclient.read_holdingregisters(15,1)"ET NOUS METTONS A LA FIN [0]/100 POUR AVOIR UN FACTEUR DE 0,01                         ##
    print("Capteur température ambiance V2", temperature_ambv2, "°C")   ## ICI NOUS PRINTONS DONC NOTRE VARIABLE "temperature_ambv2" POUR QUE LE SCRIPT AFFICHE NOS DONNÉES.                                                                                                                                        ##   
    co2_ambv2 = modbusclient.read_holdingregisters(17,1)[0]             ## ICI NOUS DEMANDONS AVEC LA VARIABLE "co2_ambv2" LES DONNÉES DE L'ADRESSE 17 SUR 1 OCTET GRACE A "modbusclient.read_holdingregisters(17,1)"ET NOUS METTONS A LA FIN [0]POUR NE PAS L'AVOIR ENTRE CROCHET QUAND NOUS ALLONS LE PRINT       ##   
    print("Capteur Co2 ambiance V2",co2_ambv2,"PPM")                    ## ICI NOUS PRINTONS DONC NOTRE VARIABLE "co2_ambv2" POUR QUE LE SCRIPT AFFICHE NOS DONNÉES.                                                                                                                                                ##
    humidite_ambv2 = modbusclient.read_holdingregisters(19,1)[0]/100    ## ICI NOUS DEMANDONS AVEC LA VARIABLE "humidite_ambv2" LES DONNÉES DE L'ADRESSE 19 SUR 1 OCTET GRACE A "modbusclient.read_holdingregisters(19,1)"ET NOUS METTONS A LA FIN [0]/100 POUR AVOIR UN FACTEUR DE 0,01                            ##       
    print("Capteur humidité ambiance V2", humidite_ambv2,"%")           ## ICI NOUS PRINTONS DONC NOTRE VARIABLE "humidite_ambv2" POUR QUE LE SCRIPT AFFICHE NOS DONNÉES.                                                                                                                                           ##   
    luminosite_ambv2 = modbusclient.read_holdingregisters(21,1)[0]      ## ICI NOUS DEMANDONS AVEC LA VARIABLE "luminosite_ambv2" LES DONNÉES DE L'ADRESSE 21 SUR 1 OCTET GRACE A "modbusclient.read_holdingregisters(21,1)"ET NOUS METTONS A LA FIN [0]POUR NE PAS L'AVOIR ENTRE CROCHET QUAND NOUS ALLONS LE PRINT##   
    print("Capteur luminosité ambiance V2", luminosite_ambv2,"lux")     ## ICI NOUS PRINTONS DONC NOTRE VARIABLE "luminosite_ambv2" POUR QUE LE SCRIPT AFFICHE NOS DONNÉES.                                                                                                                                         ##   
                                                                        ##############################################################################################################################################################################################################################################
    
##FIN##                                                                 #########################################################################################################################
    modbusclient.close()                                                ## ICI NOUS DÉCLARONS LA FIN DE NOTRE PROGRAMME AVEC "modbusclient.close()" POUR NOUS DECONNECTER DES ADRESSES MODBUS. ##
    os.system("PAUSE")                                                  ## NOUS FAISONS AUSSI UN "os.system("PAUSE")" POUR QUE LE SCRIPT NE SE FERME PAS AUTOMATIQUEMENT A LA FIN DU PROGRAMME.## 
                                                                        #########################################################################################################################
