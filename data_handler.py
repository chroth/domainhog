import urllib2
import tld
import os

def update():
    if not os.path.exists('data'):
        os.makedirs('data')

    tlds_data = file(os.path.join('data', 'tlds.txt'), 'w+')
    response = urllib2.urlopen('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    tlds_data.write(response.read())

def get_tlds():
    tlds = []
    tlds_data = file(os.path.join('data', 'tlds.txt'), 'r')
    while True:
        tld_line = tlds_data.readline()
        if not tld_line:
            break
        else:
            if tld_line[0] != '#' and tld_line.strip():
                tlds.append(tld.Tld(tld_line.strip().lower()))
    return tlds

def has_data():
    return os.path.exists(os.path.join('data', 'tlds.txt'))