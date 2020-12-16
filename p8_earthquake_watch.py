'''
CIS210 Project 8 Fall 2020

Author: Nathaniel Mason

Credits: N/A

Use a data file from the United States Geological Survey and implement a data mining algortihm to analyze the earthquake data found within the file.
After analyzing, plot the earthquake clusters on a world map with dot size depending on the magnitudes found in the data.
'''

from turtle import *
import math
import csv
import random
import doctest
import urllib.request


def euclidD(point1, point2):
    '''
    (point1: list, point2: list) -> float

    Determines the distance between two points, each point being a list of n coordinate values. 

    >>> euclidD([144.8897, 38.0555], [-84.0888, -41.4839])
    242.39981356141757
    '''
    
    total = 0
    for i in range(len(point1)):
        diff = (point1[i] - point2[i]) ** 2
        total += diff

    euclid_dist = math.sqrt(total)
    
    return euclid_dist


def createCentroids(k, data_dict):
    '''
    (k: int, data_dict: dict) -> list

    Randomly selects k number of centroids from the data dictionary (docstring answer changes every time)

    > createCentroids(5, {1: [-117.8533, 38.1693, 5.3], 2: [159.674, -53.1238, 5.7], 3: [117.2718, -49.5935, 5.0], 4: [122.7546, 4.1131, 5.1], 5: [126.2419, 10.1895, 5.2], 6: [121.8976, 21.651, 5.0], 7: [142.7625, 25.4623, 5.7], 8: [20.7954, 41.6953, 5.0]})
    [[126.2419, 10.1895, 5.2], [20.7954, 41.6953, 5.0], [122.7546, 4.1131, 5.1], [117.2718, -49.5935, 5.0], [159.674, -53.1238, 5.7]] 
    '''
    
    centroids = []
    centroid_count = 0
    centroid_keys = []

    while centroid_count < k:
        rkey = random.randint(1, len(data_dict))
        if rkey not in centroid_keys:
            centroids.append(data_dict[rkey])
            centroid_keys.append(rkey)
            centroid_count += 1

    return centroids


def createClusters(k, centroids, data_dict, r):
    '''
    (k: int, centroids: list, data_dict: dictionary, r: int) -> list

    Calls: euclidD

    Clusters the keys that point to the data from the data dictionary based on the distance between the data and centroids, then finds the mean of each cluster to create new centroids. Repeats "r" times.

    >>> createClusters(5, [[126.2419, 10.1895, 5.2], [20.7954, 41.6953, 5.0], [122.7546, 4.1131, 5.1], [117.2718, -49.5935, 5.0], [159.674, -53.1238, 5.7]],{1: [-117.8533, 38.1693, 5.3], 2: [159.674, -53.1238, 5.7], 3: [117.2718, -49.5935, 5.0], 4: [122.7546, 4.1131, 5.1], 5: [126.2419, 10.1895, 5.2], 6: [121.8976, 21.651, 5.0], 7: [142.7625, 25.4623, 5.7], 8: [20.7954, 41.6953, 5.0]}, 10)
    ****PASS 1 ****
    ****PASS 2 ****
    ****PASS 3 ****
    ****PASS 4 ****
    ****PASS 5 ****
    ****PASS 6 ****
    ****PASS 7 ****
    ****PASS 8 ****
    ****PASS 9 ****
    ****PASS 10 ****
    [[6, 7], [1, 8], [4, 5], [3], [2]]
    '''
    
    for aPass in range(r):
        print(f'****PASS {aPass + 1} ****')
        clusters = [] #create list of k empty lists

        for i in range(k):
            clusters.append([])

        for aKey in data_dict: #calculate distance to centroid
            distances = []

            for clusterIndex in range(k):
                dToC = euclidD(data_dict[aKey], centroids[clusterIndex])
                distances.append(dToC)
                
            minDist = min(distances) #find minimum distance
            index = distances.index(minDist)

            clusters[index].append(aKey) #add to cluster

        dimensions = len(data_dict[1]) #recompute the clusters

        for clusterIndex in range(k):
            sums = [0] * dimensions #initialize sum for each dimension
            
            for aKey in clusters[clusterIndex]:
                data_points = data_dict[aKey]

                for ind in range(len(data_points)): #calculate sums
                    sums[ind] += data_points[ind]
                    
            for ind in range(len(sums)): #calculate average
                cluster_len = len(clusters[clusterIndex])
                
                if cluster_len != 0: #do not divide by zero
                    sums[ind] = sums[ind] / cluster_len
                    
            centroids[clusterIndex] = sums #assign avg to centroids
    '''
        for c in clusters:
            print("CLUSTER")
            
            for key in c:
                print(data_dict[key], end = " ")
                
            print()
    '''
    
    return clusters


