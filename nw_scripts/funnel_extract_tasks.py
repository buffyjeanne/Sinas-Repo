import math
import pandas as pd
#import requests
import pyexasol
import os
C = pyexasol.connect_local_config('my_exasol') 
#C = pyexasol.connect(dsn='10.12.240.200..234:8563', user=exalogin, password=exapassword)



#Test ID :	WHERE id='00T1i000025piGdEAI'     
  
sql_stmt = """
SELECT ID, DESCRIPTION
	FROM BU_RED_ETL.SALESFORCE_TASKS 
    where DESCRIPTION like '%%Landingpage%%'
    and  DESCRIPTION like '%%sc_cmp=%%'
    AND CREATEDDATE >='2022-01-01'
"""


results = C.execute(sql_stmt) 
df1 = pd.DataFrame(results, 
                   columns = ['ID', 'DESCRIPTION']                   
                  )

df1['LP_no']=df1['DESCRIPTION'].str.find('Landingpage')
#df1['LP_no']=df1.DESCRIPTION.str.find('Landingpage') #alternative
#df1[df1['LP_no']>0]


#df1['LP']=df1.DESCRIPTION.str[10:]#geht
#df1['LP']=df1.DESCRIPTION.str.slice(10,) #geht

#df1['LP']=df1.DESCRIPTION.str[df1['LP_no']:] #geht nicht
#df1['test']=df1['DESCRIPTION'][df1.LP_no:] #geht nicht

#couldn't find a way like df1['LP']=df1.DESCRIPTION.str[df1['LP_no']:] so we used lambda functions
df1['LP']=df1.apply(lambda x: x['DESCRIPTION'][x['LP_no']:], axis=1)
#df1['occ']=df1.apply(lambda x: x['sc_cmp'])
df1['sc_no']=df1.LP.str.rfind('sc_cmp=')
df1['sc_cmp']=df1.apply(lambda x: x['LP'][x['sc_no']+7:], axis=1)

df1['sc_end1']=df1.sc_cmp.str.find('\n')
df1['sc_end2']=df1.sc_cmp.str.find('&')
#df1['sc_end3']=df1.sc_cmp.str.find('/')
df1['sc_end4']=df1.sc_cmp.str.find('?')
#df1['sc_end5']=df1.sc_cmp.str.find('%')
#df1['sc_end6']=df1.sc_cmp.str.find('/')

def to_nan(ind):
    if ind==-1:
        out=float('nan')
    else:
        out=ind
    return out


#to make the min function about that columns possible we have to exclude the -1 value meaning there is no sign of \n etc
df1['sc_end1']=df1.sc_end1.apply(to_nan)
df1['sc_end2']=df1.sc_end2.apply(to_nan)
#df1['sc_end3']=df1.sc_end3.apply(to_nan)
df1['sc_end4']=df1.sc_end4.apply(to_nan)
#df1['sc_end5']=df1.sc_end5.apply(to_nan)


#getting minimum of the three columns sc_endi
df1['sc_end']=df1[['sc_end1','sc_end2',  'sc_end4']].min(axis=1)
#df1['sc_end']=df1[[ 'sc_end4']].min(axis=1)

def del_nan(end):
    if math.isnan(end):
        out=1300
    else :
        out=end
    return out

df1['sc_end']=df1.sc_end.apply(del_nan)

df1['sc_end']=df1['sc_end'].astype('int')

df1['sc_end']=df1.sc_end.astype('int')

#to avoid problems if the parameter goes until the end (and there is no \n, ? or &)
def extr(part, end):
    if end==-1:
        out=part
    else :
        out=part[:end]
    return out


df1['sc_cmp']=df1.apply(lambda x: extr(x['sc_cmp'], x['sc_end']), axis=1)


#df1['sc_cmp']=df1.apply(lambda x: x['sc_cmp'][:x['sc_end']], axis=1)
#df1[df1['ID']=='00T1i000025pjg9EAA']

#deleting unessacary
df1.drop('LP', axis=1, inplace=True)
df1.drop('LP_no', axis=1, inplace=True)
df1.drop('sc_no', axis=1, inplace=True)
df1.drop('sc_end1', axis=1, inplace=True)
df1.drop('sc_end2', axis=1, inplace=True)
#df1.drop('sc_end3', axis=1, inplace=True)
df1.drop('sc_end4', axis=1, inplace=True)
#df1.drop('sc_end5', axis=1, inplace=True)
df1.drop('sc_end', axis=1, inplace=True)
df1.drop('DESCRIPTION', axis=1, inplace=True)

#getting length per row in a column
#df1['len']=df1.sc_cmp.str.len()
#df1.drop('len', axis=1, inplace=True)


##writing back to exasol
sql_stmt = """
CREATE OR REPLACE TABLE tmp_tables.salesforce_tasks_with_tracking_parameter  ( 
                Id VARCHAR(18),
                sc_cmp varchar(1300)
                )
"""
results = C.execute(sql_stmt) 
# COPIED from SQL Scanner
C.import_from_pandas(df1, ('tmp_tables','salesforce_tasks_with_tracking_parameter'))























