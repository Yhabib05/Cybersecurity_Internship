import array
import os
import time
import pyfiglet
import joblib
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.preprocessing import RobustScaler


# Load the model from the file
model = joblib.load('model_file.pkl')


#defining the necessary functions

#Scaling
def Scaling(df_num, cols):
    std_scaler = RobustScaler()
    std_scaler_temp = std_scaler.fit_transform(df_num)
    std_df = pd.DataFrame(std_scaler_temp, columns =cols)
    return std_df 

#preprocessing
cat_cols = ['is_host_login','protocol_type','service','flag','land', 'logged_in','is_guest_login', 'level', 'outcome']
def preprocess(dataframe):
    df_num = dataframe.drop(cat_cols, axis=1)
    num_cols = df_num.columns
    scaled_df = Scaling(df_num, num_cols)
    
    dataframe.drop(labels=num_cols, axis="columns", inplace=True)
    dataframe[num_cols] = scaled_df[num_cols]
    
    dataframe.loc[dataframe['outcome'] == "normal", "outcome"] = 0
    dataframe.loc[dataframe['outcome'] != 0, "outcome"] = 1
    
    dataframe = pd.get_dummies(dataframe, columns = ['protocol_type', 'service', 'flag'])
    return dataframe


#loading the data
data_train = pd.read_csv("KDDTrain+.txt")

#assigning the columns to the data frame
columns = (['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot'
               ,'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations'
               ,'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate'
               ,'srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count'
               ,'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate'
               ,'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','outcome','level'])

data_train.columns = columns

#transforming the independent variable of the data to a binary output (attack/normal)
data_train.loc[data_train['outcome'] == "normal", "outcome"] = 'normal'
data_train.loc[data_train['outcome'] != 'normal', "outcome"] = 'attack'

#getting the preprocessed training data
scaled_train = preprocess(data_train)





# Make predictions using the loaded model

#log example:
#log = "0,tcp,ftp_data,SF,491,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0.00,0.00,0.00,0.00,1.00,0.00,0.00,150,25,0.17,0.03,0.17,0.00,0.00,0.00,0.05,0.00,normal,20"

def preprocess_log(log):

    # Split the log string by comma
    log_data = log.split(',')

    # Create a DataFrame with a single row
    df = pd.DataFrame([log_data])
    df.columns = columns

    # Preprocess the log DataFrame
    preprocessed_log = preprocess(df)

    # Get the original features from the preprocessed training data
    original_features = scaled_train.drop(['outcome', 'level'], axis=1).columns

    # Reindex the preprocessed log DataFrame to include all the original features
    preprocessed_log = preprocessed_log.reindex(columns=original_features, fill_value=0)
    
    return preprocessed_log


def run_intrusion_detection(log):
    #preprocess
    # Check if the log contains the outcome value
    if len(log.split(',')) == len(columns):
        # Log contains the outcome value
        preprocessed_log = preprocess_log(log)
    else:
        # Log does not contain the outcome value
        log += ',unknown' # Add a placeholder value for the outcome (normally it s for the last column but as we drop both the last and the one before it,level and outcome, we dont care that much)
        preprocessed_log = preprocess_log(log)

    # Make predictions using the loaded model
    prediction = model.predict(preprocessed_log)

    # Process the prediction result
    if prediction == 1:
        print("Intrusion detected!")
    else:
        print("No intrusion detected.")


def exit_program():
    exit()

def start():
    print(pyfiglet.figlet_format("Intrusion Detector"))
    print(" Welcome to the intrusion detector \n")
    print(" 1. Perform Intrusion Detection")
    print(" 2. Exit\n")

    select = int(input("Enter your choice: "))

    if select == 1:
        print("\nEnter a log with the specifications:\n\n"
              "duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment,\n"
              "urgent, hot, num_failed_logins, logged_in, num_compromised, root_shell, su_attempted, num_root,num_file_creations\n"
               ",num_shells, num_access_files, num_outbound_cmds, is_host_login, is_guest_login, count, srv_count, serror_rate\n"
               ",srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate, srv_diff_host_rate, dst_host_count, dst_host_srv_count\n"
               ",dst_host_same_srv_rate, dst_host_diff_srv_rate, dst_host_same_src_port_rate, dst_host_srv_diff_host_rate, dst_host_serror_rate\n"
               ",dst_host_srv_serror_rate, dst_host_rerror_rate, dst_host_srv_rerror_rate, outcome,level\n\n")
        log = input("Enter the log: ")
        run_intrusion_detection(log)
        
        choice = input("Do you want to perform another intrusion detection? (y/n)")
        if choice.lower() == 'y':
            start()
        else:
            exit_program()

    elif select == 2:
        exit_program()

    else:
        print("Bad input\nExiting...")
        time.sleep(3)
        exit_program()

start()


