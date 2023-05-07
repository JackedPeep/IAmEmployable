# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

#### Instructions
I will be summarizing a data set from the bureau of labor's 2021 data set.  
#### The solution
I will use the methods I learned in last lesson to organize the data into sensible pieces.
I will then create a more effective program that can handle the whole file.
#### Known Methods
Grep, sort, cat, tac.
#### Challenges
I will run into the challenge of not knowing what functions to run in order to decrease the workload on the computer.
## Phase 1: System Analysis *(10%)*

#### Inputs & Outputs
##### Function Name: IndustryDataSet(Input: FIPS files ) 
* Output: Number of FIPS areas, Total/Max; annual wages, establishment wages, employee wages 
* Organises the Data by Total/Max wages in categories of areas, establishment, and employee.
##### Function Name: Report(Input: IndustryDataSet())
* Output: Number of FIPS areas, Total/Max; annual wages, establishment wages, employee wages  in a correctly formatted list.
* This returns data organized by *IndustryDataSet()* and returns it as a formatted report.

## Phase 2: Design *(30%)*

### Pseudo Code

   ` if to few argumets:
        print error
    open area-titles file using file path from user and target file hardcode
    REMOVE HEADER
    for line in file
        erase all spaces
        lineArray = split line at coma
        add to dictionary
    open 2020.annual file using file path from user and target file hardcode
    REMOVE HEADER
    for line in file
        erase all spaces
        lineArray = split line by comas
        if fipsValue[2:] is not "000":
            record values:
            number of areas
            total anual wages
            max anual wages
            total establishments
            max establishments
            total employees
            max employees
        if inustry == software:
            record values:
            number of areas
            total anual wages
            max anual wages
            total establishments
            max establishments
            total employees
            max employees
    Report values `
* DELETE ALL TODO MESSAGES 

    

## Phase 3: Implementation *(15%)*

###Things that went wrong!
1) I couldn't figure out why my dictionary wasn't assigning the proper code.
2) I didn't inderstand why my software iteration wasn't recording any values. 
###Things I fixed!
1) I found out that the reason my dictionary read out was throwing errors was because there was nothing assighned to an `""` value and so I included {"",0}
2) I found that it was reading the `""`s surounding the string as strings so I included `\"\"` in my checks


## Phase 4: Testing & Debugging *(30%)*

* For the bad inputs you thought of back in **Phase 2**, write a *test case* that you can run to prove that your functions work as expected
    *   It is not necessarily bad if a function crashes if you can explain *why* and *how* it happens
* Write the test cases you have *personally run*
    *   The *exact command* you used
    *   Copy & paste the program's *output*
    *   Be precise so that your grader can replicate your experience
* For any bugs discovered, describe their *cause* and *remedy*
###Test case
* I could run a case where we take bits and pieces of the files and test them incramentaly and backward.
* I discovered alot of missed string bugs that I quickly fixed.
* When reading the lines for identifying software vs all the numbers "0" and "10" were had `""` around them so I had to take that into account. other wise the information I gathered would turn out to be 0.



## Phase 5: Deployment *(5%)*
#**COMPLETE!**
## Phase 6: Maintenance

###Program neatness
* I would say my program this time around Is a lot better written.
* If a bug was reported I'm confident I could fix it.
### Documentation
* My documentation should make sense to others who read it. 
* I would understand it in six months.
### Longevity 
* It should work better after a hardware upgrade.
* Yes It should work on a different operating system.
* It depends on how much they change i think.