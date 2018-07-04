#!/usr/bin/python3



#*****************************************************#
# To Configure PUSH/PULL							  #
# PUSH is set by default					 		  #
# To enable PULL, set PUSH_pull variable to False.    #
#*****************************************************#
PUSH_pull=True



#*********************************************#
# To Configure number of hops a query		  #
# should propagate to				 		  #
#*********************************************#
HOP=10  

#*********************************************#
# To Configure TTR value 		  			  #
# the number is in seconds.					  #
# TTR>=1 			 		  				  #
#*********************************************#
TTR=40  #seconds



#*********************************************#
# To Configure Ports					  	  #
# Change the numbers to get new ports,		  #
# if they are busy.				 			  #
# DO NOT CHANGE THE VARIABLE NAME			  #
#*********************************************#
#portList=[6126,6127,6128,6129,6130,6131,6132,6133,6134,6135]
portList=[xx for xx in range(6126,6136)]


#*****************************************************#
# Each set corresponds to a peer. 					  #
# To change port, use portList. DO NOT change it here #
# To change shared directory, change the path variable#
#*****************************************************#

peer_1_port=portList[0]
peer_1_port_conn=[portList[1]]
peer_1_path='peer_1_sharedFolder/*'

peer_2_port=portList[1]
peer_2_port_conn=[portList[2]]
peer_2_path='peer_2_sharedFolder/*'

peer_3_port=portList[2]
peer_3_port_conn=[portList[3]]
peer_3_path='peer_3_sharedFolder/*'

peer_4_port=portList[3]
peer_4_port_conn=[portList[4]]
peer_4_path='peer_4_sharedFolder/*'

peer_5_port=portList[4]
peer_5_port_conn=[portList[5]]
peer_5_path='peer_5_sharedFolder/*'

peer_6_port=portList[5]
peer_6_port_conn=[portList[6]]
peer_6_path='peer_6_sharedFolder/*'

peer_7_port=portList[6]
peer_7_port_conn=[portList[7]]
peer_7_path='peer_7_sharedFolder/*'

peer_8_port=portList[7]
peer_8_port_conn=[portList[8]]
peer_8_path='peer_8_sharedFolder/*'

peer_9_port=portList[8]
peer_9_port_conn=[portList[9]]
peer_9_path='peer_9_sharedFolder/*'

peer_10_port=portList[9]
peer_10_port_conn=[portList[0]]
peer_10_path='peer_10_sharedFolder/*'



