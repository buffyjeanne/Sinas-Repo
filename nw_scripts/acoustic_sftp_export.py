#exporting files into sftp server

"""
@author: sina.herbst
"""

#%% PACKAGES
# general packages
import math
import os
import platform
import sys
import pandas as pd
import pyexasol
import paramiko  #for connection to sftp server
import keyring
#C = pyexasol.connect_local_config('my_exasol') 




# for exasol connection flexibel for own local machine and airflow server we define these functions
def get_environment():
    # is this script running on airflow server or on a local machine?
    if 'nb-' in platform.node():
        return 'local'    
    else:
        return 'server'

def get_exasol_connection(environment_name):   
    if environment_name == 'local':
        # initialize Exasol connection via local config file
        C = pyexasol.connect_local_config('my_exasol')         

    elif environment_name == 'server':
        # initialize Exasol connection via basehook connection
        from airflow.hooks.base_hook import BaseHook
        connection = BaseHook.get_connection("exasol_bu_red_general")
        exapassword = connection.password
        exalogin = connection.login
        C = pyexasol.connect(dsn='10.12.240.200..234:8563', user=exalogin, password=exapassword)
    return C


############################################
def get_acoustic_connection(environment_name):   
    if environment_name == 'local':
        # initialize acoustic connection via local config file
        ac_password=keyring.get_password("acoustic", "exchange_recruitingr")
        #ac_login = "exchange_recruitingr_sandbox@xing.com"        

    elif environment_name == 'server':
        # initialize acoustic connection via basehook connection
        from airflow.hooks.base_hook import BaseHook
        connection = BaseHook.get_connection("berry_acoustic_sandbox")
        ac_password = connection.password
        #ac_login = connection.login
    #return [ac_password, ac_login]
    return ac_password
#################################################


environment_name = get_environment()
#Exasol connection
C = get_exasol_connection(environment_name)

#acoustic connection
#works only on server
"""
from airflow.hooks.base_hook import BaseHook
connection = BaseHook.get_connection("berry_acoustic_sandbox")
ac_password = connection.password
ac_login = connection.login
"""

ac_password=get_acoustic_connection(environment_name)
ac_login = "exchange_recruitingr_sandbox@xing.com"




sql_stmt_main = """
SELECT * from tmp_tables.acoustic_second_main_database ;
"""
df_main = C.export_to_pandas(query_or_table=sql_stmt_main, callback_params={'decimal': ','})

##old way
#results_main = C.execute(sql_stmt_main) 
"""
df_main=pd.DataFrame(results_main,
                   columns = [
                    'master_user_id',
                   'xing_user_id', 
                   'sf_contact_id',
                   'lead_id',
                   'silverpop_recipient_id',
                   'Email', 
                   'first_name', 
                   'last_name',
                   'salutation', 
                   'country', 
                   'account_id', 
                   'title', 
                   'contact_owner',
                   'contact_owner_email', 
                   'contact_owner_phone',
                   'contact_owner_role',
                   'is_primary_contact,',
                   'do_not_contact',
                    'is_sf_contact',
                     'onboarding_Wizard_User',
                      'xtm_User',
                       'xtp_User',
                        'Jobs_User',
                         'EBP_User',
                         'active_flag']       )

"""

sql_stmt_contr = """
SELECT * from tmp_tables.acoustic_productcontract;
"""
df_contr = C.export_to_pandas(query_or_table=sql_stmt_contr, callback_params={'decimal': ','})


sql_stmt_acc = """
SELECT * from tmp_tables.acoustic_account
"""
df_acc = C.export_to_pandas(query_or_table=sql_stmt_acc, callback_params={'decimal': ','})


sql_stmt_opp = """
SELECT * from tmp_tables.acoustic_opp
"""
df_opp = C.export_to_pandas(query_or_table=sql_stmt_opp, callback_params={'decimal': ','})


sql_stmt_user= """
SELECT * from tmp_tables.acoustic_productuser
"""
df_user = C.export_to_pandas(query_or_table=sql_stmt_user, callback_params={'decimal': ','})






## test paramiko for connecting to sftp server

#connection to sftp server
host = "18.157.136.170"#"sftp://transfer-campaign-eu-1.goacoustic.com"
port = 22
transport = paramiko.Transport((host, port))
#Create a Transport object


transport.connect(username = ac_login, password = ac_password)
#Connect to a Transport server
sftp = paramiko.SFTPClient.from_transport(transport)

with sftp.open('/upload/second_database.csv', "w") as f:
    f.write(df_main.to_csv(index=False))


with sftp.open('/upload/productcontract.csv', "w") as f:
    f.write(df_contr.to_csv(index=False))


with sftp.open('/upload/accounts.csv', "w") as f:
    f.write(df_acc.to_csv(index=False))

with sftp.open('/upload/opp.csv', "w") as f:
    f.write(df_opp.to_csv(index=False))

with sftp.open('/upload/productuser.csv', "w") as f:
    f.write(df_user.to_csv(index=False))


sftp.close()
transport.close()




###current script on airflow 

#
"""
@author: sina.herbst
"""

#%% PACKAGES
# general packages
import math
import os
import platform
import sys
import pandas as pd
import pyexasol 
import paramiko  #for connection to sftp server

# for exasol connection flexibel for own local machine and airflow server we define these functions
def get_environment():
    # is this script running on airflow server or on a local machine?
    if 'nb-' in platform.node():
        return 'local'    
    else:
        return 'server'

def get_exasol_connection(environment_name):   
    if environment_name == 'local':
        # initialize Exasol connection via local config file
        C = pyexasol.connect_local_config('my_exasol')         

    elif environment_name == 'server':
        # initialize Exasol connection via basehook connection
        from airflow.hooks.base_hook import BaseHook
        connection = BaseHook.get_connection("exasol_bu_red_general")
        exapassword = connection.password
        exalogin = connection.login
        C = pyexasol.connect(dsn='10.12.240.200..234:8563', user=exalogin, password=exapassword)
    return C

environment_name = get_environment()
#Exasol connection
C = get_exasol_connection(environment_name)

from airflow.hooks.base_hook import BaseHook
connection = BaseHook.get_connection("berry_acoustic")
ac_password = connection.password
ac_login = connection.login



sql_stmt_main = """
SELECT * from tmp_tables.acoustic_second_main_database
"""
results_main = C.execute(sql_stmt_main) 
df_main = C.export_to_pandas(query_or_table=sql_stmt_main, callback_params={'decimal': ','})




#connection to sftp server
host = "18.157.136.170"#"sftp://transfer-campaign-eu-1.goacoustic.com"
port = 22
transport = paramiko.Transport((host, port))
#Create a Transport object

transport.connect(username = ac_login, password = ac_password)
#Connect to a Transport server
sftp = paramiko.SFTPClient.from_transport(transport)

with sftp.open('/upload/testfile2.csv', "w") as f:
    f.write(df_main.to_csv(index=False))
    
sftp.close()
transport.close()


