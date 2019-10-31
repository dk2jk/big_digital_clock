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

data= gps_str.split(',')  # daten sind durch ',' getrennt
print("Daten als Liste:")
print(data)

if data[2]=='A': print (data[2] ,"   = Daten ok")

zeit= data[1]
# 222615.000
hms = zeit[0:2]+':'+zeit[2:4]+':'+zeit[4:6]
print ("Zeit =", hms, "Uhr UTC")

speed=float(data[7])

k2kmh=1.852
kmh= speed*k2kmh
kmh_string = format(kmh, '.1f') 
print ("speed=", speed, "Knoten", kmh_string, "km/h")
