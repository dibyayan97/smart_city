#code to generate the centroid of nodes marked by aruco markers 

import numpy as np
import cv2
import cv2.aruco as aruco

def nodesdetector(cap):
    node_cent_stored = np.zeros((8,2))
    #creating array of node centroids
    node_centroid_array = np.zeros((8,2))

    while(True):
        init = 0 
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come here
        if ret is True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()


        '''    detectMarkers(...)
            detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
            mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''

        #lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        # converting to numpy array 
        arr_full = np.array(corners)

        # initializing node array to zero to store corner values
        node_array = np.zeros((8,4,2))        


        # resizing the array to required dimensions
        corners_array = np.resize(arr_full,(len(corners),4,2))

        #creating an array of which stores values of corners corresponding to certain ids
        #The corner value remains zero if the corner is not detected

        if len(corners)> 0 :
            for i in range(0,len(corners)):
                if ids[i] == 1 :
                    node_array[0] = corners_array[i]
                elif ids[i] == 2 :
                    node_array[1] = corners_array[i]
                elif ids[i] == 3 :
                    node_array[2] = corners_array[i]
                elif ids[i] == 4 :
                    node_array[3] = corners_array[i]
                elif ids[i] == 5 :
                    node_array[4] = corners_array[i]
                elif ids[i] == 6 :
                    node_array[5] = corners_array[i]
                elif ids[i] == 7 :
                    node_array[6] = corners_array[i]
                elif ids[i] == 8 :
                    node_array[7] = corners_array[i]

        # for calculating the centroid of the nodes with the corner coordinates
        for i in range(0,8):

            x_sum = 0
            y_sum = 0

            for j in range(0,4):
                x_sum = x_sum + node_array[i][j][0]
                y_sum = y_sum + node_array[i][j][1]
                j = j+1

            #To store previous centroid values if node is not detected 
            if x_sum != 0 and y_sum != 0:
                node_centroid_array[i][0] = x_sum/4
                node_centroid_array[i][1] = y_sum/4


        print(corners_array)
        print('---------------------------------------')
        print(ids)
        print('----------------------------------------')
        print(node_array)
        print('-----------------------------------------')
        print(node_centroid_array)
        print('\n\n\n')
        gray = aruco.drawDetectedMarkers(gray, corners,ids)

        #To end camera feed 
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(1)    
nodesdetector(cap)
