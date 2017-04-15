# Uses python3
import sys
import numpy as np

# def get_optimal_value(capacity, weights, values):
#     value = 0.    
#     weighted_values = values/weights

#     while capacity > 0:
#     	if max(weighted_values) <= 0:
#     		break

#     	item = np.argmax(weighted_values)

#     	if weights[item] <= capacity:
#     		value += values[item]
#     		capacity -= weights[item]

#     		values[item] = 0
#     		weights[item] = 0
#     		weighted_values[item] = 0

#     	else:
#     		fraction_used = capacity/weights[item]

#     		value += values[item]*fraction_used
#     		capacity = 0

#     		values[item] -= values[item]*fraction_used
#     		weights[item] -= weights[item]*fraction_used
#     		# weighted_values[item] = 

#     return value

def get_optimal_value(capacity, weights, values):
	total_value = 0
	total_weight = 0

	weighted_values = values/weights
	order = weighted_values.argsort()[::-1]

	weighted_values = weighted_values[order]
	weights = weights[order]
	values = values[order]

	num_items = 0

	while (total_weight < capacity and len(weights) > 0):

		if weights[0] <= (capacity - total_weight):
			total_value += values[0]
			values = values[1:]

			total_weight += weights[0]
			weights = weights[1:]

			num_items += 1

		else:
			fraction_used = (capacity - total_weight)/weights[0]

			total_value += values[0]*fraction_used
			total_weight += weights[0]*fraction_used

			values[0] -= values[0]*fraction_used
			weights[0] -= weights[0]*fraction_used

	return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = np.array(data[2:(2 * n + 2):2])
    weights = np.array(data[3:(2 * n + 2):2])
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
