# AGE OF INFORMATION ON TRAINING MACHINE LEARNING MODELS
Aim of this project is to do a performance analysis on  how age of information impacts training of a machine learning model.
Thus to do so we have take the hourly Energy consumption of PJM Interconnection LLC which is a regional transmission organization(RTO) in the United States. The dataset is provided in the dataset directry. The model used for prediction is the Facebook Prophet model.

There are various scenarios for which the analysis is done.

## Scenario 1:Introduction of Delays (in hours) tothe Data-set
In this scenario we have to add a random or a static or an uniform delay to the dataset inorder carry the analysis.

Steps:-
1. Run the random_static_uniform_delay.py

## Scenario 2: Implementation  of  Gilbert  ElliotChannel
In this case we implement a Server  and  a  Client  model  withGilbert  Elliot  channel.

To experiment, run the below files sequentially:-

Step 1: Run client_pre_processing.py

Step 2: Run server_edited.py

Step 3: Run client_edited.py

The Received file will be generated in the server_file folder under the server_client directory.

Once the received file is created, run the implementation_gillbert_elliot.py

## Scenario 3: Introduction of delay during data transmission
Here, a delay is introduced for the data transmission. Each packet is termed either as a good packet or a bad packet and if it is a good packet then it is transmitted to server with delay else it is dropped.

Hence, to investigated the effect of delay on dataset, follow the below steps orderly:-

Step 1: Run client_pre_processing_with_delay.py

Step 2: Run server_edited.py

Step 3: Run client_edited.py

The Received file will be generated in the server_file folder under the server_client directory.

Once the received file is created, run the gillbert_elliot_channel_with_delay.py



Lastly few plots are drawn using the plots.py.




update