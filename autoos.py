import sys
import time
import nmap


yp_scan = nmap.PortScanner() 
#Making a nmap scanner object

print("Scanning ...\n")

yp_scanner = yp_scan.scan(sys.argv[1],'80',arguments= '-O')
#Passing on the 1 argument give in CLI as IP for the nmap scanner object
#Along with port number and -O flag for OS fingerprinting 


# The result stored in yp_scanner is a complex dict 
# So below assignments are to gather required information from the scanner dict made
os_method = yp_scanner["nmap"]["scaninfo"]["tcp"]["method"]
os_service = yp_scanner["nmap"]["scaninfo"]["tcp"]["services"]
system_up = yp_scanner["scan"][sys.argv[1]]["status"]["state"]
os_version = yp_scanner["scan"][sys.argv[1]]["osmatch"][0]["name"]
os_accuracy = yp_scanner["scan"][sys.argv[1]]["osmatch"][0]["accuracy"]
os_accu = "This system is running {} os with {}% certainity".format(os_version,os_accuracy)


# After the required fields are collected
# We need to write the result to a text file with name of IP on which this script was run
with open("{}.txt".format(sys.argv[1]),'w') as f:
    f.write("System is "+system_up+" found using "+os_method+" method. "+"\n"+
            os_accu+"\n",)
    f.write("\nReport generated: "+time.strftime("%Y-%m-%d_%H:%M:%S GMT"))
    
print("\nFinished ...")
    