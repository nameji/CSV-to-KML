import csv
import string
import alphabetDict

def main():
    inputCSV = open('NG_OP.csv','rb')
    csvFile = csv.reader(inputCSV)
    next(csvFile,None)
    
    
    def kmlWriter(CSV):
        kml = open("test.kml","w")
        kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n\t<Document>\n\t<name>Excel</name>\n')
        letters = alphabetDict.alphabet()
    
        placemark = raw_input("Which column letter do you want as your name?: ").lower()
        place = letters[placemark]
    
        latCol = raw_input("Which column letter is your Latitude?: ").lower()
        lat = letters[latCol]
    
        lonCol = raw_input("Which column letter is your Longitude?: ").lower()
        lon = letters[lonCol]

        #desc_q = raw_input("Does your CVS have a description column? Type Y or N ").lower()
        
        description = raw_input("Which column letter has your file's descriptions?: ").lower()
        desc = letters[description]
        
        #if desc_q == 'Y':
            #description = raw_input("Which column letter has your file's descriptions?: ").lower()
            #desc = letters[description]
        #else:
            #desc = 
        
        for row in CSV:
            kml.write('<Placemark>\n\t<name>'+row[place]+'</name>\n\t<description>'+row[desc]+'</description>\n\t\t<Point>\n\t\t\t<coordinates>'+row[lon]+','+row[lat]+',0</coordinates>\n\t\t</Point>\n</Placemark>\n')
        kml.write('</Document></kml>')
        kml.close()
    kmlWriter(csvFile)

main()