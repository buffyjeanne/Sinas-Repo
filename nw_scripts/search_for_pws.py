#################
# First Step: Browse current repo on git, testing on my repo

import os
#import csv
#import pyexasol
import pandas as pd
#import re


##getting the password
#import atc_functions 
#from atc_functions import *
#password=exapassword
os.chdir('C:\\Users\\sina.herbst\\Documents')
import exasol_tech_user_config
import sfdc_config
password_ex=exasol_tech_user_config.password
password_sf=sfdc_config.password
#passwords=[password_ex, password_sf, 'lalalala']
passwords={'password_ex':password_ex, 'password_sf':password_sf, 'lalalala':'lalalala'}



crawling_directories = ['C:\\Users\\sina.herbst\\Documents\\git_repos\\Sinas-Repo']


# initialize Exasol connection  via local config file
#C = pyexasol.connect_local_config('my_exasol') 

files = []
for cd in crawling_directories:
    os.chdir(cd)
    path = os.getcwd()

    #get all files: Build Rfiles
    print('Crawling ' + cd)
    for r, d, f in os.walk(path):
        for file in f:
            #if '.R' in file:   # exclude to avoid strange char conversion errors 
                #get type
                # if '\\Tasks\\' in r:
                #     frequency_type = 'adhoc'
                # else:
                #     frequency_type = 'process'
                
            #files.append([os.path.join(r, file),'R file'])
            files.append(os.path.join(r, file))
            
    print('Files found: ' + str(len(files)))    
    print('')



files_with_credentials=[]
for file in files:
    try:
        with open(file) as f:
            if pw in f.read():
                #print("true")
                #var=
                files_with_credentials.append([file, 'test'])
    except:
    # Rlines =[]
        print('Error - ignoring file')





files_with_credentials=[]
for file in files:
    for key, value in passwords.items():
        try:
            with open(file) as f:
                if value in f.read():
                    #print("true")
                    #var=
                    files_with_credentials.append([file, key])
        except:
        # Rlines =[]
            print('Error - ignoring file')





