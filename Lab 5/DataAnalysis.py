#Lab 5
#File name: DataAnalysis.py
#Author:Andora Zuniga
#Date: September 19th, 2019
#Purpose:   allows a user to load one of two CSV files and then perform histogram analysis
#           and plots for select variables on the datasets

#Import statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

#Variables
fileChoice = 0
columnChoice = ''
popFile = "PopChange.csv"
houseFile = "Housing.csv"
mypath = os.path.dirname(os.path.abspath(__file__))

#Start of program 

print("***************** Welcome to the Python Data Analysis Application***********************")

while fileChoice != 3:
    #Ask user which file they would like store choice
    print("\nSelect the file you want to analyze:")
    print("1. Population Data\n2. Housing Data\n3. Exit the Program")
    
    #Try user input
    while True:
        try:
            fileChoice = int(input())
            break
        except:
            print("Incorrect input, please enter 1, 2, or 3")
        
    if fileChoice == 1:
        #open and load file with class
        popDataFrame = pd.read_csv(mypath+'/PopChange.csv')
        popDataFrame.columns = ['Id', 'Geography', 'Target Geo Id', 'Target Geo Id2', 'Pop Apr 1', 'Pop Jul 1', 'Change Pop']
        
        print("\nYou have entered Population Data!")
        
        while columnChoice != 'd':
            print("Select the Column you want to analyze:")
            print("a. Pop Apr 1\nb. Pop Jul 1\nc. Change Pop\nd. Exit Column")
            
            #try user input
            while True:
                try:
                    columnChoice = input("\n")
                    break
                except:
                    print("Incorrect input, please enter a, b, c, or d")
        
            if columnChoice == 'a':
                print("\nYou selected Pop Apr 1\nThe statistics for this column are:")
                print(popDataFrame['Pop Apr 1'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display1 = popDataFrame.hist(column='Pop Apr 1', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display1=plt
                # Save Figure for Download
                display1.savefig('display1.svg')
                
            if columnChoice == 'b':
                print("\nYou selected Pop Jul 1\nThe statistics for this column are:")
                print(popDataFrame['Pop Jul 1'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display2 = popDataFrame.hist(column='Pop Jul 1', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display2=plt
                # Save Figure for Download
                display2.savefig('display2.svg')
            
            if columnChoice == 'c':
                print("\nYou selected Change Pop\nThe statistics for this column are:")
                print(popDataFrame['Change Pop'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display3 = popDataFrame.hist(column='Change Pop', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display3=plt
                # Save Figure for Download
                display3.savefig('display3.svg')
            
            if columnChoice == 'd':
                print("*Exiting column*")
                
    if fileChoice == 2:
        #open and load file 
        housingDataFrame = pd.read_csv(mypath+'/Housing.csv')
        housingDataFrame.columns = ['AGE', 'BEDRMS', 'BUILT', 'NUNITS', 'ROOMS', 'WEIGHT', 'UTILITY']
        
        print("\nYou have entered Housing Data!")
        
        while columnChoice != 'f':
            print("Select the Column you want to analyze:")
            print("a. AGE\nb. BEDRMS\nc. BUILT\nd. ROOMS\ne. UTILITY\nf. Exit")
            
            #try user input
            while True:
                try:
                    columnChoice = input("\n")
                    break
                except:
                    print("Incorrect input, please enter a, b, c, d, e, or f")
        
            if columnChoice == 'a':
                print("\nYou selected AGE\nThe statistics for this column are:")
                print(housingDataFrame['AGE'].describe())
                 #Histogram
                display8 = housingDataFrame.hist(column='AGE', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display8=plt
                # Save Figure for Download
                display8.savefig('display8.svg')
                
            if columnChoice == 'b':
                print("\nYou selected BEDRMS\nThe statistics for this column are:")
                print(housingDataFrame['BEDRMS'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display4 = housingDataFrame.hist(column='BEDRMS', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display4=plt
                # Save Figure for Download
                display4.savefig('display4.svg')
                
            if columnChoice == 'c':
                print("\nYou selected BUILT\nThe statistics for this column are:")
                print(housingDataFrame['BUILT'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display5 = housingDataFrame.hist(column='BUILT', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display5=plt
                # Save Figure for Download
                display5.savefig('display5.svg')
                
            if columnChoice == 'd':
                print("\nYou selected ROOMS\nThe statistics for this column are:")
                print(housingDataFrame['ROOMS'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display6 = housingDataFrame.hist(column='ROOMS', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display6=plt
                # Save Figure for Download
                display6.savefig('display6.svg')
                
            if columnChoice == 'e':
                print("\nYou selected UTILITY\nThe statistics for this column are:")
                print(housingDataFrame['UTILITY'].describe())
                print("\nThe histogram can be downloaded below")
                #Histogram
                display7 = housingDataFrame.hist(column='UTILITY', bins=50)
                
                plt.grid(True)
                #Assign to a figure
                display7=plt
                # Save Figure for Download
                display7.savefig('display7.svg')
                
            if columnChoice == 'f':
                print("*Exiting*")
        
    if fileChoice == 3:
        print("\n\n*************** Thanks for using the Data Analysis Application**********")
        
        
        
        
        
        