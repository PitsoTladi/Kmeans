import matplotlib.pyplot as plt
import random as rn
import numpy as np
import math


# function that calculate distance between two points
def euclidean_Distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


# return a list of x data and a list of y data
def get_x_y_data(data):
    # get x and y coordinates
    x_data = [p[0] for p in data]
    y_data = [p[1] for p in data]
    return [x_data, y_data]


# function to plot data
def plot_data(cluster, cluster_colour):
    x_data, y_data = get_x_y_data(cluster)
    graph = plt.subplot(2, 1, 1)

    # plot and label graph
    plt.xlabel('Birth Rate')
    plt.ylabel('Life expectancy')
    graph.scatter(x_data, y_data, c=cluster_colour)


# filter countries from points
def countries(cluster):
    country_list = []

    # loop through the data
    for cluster_point in cluster:

        # if coountry data belongs a cluster add country to cluster list
        for country, point in file_data.items():
            if cluster_point == point:
                # add country
                country_list.append(country)
                break

    return country_list


# used to calculate an average of a cluster
def cluster_average(cluster):
    x, y = get_x_y_data(cluster)

    # calculate mean for x and y points
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # return the mean
    return [x_mean, y_mean]


# used to read data from the csv file and create a dictionary data
def read_file(file_name):
    # open file
    f = open(file_name, 'r')
    f.readline()

    # create a dictionary to store the data
    data = {}
    for line in f:
        country, x, y = line.strip('\n').split(',')
        data[country] = (float(x), float(y))

    return data


# report about the data
def generate_report(all_Clusters):
    # ask user to enter the number of iterations they want
    # create a colour list
    colour_list = ['r', 'green', 'blue', 'black']
    # create a counter for cluster numbers
    c_numb = 1
    for cl in all_Clusters:
        # print results
        print(f"Cluster {c_numb} birth and death rate mean is:")
        print(cluster_average(cl))
        print(f"countries that belong to cluster {c_numb} are: ")
        print("\n".join(countries(cl)))
        plot_data(cl, colour_list[c_numb - 1])
        c_numb += 1
        country_num = len(cl)
        print(f'there are {country_num} countries in cluster {c_numb - 1} ')

    plt.show()


# this is where the algorithmn start
def start_Kmean(numb_clusters):
    clusterPoints = [point for point in file_data.values()]

    start_clusterpoints = rn.sample(clusterPoints, numb_clusters)

    all_clusters = [[] for nc in range(numb_clusters)]

    # iterate through the points in the cluster
    for point in clusterPoints:

        # create a distance list
        distances = []
        for c in range(numb_clusters):
            # calculate distance between points
            d = euclidean_Distance(point, start_clusterpoints[c])  # distance for cluster 1 point
            # add distanceto the list
            distances.append(d)

        # find shortest distance between points
        shotest_distance = min(distances)
        for c in range(numb_clusters):
            if shotest_distance == distances[c]:
                all_clusters[c].append(point)
                break

    generate_report(all_clusters)


data_file = input('enter file name:\ndata1953.csv\ndata2008.csv\ndataBoth.csv\t')
file_data = read_file(data_file)

# No of clusters
num_Cluster = 2
while True:
    try:
        num_Clusters = int(input("Enter the number of clusters:\t"))
        break
    except ValueError:
        print("Please enter a valid number of clusters:")
# No of Iterations
num_Iterations = 6
while True:
    try:
        num_Iterations = int(input("Enter the number of Iterations:\t"))
        break
    except ValueError:
        print("Please enter the valid number of iterations: ")

start_Kmean(num_Clusters)

'''resources:
https://jakevdp.github.io/PythonDataHandbook/05.11-k-means.html#:~:text=The%20k%2Dmeans%20%algorithm%20%searches,points%20belonging%20%to%20%the%20%cluster.
>https://youtu.be/1XqG0kaJVHY
>https://www.geekforgeeks.org
>https://towardsdatascience.com/k-means-clustering-for-beginners-ea2256154109

'''
 