def readFile(fname):
    '''
    (fname: str) -> dictionary

    Returns a data dictionary after opening the specified file

    >>> readFile('test_equakes.csv')
    {1: [-117.8533, 38.1693, 5.3], 2: [159.674, -53.1238, 5.7], 3: [117.2718, -49.5935, 5.0], 4: [122.7546, 4.1131, 5.1], 5: [126.2419, 10.1895, 5.2], 6: [121.8976, 21.651, 5.0], 7: [142.7625, 25.4623, 5.7], 8: [20.7954, 41.6953, 5.0]}
    '''

    with open(fname, mode='r', encoding='utf8') as eqfile:
        datadict = {}
        key = 0
        csvR = csv.reader(eqfile)
        next(csvR)
        
        for aline in csvR:
            #aline = aline.strip().split() done by csv module
            key += 1
            lat = float(aline[1])
            long = float(aline[2])
            mag = float(aline[4])
            datadict[key] = [long, lat, mag]
            
    return datadict

#readFile(fname='world_equakes.csv')

def readeqi():
    '''
    Returns a data dictionary after getting the data directly from USGS website
    '''
    #with urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/1/\query?format=csv\&starttime=2019-11-13\&minmagnitude=5') as eqf: backslashes from instructions did not work
    with urllib.request.urlopen('https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2019-11-13&minmagnitude=5') as eqf:
        datadict = {}
        key = 0
        eqf.readline()
        for aline in eqf:
            aline = aline.strip().split(b',')
            key += 1
            lat = float(aline[1])
            long = float(aline[2])
            mag = float(aline[4])
            datadict[key] = [long, lat, mag]
    
    return datadict

def writeeqiToFile():
    '''
    Reads the data from the USGS website and then saves it to a data file that will be used in readFile()
    '''
    with urllib.request.urlopen('https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2019-11-13&minmagnitude=5') as eqf:
        data = eqf.read()
    f = open('world_equakes_website.csv', 'wb')
    f.write(data)
    f.close()
    
    return 

def visualizeQuakes(k, r, dataFile):
    '''
    (k: int, r: int, fname: str) -> None

    Data mining, creates clusters based on centroids and data dictionary and then plots the earthquake clusters on a world map.

    Calls: readFile, createCentroids, createClusters

    >>> visualizeQuakes(6, 4, 'world_equakes.csv')
    ****PASS 1 ****
    ****PASS 2 ****
    ****PASS 3 ****
    ****PASS 4 ****
    '''
    #data_dict = readeqi() #changed from readFile() function so that now the data is accessed directly from the USGS website
    writeeqiToFile() #writes data from USGS website to a file named 'world_equakes_website.csv'
    data_dict = readFile('world_equakes_website.csv')
    centroids = createCentroids(k, data_dict)
    clusters = createClusters(k, centroids, data_dict, r)
    eqDraw(k, data_dict, clusters)
    
    return


def eqDraw(k, eqDict, eqClusters):
    '''
    (k: int, eqDict: dict, eqClusters: list) -> Turtle graphics drawing

    Plots points with different sizes based on earthquake magnitudes on a world map.

    >>> eqDraw(5, {1: [-117.8533, 38.1693, 5.3], 2: [159.674, -53.1238, 5.7], 3: [117.2718, -49.5935, 5.0], 4: [122.7546, 4.1131, 5.1], 5: [126.2419, 10.1895, 5.2], 6: [121.8976, 21.651, 5.0], 7: [142.7625, 25.4623, 5.7], 8: [20.7954, 41.6953, 5.0]}, [[6, 7], [1, 8], [4, 5], [3], [2]])
    '''
    tracer(0,0)
    speed('fastest')
    bgpic('world_map.gif')
    screensize(1800, 900)

    wFact = (screensize() [0]/2)/ 180
    hFact = (screensize() [1]/2)/ 90

    hideturtle()
    penup()

    # note: len(colorlist) must be >= k
    colorlist = ['red', 'lawngreen', 'blue',
                 'orange', 'cyan', 'yellow']

    for clusterIndex in range(k):
        color(colorlist[clusterIndex])
        
        for aKey in eqClusters[clusterIndex]:
            longitude = eqDict[aKey][0]
            latitude = eqDict[aKey][1]
            mag = eqDict[aKey][2]
            
            goto(longitude*wFact, latitude*hFact)
        
            if mag <= 5:
                s = 3
            elif 5 < mag <= 5.4:
                s = 6
            elif 5.4 < mag <= 6.0:
                s = 9
            elif 6.0 < mag <= 6.9:
                s = 12
            elif 6.9 < mag <= 7.9:
                s = 15
            else:
                s = 3
            dot(s) # note: dot can take an optional size argument, "s" in this case
    update()

    #exitonclick()
    
    return 

def main():
    '''
    Top level function for earthquake data mnining

    Calls: visualizeQuakes
    '''
    k = 6
    r = 100
    file_name = 'world_equakes.csv'
    
    visualizeQuakes(k, r, file_name)
    
    return

if __name__ == '__main__':
    main()

doctest.testmod()       
    
