log_file = open("um-server-01.txt")
# this is creating a variable for the .txt file for it to open and be used in a equation 


def sales_reports(log_file):
    #def marks the start of a function called sales report and the paramerter is log_file
    for line in log_file:
        # this just created a vairable inside of log_file and the function of it is below
        line = line.rstrip()
        #defininf what line is,and .strip means to strip the txt file of any extra wordage at the beginning and end 
        day = line[0:3]
        #this is creating a new variable called day and day is = to index 0 
        if day == "Mon":
        #this is saying if the first index is equal to tues
            print(line)
            #then to print put the whole array/ line with the content inside of it


sales_reports(log_file) 
#this is running the function that we just created
