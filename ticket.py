import urllib.request
import json


def getdata(urlstring, urlstring1):
    respond = urllib.request.urlopen(urlstring)
    content = respond.read().decode()
    data = json.loads(content)
    respond1 = urllib.request.urlopen(urlstring1)
    content1 = respond1.read().decode()
    data1 = json.loads(content1)
    fData = []
    for disc in data:
        fdata = []
        loca = disc["the_geom"]
        locaxy = loca["coordinates"]
        fdata.append(float(locaxy[1]))
        fdata.append(float(locaxy[0]))
        fdata.append(disc["district"] + " " + disc["address"])
        fData.append(fdata)
        rapefor2008 = 0
        rapefor2009 = 0
        rapefor2010 = 0
        rapefor2011 = 0
        rapefor2012 = 0
        rapefor2013 = 0
        rapefor2014 = 0
        rapefor2015 = 0
        rapefor2016 = 0
        rapefor2017 = 0
        rapefor2018 = 0
    rape = []
    assault = []
    for x in data1:
        if x['type'] == 'Rape' and x['year'] == '2008':
            rapefor2008 += 1
        elif x['type'] == 'Rape' and x['year'] == '2009':
            rapefor2009 += 1
        elif x['type'] == 'Rape' and x['year'] == '2010':
            rapefor2010 += 1
        elif x['type'] == 'Rape' and x['year'] == '2011':
            rapefor2011 += 1
        elif x['type'] == 'Rape' and x['year'] == '2012':
            rapefor2012 += 1
        elif x['type'] == 'Rape' and x['year'] == '2013':
            rapefor2013 += 1
        elif x['type'] == 'Rape' and x['year'] == '2014':
            rapefor2014 += 1
        elif x['type'] == 'Rape' and x['year'] == '2015':
            rapefor2015 += 1
        elif x['type'] == 'Rape' and x['year'] == '2016':
            rapefor2016 += 1
        elif x['type'] == 'Rape' and x['year'] == '2017':
            rapefor2017 += 1
        elif x['type'] == 'Rape' and x['year'] == '2018':
            rapefor2018 += 1
    rape.append(rapefor2008)
    rape.append(rapefor2009)
    rape.append(rapefor2010)
    rape.append(rapefor2011)
    rape.append(rapefor2012)
    rape.append(rapefor2013)
    rape.append(rapefor2014)
    rape.append(rapefor2015)
    rape.append(rapefor2016)
    rape.append(rapefor2017)
    rape.append(rapefor2018)
    Assafor2008 = 0
    Assafor2009 = 0
    Assafor2010 = 0
    Assafor2011 = 0
    Assafor2012 = 0
    Assafor2013 = 0
    Assafor2014 = 0
    Assafor2015 = 0
    Assafor2016 = 0
    Assafor2017 = 0
    Assafor2018 = 0
    for x in data1:
        if x['type'] == 'Assault' and x['year'] == '2008':
            Assafor2008 += 1
        elif x['type'] == 'Assault' and x['year'] == '2009':
            Assafor2009 += 1
        elif x['type'] == 'Assault' and x['year'] == '2010':
            Assafor2010 += 1
        elif x['type'] == 'Assault' and x['year'] == '2011':
            Assafor2011 += 1
        elif x['type'] == 'Assault' and x['year'] == '2012':
            Assafor2012 += 1
        elif x['type'] == 'Assault' and x['year'] == '2013':
            Assafor2013 += 1
        elif x['type'] == 'Assault' and x['year'] == '2014':
            Assafor2014 += 1
        elif x['type'] == 'Assault' and x['year'] == '2015':
            Assafor2015 += 1
        elif x['type'] == 'Assault' and x['year'] == '2016':
            Assafor2016 += 1
        elif x['type'] == 'Assault' and x['year'] == '2017':
            Assafor2017 += 1
        elif x['type'] == 'Assault' and x['year'] == '2018':
            Assafor2018 += 1
    assault.append(Assafor2008)
    assault.append(Assafor2009)
    assault.append(Assafor2010)
    assault.append(Assafor2011)
    assault.append(Assafor2012)
    assault.append(Assafor2013)
    assault.append(Assafor2014)
    assault.append(Assafor2015)
    assault.append(Assafor2016)
    assault.append(Assafor2017)
    assault.append(Assafor2018)
    fData.append(rape)
    fData.append(assault)
    return(json.dumps(fData))