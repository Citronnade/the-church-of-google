from google import search
import re
import urllib
#import nameapp

if __name__ == "__main__":
    query = raw_input(">>>>")
    s = search(query, stop=10)
    queryType = re.match(r'^((Who)|(When))', query).group(1)
    thing = re.search(r'((\s[A-Z]\w+)+)\??$', query).group(1).strip() #replace this with name finder code

    if queryType == 'Who':
        subject = give_text(query)[0]
        
    
    
