import matplotlib.pyplot as plt

def hide_object(img , i , j) :
	"""function to darken (black) the visited part of image, so that it is not counted again.

	Parameters
	----------
	img : 2D numpy array
		input image which need to be darken for a object
	i : int
		row index lying in the object (i.e. white)
	j : int
		column index lying in the object (i.e. white)
	"""
	stack = [(i,j)]                                             # stack for DFS traversal

	possible_dir = [(-1,0) , (1,0) , (0,1) , (0,-1)]            # possible direction are the

	while(len(stack) > 0) :
		u = stack.pop()
		img[u[0]][u[1]] = 0										# darkening it ( 1 --> 0 )

		for directions in possible_dir :                        # iterating in the possible directions
			if(img.shape[0] > u[0] + directions[0] >= 0 and img.shape[1] > u[1] + directions[1] >= 0 and img[u[0] + directions[0]][u[1] + directions[1]] == 1) :
				# if the index is valid and the pixel at that index is white
				# the we need to darken it
				stack.append((u[0] + directions[0],u[1] + directions[1]))

def number_of_objects(img) -> int :
	"""function to find number of white objects in the black background image

	Parameters
	----------
	img : 2D numpy array
		input image

	Returns
	-------
	int
		number of white objects in the image
	"""
	objects_counter = 0											# starting object counter

	for i in range(img.shape[0]) :
		for j in range(img.shape[1]) :
			if(img[i][j] == 1) :                				# white pixel of a object is found
				objects_counter += 1							# one more object is found
				hide_object(img , i , j)						# need to hide all other white pixels of this object
	
	return objects_counter			

if __name__ == "__main__":
	img = plt.imread('test.png')        					# reading the image

	# assuming the image is already binarized (i.e. black and white) and black is background
	
	print('Number of objects in input images is' , number_of_objects(img))
	
