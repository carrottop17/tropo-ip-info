import dns.resolver
import sys
import csv

myResolver = dns.resolver.Resolver()
myAnswers = myResolver.query("_netblocks.tropo.com", "TXT")
tropoString = 'tropo,'
writer = csv.writer(
    sys.stdout, delimiter=' ', 
    quotechar='', quoting=csv.QUOTE_NONE)

for rdata in myAnswers:
    writer.writerow([tropoString + ''.join(str(rdata).strip("\""))])
    
    