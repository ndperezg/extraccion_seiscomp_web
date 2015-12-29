# Extracci贸 de formas de onda de Seiscomp3

Esta rutina permite extraer formas de onda en formato miniSEED desde el servidor de Seiscomp3.
Esto se h耡ce utilizando el servicio web FDSN mediante m贸dulos de ObsPy.

1. Requisitos:

-Obspy 0.10.2

2. Modo de uso b谩sico:

En una terminal escriba el comando

$./scx YYYYMMddhhmmss tttt

en este caso YYYY representa el a帽o, MM el mes, dd el d铆a, hh hora (UT), mm minuto y ss segundos. 
El tiempo de la extracci贸n se reresenta como tttt en segundo. Por defecto se extraer胻oda 
la informaci贸nde la agencia CM.

2. Modo de uso espec铆fico:

$ ./scx YYYYMMddhhmmss tttt AG STA LOC CHA 

Es posible especificar la agencia, estacion, codigo de localizacion y canal. El uso de wildcards de
unix es permitido. 


