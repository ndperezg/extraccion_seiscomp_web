#!/usr/bin/env python
"""
Script que permite realizar extracciones del servido de seiscomp mediante el servicio web fdsn
"""
from obspy import UTCDateTime
from obspy.fdsn.client import Client
import sys

ip_fdsn = "http://10.100.100.232"
port_fdsn = "8091"
Format = "mseed"

def request(client, t1, t2, AG="CM", STA="*", LOC="?0", CHA="*"):
	st = client.get_waveforms(AG, STA, LOC, CHA, t1, t2)
	return st
def archive_name(lista):
	name = "_"
	for l in lista:
		name += "_"+l
	return name

if len(sys.argv) < 2:
	print "No hay parametros de entrada"
	sys.exit()

year, MM, dd, hh, mm, ss = int(sys.argv[1][0:4]), int(sys.argv[1][4:6]), int(sys.argv[1][6:8]), int(sys.argv[1][8:10]), int(sys.argv[1][10:12]), int(sys.argv[1][12:14])

t = UTCDateTime(year, MM, dd, hh, mm)
t_ = float(sys.argv[2])

if len(sys.argv)>2:
	name = str(t)+archive_name(sys.argv[3:])+"."+Format
else:
	name = str(t)+"."+Format 

#print t, t_

client_sc = Client(ip_fdsn+":"+port_fdsn)
print client_sc

if len(sys.argv) == 2:
	st = request(client = client_sc, t1 = t, t2= t + t_)
	print st
if len(sys.argv) == 4:
	st = request(client = client_sc, t1 = t, t2= t + t_, AG=sys.argv[3])
        print st
elif len(sys.argv) == 5:
	st = request(client = client_sc, t1 = t, t2= t + t_, AG=sys.argv[3], STA=sys.argv[4])
	print st
elif len(sys.argv) == 6:
	st = request(client = client_sc, t1 = t, t2= t + t_, AG=sys.argv[3], STA=sys.argv[4], LOC=sys.argv[5])
	print st
elif len(sys.argv) == 7:
	st = request(client = client_sc, t1 = t, t2= t + t_, AG=sys.argv[3], STA=sys.argv[4],LOC=sys.argv[5],CHA=sys.argv[6])
	print st

st.write(name, format=Format)
	
	
