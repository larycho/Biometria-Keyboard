import numpy as np

data_samples = np.array([ [0.28078651 , 0.1872046, 0.0 , 0.22233319 ] , 
                         [0.27253509 , 0.24622488 , 0.15918374, 0.0980804],
                         [0.0, 0.00318193, 0.06106949, 0.0],
                         [0.27253509 , 0.24622488 , 0.15918374, 0.0980804]])

data_class = np.array([1, 2, 1, 2])

compared = 0 # The index of the sample set we want to compare to other ones
distances = np.zeros(len(data_samples))

for i in range(len(data_samples)): # Calculating Euclidean distance between the main sample and other samples

    distance = (data_samples[compared] - data_samples[i])**2
    distance = distance.sum(axis=-1)
    distance = np.sqrt(distance)

    distances[i] = distance


# Merging the array of samples with array of ids (matching distance to id)
distances = np.split(distances, len(distances))
data_class = np.split(data_class, len(data_class))
distances_classes = np.concatenate((distances, data_class), axis=1)

# Removing the array element that represents the distance of the main sample to itself
distances_classes = np.delete(distances_classes, compared, 0)

# Sorting by distance
distances_classes = distances_classes[distances_classes[:, 0].argsort()]

if (len(distances_classes) >= 2): # Protection against out of bounds errors

    first_result = distances_classes[0, 1] # Result with smallest distance
    second_result = distances_classes[1, 1] # Result with second smallest distance

    if (first_result == second_result): # If both distances belong to the same class
        print("The sample most likely belongs to class {0}".format(first_result))
    else:
        print("Result uncertain.")

print(distances_classes)