def bubble_sort():
	# Variables
	sorted = False

	# While we have swapped a variable...
	while not sorted:
		
		# Print our array at the current moment
		print array

		# Assume it's sorted
		sorted = True

		# For every element in the array except the last...
		for i in range(len(array) - 1):

			# If the element is larger than the one to the right of it...
			if array[i] > array[i + 1]:

				# Swap the two elements
				array[i], array[i + 1] = array[i + 1], array[i]

				# And mark that we have swapped something this pass
				sorted = False

	# Return sorted array
	return array