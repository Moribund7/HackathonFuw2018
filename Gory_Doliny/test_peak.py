import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as filters
from skimage.feature import peak_local_max
from pprint import pprint

def filter_map(data):
    kernel = np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 2, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ])
    kernel = kernel/14
    filtered_data = filters.convolve(data, kernel)
    return filtered_data

def find_maximas(data):
    coordinates = peak_local_max(data, min_distance=1)
    return coordinates

def calculate_no_points(n, a1, phi):
    return (n-1)*(a1+phi) + (n-2)

gradients = []

def validate_maxima(coordinate, data):
    grad = np.gradient(data)
    i = 0
    run = True
    while run:
        i += 1
        try:
            gradII = sum(abs(np.array(grad)))[coordinate[0]-i:coordinate[0]+i+1,coordinate[1]-i:coordinate[1]+i+1]
            condition = sum(gradII[0, :] + gradII[gradII.shape[0] - 1, :] + gradII[:, 0] + gradII[:, gradII.shape[0] - 1])
            gradients.append(condition/(8 if i==1 else calculate_no_points(i, 8, 7)))
        except:
            run = False
        if not condition:
            return True
            run = False
    return False

def show_maximas(coordinates, data):
    zeros = np.zeros(data.shape)
    for coordinate in coordinates:
        zeros[coordinate[0], coordinate[1]] = 20
    plt.imshow(data + zeros)
    plt.show()

if __name__ == '__main__':
    data = np.loadtxt('/Users/paulpierzchlewicz/Downloads/data.np')
    peak = data[330:355, 400:440]
    peak = data[570:580, 470:530]
    peak = data[390:500, 280:380]

    # fig,ax = plt.subplots(1)
    # ax.imshow(peak, cmap='rainbow')
    # plt.show()

    maximas = find_maximas(peak)
    show_maximas(maximas, peak)
    # print(maximas)
    # show_maximas([[56, 44]], peak)
    # validate_maxima([56, 44], peak)
    # pprint(gradients)
    # plt.plot(gradients)
    # plt.show()
    #
    # validate_maxima([9, 32], peak)
    # pprint(gradients)
    # plt.plot(gradients)
    # plt.show()

    for i in maximas[:30]:
        gradients = []
        validate_maxima(i, peak)
        # pprint(gradients)
        plt.plot(gradients)
        plt.axhline(np.mean(gradients))
        plt.axhline(np.mean(gradients) + np.std(gradients))
        plt.axhline(np.mean(gradients) - np.std(gradients))
        plt.show()

    # print('mean', np.mean(gradients[15:]))
    # print('std', np.std(gradients[15:]))
