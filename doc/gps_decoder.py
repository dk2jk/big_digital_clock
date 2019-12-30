#gps-decoder

f= open(  "nmea.txt")
'''
$GPRMC,222615.000,A,5128.9775,N,00819.3163,E,4.10,,060619,,,A*7D
'''

zeilen= f.readlines()

found= False
for i in range ( 0, len(zeilen)):
    if zeilen[i].find("$GPRMC") ==0:
        found=True
        break;

if not found:
    print( "not found")
else:
    gps_str= zeilen[i]
    print("gefunden:",gps_str)
    #gefunden: $GPRMC,222615.000,A,5128.9775,N,00819.3163,E,4.10,,060619,,,A*7D

data= gps_str.split(',')  # daten sind durch ',' getrennt
print("Daten als Liste:")
print(data)
#['$GPRMC', '222615.000', 'A', '5128.9775', 'N', '00819.3163', 'E', '4.10', '', '060619', '', '', 'A*7D\n']

if data[2]=='A': print (data[2] ,"   = Daten ok")

zeit= data[1]
# 222615.000
hms = zeit[0:2]+':'+zeit[2:4]+':'+zeit[4:6]
#'22:26:15'
print ("Zeit =", hms, "Uhr UTC")
#Zeit = 22:26:15 Uhr UTC

speed=float(data[7]) # string nach float
#4.1

k2kmh=1.852
kmh= speed*k2kmh
#7.5931999999999995
kmh_string = format(kmh, '.1f') # eine nachkommastelle
print ("speed=", speed, "Knoten", kmh_string, "km/h")
#speed= 4.1 Knoten 7.6 km/h
