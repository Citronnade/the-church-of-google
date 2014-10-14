from bs4 import BeautifulSoup
import re, urllib, nameapp, google, math, unittest



def who(s):
    g = google.search(s, num= 1,start = 0, stop = 8)
    #l = BeautifulSoup(google.get_page(g.next()))
    #x = givetext(l.prettify()) 
    f=[]
    #soup=[(BeautifulSoup(google.get_page(x)).find_all('p') for x in urls] HOW TO SOUP
    urls = [x for x in g]
    f.append("Step 1 - Collecting URLS:")
    for x in urls:
        f.append(x)
    f.append("")
    f.append("")
    soup=[(google.get_page(x)) for x in urls]
    alphabetsoup=[nameapp.givetext(x) for x in soup]
    f.append("Step 2 - Collecting all the Names:")
    f.append(str(alphabetsoup))
    f.append("")
    f.append("")
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
    f.append("Step 3 - Making a Dictionary:")
    f.append(str(namestats))
    f.append("")
    f.append("")
    final = {};
    for i in namestats:
        if namestats[i] >= 25:
            final[i] = namestats[i]

    f.append("Step 4 - Narrowing Possibilites:")
    f.append(str(final))
    f.append("")
    f.append("")
    maxname=final.keys()[0]
    if (maxname == s):
        maxname=final.keys()[1]
    maxvalue=final[maxname]
    for x in final.keys():
        if final[x] > maxvalue and x != s:
            maxname=x
            maxvalue=final[x]
    f.append("Step 5 - The Answer:")
    f.append(maxname)
    return f

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
        
    
    
