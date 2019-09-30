

def maze():
	coord1_input = ""
	coord2_input = ""
	curloc_input = ""
	target_input = ""
	coord1 = None
	coord2 = None
	coordpair = None
	curloc = None
	target = None

	# Valid coordinate pairs for indicators
	valid_pairs = {
		((1,5),(6,4)),
		((2,3),(5,5)),
		((4,3),(6,3)),
		((1,3),(1,6)),
		((4,1),(5,4)),
		((3,2),(5,6)),
		((2,1),(2,6)),
		((3,3),(4,6)),
		((1,2),(3,5))
	}

	# Valid individual coordinates for indicators
	valid_inputs = {
		(1,5),(6,4),
		(2,3),(5,5),
		(4,3),(6,3),
		(1,3),(1,6),
		(4,1),(5,4),
		(3,2),(5,6),
		(2,1),(2,6),
		(3,3),(4,6),
		(1,2),(3,5)
	}

	def coord_validation(input_coord):
		if input_coord.count(",") > 1 or "," not in input_coord:
			print("Error: Incorrect coordinate formatting.")
			return 0
		x, y = input_coord.replace(" ", "").split(",")
		if not x.isnumeric() or not y.isnumeric() or int(x) > 6 or int(x) < 1 or int(y) > 6 or int(y) < 1:
			print("Error: x or y coordinate is not a valid integer or it is not within range")
			return 0
		return (int(x), int(y))

	while coordpair not in valid_pairs:

		# Take input for first coordinate pair
		while coord1 not in valid_inputs:
			coord1_input = input("What is the first indicator coordinate: ")
			coord1 = coord_validation(coord1_input)
			if coord1 == 0: # Returned error
				continue
			if coord1 not in valid_inputs:
				print("Error: Cooridinate does not match any existing mazes. Try again.")

		# Take input for second coordinate pair
		while coord2 not in valid_inputs:
			coord2_input = input("What is the second indicator coordinate: ")
			coord2 = coord_validation(coord2_input)
			if coord2 == 0: # Returned error
				continue
			if coord2 not in valid_inputs:
				print("Error: Cooridinate does not match any existing mazes. Try again.")

		# Check both combinations of coordinate pairs with valid mazes
		coordpair = (coord1, coord2)
		if coordpair in valid_pairs:
			print("Valid coordinate pair! Continuing ...")
		else:
			coordpair = (coord2, coord1)
			if coordpair in valid_pairs:
				print("Valid coordinate pair! Continuing ...")
				break # Unnecessary but we'll keep it in for now.
			else:
				print("Error: Coorinate pair does not match any existing mazes. Try again.")

	# At this point, the maze should be chosen and decided upon

	curloc_valid = False
	while not curloc_valid:
		curloc_input = input("What is the coordinate of current location: ")
		curloc = coord_validation(curloc_input)
		if curloc == 0:
			continue
		else:
			break

	target_valid = False
	while not target_valid:
		target_input = input("What is the coordinate of current location: ")
		target = coord_validation(target_input)
		if target == 0:
			continue
		else:
			break