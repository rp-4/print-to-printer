import subprocess
import os
import os.path
import sys

def main():
  
  # get file path from users
    pdf_name = str(input("Enter full path of PDF file: ")).strip()
    
    #check if file exist or not, if not --> then ask again
    while os.path.exists(pdf_name) is False:
        print("File does not exist !!")
        pdf_name = str(input("Enter full path of PDF file: ")).strip()
    
    #get all installed printer on the system
    printers = getAllPrinter()
    i = 1
    for p in printers:
        print(i," ", p)
        i += 1
        
      #select the printer user wants to print from
    printer = printers[int(input("Enter Printer number: "))-1]
            
  #try to print the pdf and if doesnt work then give error
    try:
        
        subprocess.call(['C:\Program Files\SumatraPDF\SumatraPDF.exe', '-print-to', printer,
                        '-print-settings', "portrail,2,1x", pdf_name])

    except BaseException as msg:
        print(msg)

 # fn to get all installed printers and filter our useless printers
def getAllPrinter():

    data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')
    faltu_printers = ['Location','Send To OneNote 2016','OneNote for Windows 10','PDF24 Fax','PDF24','Microsoft XPS Document Writer  0','Microsoft Print to PDF','Microsoft XPS Document Writer','Fax']
    
    printers = []

    for i in data:
        for j in i.split("  "):
            if j  != "":
                printers.append(j.strip())
                break
    
    p = set(printers)
    f = set(faltu_printers)
    print(p - f)
    t = list(p-f)
    return t

if __name__ == "__main__":
    main()
