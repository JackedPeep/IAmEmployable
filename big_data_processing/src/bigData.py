#!/usr/bin/env python  	    	       

#                         _  	    	       
#                        (o)<  DuckieCorp Software License  	    	       
#                   .____//  	    	       
#                    \ <' )   Copyright (c) 2022 Erik Falor  	    	       
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	    	       
#  	    	       
# Permission is granted, to any person who is EITHER an employee OR  	    	       
# customer of DuckieCorp, to deal in the Software without restriction,  	    	       
# including without limitation the rights to use, copy, modify, merge,  	    	       
# publish, distribute, sublicense, and/or sell copies of the Software, and to  	    	       
# permit persons to whom the Software is furnished to do so, subject to the  	    	       
# following conditions:  	    	       
#  	    	       
# The above copyright notice and this permission notice shall be included in  	    	       
# all copies or substantial portions of the Software.  	    	       
#  	    	       
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	    	       
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  	    	       
# FITNESS FOR A PARTICULAR PURPOSE, EDUCATIONAL VALUE AND NONINFRINGEMENT. IN  	    	       
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  	    	       
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  	    	       
# OTHERWISE, ARISING FROM INDIGNATION, INDIGESTION, INDIFFERENCE, INDECENCY,  	    	       
# INDENTATION, INDETERMINATION, INTOXICATION, INDOCTRINATION, INTOLERANCE,  	    	       
# INDULGENCE, INDELICATENESS, INDISCRETION, INEFFECTIVENESS OR IN CONNECTION  	    	       
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  	    	       


import time  	    	       
import sys  	    	       
from Report import Report  	    	       


rpt = Report(year=2021)  	    	       

if __name__ == '__main__':  	    	           	       
    #----Reading commands-----
    if len(sys.argv) <2:
        print("no argument given.")
        exit(1)
    else:
        pass
        
    print("Reading the databases...", file=sys.stderr)
    before = time.time()  	    	       

     	       
    targetFilePath = sys.argv[1] + "/area-titles.csv" 
    oAreaFile = open(targetFilePath)   	       
    #---------Creating the fips dictionary for fast area names----------
    areaFipsDictionary = {"":""}
    for line in oAreaFile:
        
        vLine = line.split("\",\"")
        vLine[0] = vLine[0].replace("\"","")
        vLine[1] = vLine[1].replace("\"\n", "")
        
        areaFipsDictionary[vLine[0]] = vLine[1]
    oAreaFile.close()
  
    oAnnualFile = open(sys.argv[1]+"/2021.annual.singlefile.csv")
    
     	    	       
#---All industries variables---    
    aNumFipsAreas = 0
    
    aAnlWages = 0
    aMaxWageArea = ""
    aMaxAnlWage = 0
    
    aNumEstablishment = 0
    aMaxEstablishmentArea = ""
    aMaxNumEstablishment = 0
    
    aAnlEmpLvl = 0
    aMaxEmpArea = ""
    aMaxNumEmp = 0
#---Software Development Industries variables---
    sNumFipsAreas = 0

    sAnlWages = 0
    sMaxWageArea = ""
    sMaxAnlWage = 0

    sNumEstablishment = 0
    sMaxEstablishmentArea = ""
    sMaxNumEstablishment = 0

    sAnlEmpLvl = 0
    sMaxEmpArea = ""
    sMaxNumEmp = 0

    oAnnualFile.readline() #Get rid of header
    for line in oAnnualFile:
        if line == "":
            oAnnualFile.close()
            break
        else:
            pass
        vLine = line.split(",")
        
        if vLine[0][3:6] != "000" and vLine[0][1] != "C" and vLine[0][1] != "U" and vLine[0][1] != "M":
            if vLine[1] == "\"0\"" and vLine[2] == "\"10\"":
                #Record all industries data
                aNumFipsAreas += 1 #number of areas counter
                #----Wages----
                aAnlWages += int(vLine[10])
                if aMaxAnlWage < int(vLine[10]):
                    aMaxAnlWage = int(vLine[10])
                    aMaxWageArea = vLine[0].replace("\"","")
                #---Employment---
                aAnlEmpLvl += int(vLine[9])
                if aMaxNumEmp < int(vLine[9]):
                    aMaxNumEmp = int(vLine[9])
                    aMaxEmpArea = vLine[0].replace("\"","")
                #---Establishment---    
                aNumEstablishment += int(vLine[8])
                if aMaxNumEstablishment < int(vLine[8]):
                    aMaxNumEstablishment = int(vLine[8])
                    aMaxEstablishmentArea = vLine[0].replace("\"","")
                else:
                    pass
            elif vLine[1] == "\"5\"" and vLine[2] == "\"5112\"":
                #Record all Software Development data
                sNumFipsAreas += 1 #number of software development fips areas
                # ----Wages----
                sAnlWages += int(vLine[10])
                if sMaxAnlWage < int(vLine[10]):
                    sMaxAnlWage = int(vLine[10])
                    sMaxWageArea = vLine[0].replace("\"","")
                # ---Employment---
                sAnlEmpLvl += int(vLine[9])
                if sMaxNumEmp < int(vLine[9]):
                    sMaxNumEmp = int(vLine[9])
                    sMaxEmpArea = vLine[0].replace("\"","")
                # ---Establishment---    
                sNumEstablishment += int(vLine[8])
                if sMaxNumEstablishment < int(vLine[8]):
                    sMaxNumEstablishment = int(vLine[8])
                    sMaxEstablishmentArea = vLine[0].replace("\"","")
                else:
                    pass
            else:
                pass
        
    after = time.time()  	    	       
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	    	
    
    #-----------Report for all industries----------	    	       
    rpt.all.num_areas           =  aNumFipsAreas  	    	       

    rpt.all.total_annual_wages  = aAnlWages  	    	       
    rpt.all.max_annual_wage     = [areaFipsDictionary[aMaxWageArea], aMaxAnlWage]  	    	       

    rpt.all.total_estab         = aNumEstablishment  	    	       
    rpt.all.max_estab           = [areaFipsDictionary[aMaxEstablishmentArea], aMaxNumEstablishment]  	    	       

    rpt.all.total_empl          = aAnlEmpLvl  	    	       
    rpt.all.max_empl            = [areaFipsDictionary[aMaxEmpArea], aMaxNumEmp]  	    	       


    #-----------Report for software industries---------  	    	       
    rpt.soft.num_areas          = sNumFipsAreas  	    	       

    rpt.soft.total_annual_wages = sAnlWages  	    	       
    rpt.soft.max_annual_wage    = [areaFipsDictionary[sMaxWageArea], sMaxAnlWage]  	    	       

    rpt.soft.total_estab        = sNumEstablishment   	    	       
    rpt.soft.max_estab          = [areaFipsDictionary[sMaxEstablishmentArea], sMaxNumEstablishment] 	    	       

    rpt.soft.total_empl         = sAnlEmpLvl  	    	       
    rpt.soft.max_empl           = [areaFipsDictionary[sMaxEmpArea], sMaxNumEmp]  	    	       


    # Print the completed report  	    	       
    print(rpt)  	    	       

     	    	       
