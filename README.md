# Extraccion  de formas de onda de Seiscomp3

Esta rutina permite extraer formas de onda en formato miniSEED desde el servidor de Seiscomp3.
Esto se hace utilizando el servicio web FDSN mediante modulos de ObsPy.

## Requisitos:

-Obspy 0.10.2

## Modo de uso basico:

En una terminal escriba el comando

`$./scx YYYYMMddhhmmss tttt`

en este caso YYYY representa el anio, MM el mes, dd el dia, hh hora (UT), mm minuto y ss segundos. 
El tiempo de la extraccion se reresenta como tttt en segundo. Por defecto se extrae toda 
la informacion de la agencia CM.

## Modo de uso especifico:

`$ ./scx YYYYMMddhhmmss tttt AG STA LOC CHA` 

Es posible especificar la agencia, estacion, codigo de localizacion y canal. El uso de wildcards de
unix es permitido siempre y cuando se ingrese el argumento entre comillas, ej: '*'. 


