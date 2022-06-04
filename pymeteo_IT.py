######################################################
#                  P Y M E T E O                     #
#                       by                           #
#                  Pietro Favale                     #
#                                                    #
# Coded following the GNU GENERAL PUBLIC LICENSE,    #
# anyone can contribute to improve this project.     #
######################################################


import requests
import os
import colorama
import metpy.calc as mpcalc
from metpy.units import units
from colorama import Fore, Back, Style
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'it_IT.utf8')
colorama.init(autoreset=True)

user_api = 'f8a728c560cfe1dd86b93f91149f7622' # <--- INSERISCI QUI LA TUA "USER_API" DA OPENWEATHERMAP.ORG

location = input(Fore.WHITE + Style.BRIGHT +"\n\n\n   Inserisci una località: ")
print (Fore.RESET + Back.RESET +"\n\n")


complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api+"&lang=it&units=metric"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print(Back.RED + Fore.WHITE + Style.BRIGHT + "!!! ATTENZIONE !!!"+Back.RESET+Fore.RESET+Style.RESET_ALL+"\n")
    print(Back.RESET+Fore.RED+Style.BRIGHT+"NON RIESCO A TROVARE"+Fore.WHITE+Style.BRIGHT+" {}".format(location.upper())+Style.BRIGHT+Fore.RED+" - Località inserita inesistente.")

else: 
    
    ##############################################################################################################
    #
    # Converto i gradi radiali (0° - 360°) in direzioni testuali (es. "N" - per nord oppure "SSE" per Sud/Sud-Est)
    #
    ###############################################################################################################
    deg = api_data['wind']['deg']
    convert = ((deg) * units('degree'))
    direzione = mpcalc.angle_to_direction(convert, full=False)

    
    ####### Prendo tutti gli altri dati da "api_data" #########
    temp_city = api_data['main']['temp']
    feels_like = api_data['main']['feels_like']
    temp_max = api_data['main']['temp_max']
    temp_min = api_data['main']['temp_min']
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    pres = api_data['main']['pressure']
    wind_spd = ((api_data['wind']['speed']) *3.6)
    #wind_spd_gust = ((api_data['wind']['gust']) *3.6)
    nuvol = api_data['clouds']['all']
    date_time = datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")
    
    
    print (Back.BLUE + "  Condizioni meteo per - {}  || {}  ".format(location.upper(), date_time)+Back.RESET+"\n\n")
    

    print (Fore.WHITE + "Temperatura attuale:        {:.2f}°C".format(temp_city))
    print (Fore.WHITE + Style.DIM + "Temperatura percepita:      {:.2f}°C".format(feels_like))
    print (Fore.RED + "Temp. MAX:                  {:.2f}°C".format(temp_max))
    print (Fore.LIGHTBLUE_EX + Style.BRIGHT + "Temp. MIN:                  {:.2f}°C".format(temp_min))
    print (Fore.LIGHTCYAN_EX + Style.DIM + "Tempo in atto:              {}".format(weather_desc))
    print (Fore.LIGHTMAGENTA_EX + "Copertura nuvolosa:         {}%".format(nuvol))
    print (Fore.GREEN +"Pressione:                  {}".format(pres)+Fore.GREEN+" hPa")
    print (Fore.LIGHTGREEN_EX + Style.DIM + "Umidità attuale:            {}%".format(hmdt))
    print (Fore.LIGHTYELLOW_EX + "Vento:                      {:.2f}".format(wind_spd) + Fore.LIGHTYELLOW_EX +' Km/h'+ 
            Fore.LIGHTYELLOW_EX + " - {}".format(direzione))
    print (Fore.RESET+"\n\n")
    print (Fore.LIGHTMAGENTA_EX+Style.BRIGHT+ "         - - - FINE DATI - - -\n")
    print (Fore.RESET+"\n")
    #print (Fore.YELLOW +"Vento (raffica):            {:.2f}".format(wind_spd_gust) + Fore.YELLOW + ' Km/h')
