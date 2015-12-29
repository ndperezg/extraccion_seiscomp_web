# Extracci�U+00Fn  de formas de onda de Seiscomp3

Esta rutina permite extraer formas de onda en formato miniSEED desde el servidor de Seiscomp3.
Esto se h�ace utilizando el servicio web FDSN mediante módulos de ObsPy.

## Requisitos:

-Obspy 0.10.2

## Modo de uso básico:

En una terminal escriba el comando

`$./scx YYYYMMddhhmmss tttt`

en este caso YYYY representa el año, MM el mes, dd el día, hh hora (UT), mm minuto y ss segundos. 
El tiempo de la extracción se reresenta como tttt en segundo. Por defecto se extraer�toda 
la informaciónde la agencia CM.

## Modo de uso específico:

`$ ./scx YYYYMMddhhmmss tttt AG STA LOC CHA` 

Es posible especificar la agencia, estacion, codigo de localizacion y canal. El uso de wildcards de
unix es permitido. 


