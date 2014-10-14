from bs4 import BeautifulSoup
import re, urllib, nameapp, google, math, unittest

f = open('progress.txt','w');

def who(s):
    g = google.search(s, num= 1,start = 0, stop = 8)
    #l = BeautifulSoup(google.get_page(g.next()))
    #x = givetext(l.prettify()) 
    
    #soup=[(BeautifulSoup(google.get_page(x)).find_all('p') for x in urls] HOW TO SOUP
    urls = [x for x in g]
    f.write("Step 1 - Collecting URLS:\n")
    for x in urls:
        f.write(x+"\n")
    f.write("\n\n\n\n")
    soup=[(google.get_page(x)) for x in urls]
    alphabetsoup=[nameapp.givetext(x) for x in soup]
    f.write("Step 2 - Collecting all the Names:\n")
    f.write(str(alphabetsoup)+"\n")
    f.write("\n\n\n\n")
    splitted=[]
    for x in alphabetsoup:
        splitted+=x
    """for i in urls:
        html.append(BeautifulSoup(google.get_page(i)))
    allnames = []
    for i in html:
        allnames.append(nameapp.givetext(i))
    splitted = []
    for i in allnames:
        splitted += i.split(",")"""
    namestats = {}
    ##all names
    for i in splitted:
        if i in namestats:
            namestats[i] += 1
        else:
            namestats[i] = 1
    f.write("Step 3 - Making a Dictionary:\n")
    f.write(str(namestats)+"\n")
    f.write("\n\n\n\n")
    final = {};
    for i in namestats:
        if namestats[i] >= 25:
            final[i] = namestats[i]

    f.write("Step 4 - Narrowing Possibilites:\n")
    f.write(str(final)+"\n")
    f.write("\n\n\n\n")
    maxname=final.keys()[0]
    maxvalue=final[maxname]
    for x in final.keys():
        if final[x] > maxvalue:
            maxname=x
            maxvalue=final[x]
    f.write("Step 5 - The Answer:\n")
    f.close()
    return maxname

def when(s):
    g = google.search(s, num = 1, start = 0, stop = 8)
    soup = [(google.get_page(x)) for x in g]
    monthsoup = [findmonths(x) for x in soup]
    monthdict = {}
    for page in monthsoup:
        for month in page:
            if len(month) > 0:
                if month[0] in monthdict:
                    monthdict[month[0]] += len(month)
                else:
                    monthdict[month[0]] = len(month)
    yearsoup = [re.findall('[1-9]{4}',x) for x in soup]
    yeardict = {}
    for page in yearsoup:
        if len(page) > 0:
            for year in page:
                if year in yeardict:
                    yeardict[year] += 1
                else:
                    yeardict[year] = 1
    yeardict.update(monthdict)
    return yeardict
    

        
    





def findmonths(s):
    months = ['January','February','March','April','May','June','July','August',
              'September','October','November','December']
    rawlists = [re.findall(x,s) for x in months]
    return rawlists
    






if __name__ == "__main__":
    query = raw_input(">>>>")
    s = google.search(query, stop=10)
    queryType = re.match(r'^((Who)|(When|Whom))', query).group(1)
    thing = " ".join([x.strip() for x in re.findall(r'(\s[A-Z]\w+)+', query)]) #replace this with name finder code
    if queryType == 'Who':
        subject = who(thing)
        print subject
    if queryType == 'When':
        subject = when(thing)
        print subject
        
    
    
