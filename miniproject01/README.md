Objective: 
	• Allow the user to select from a list of 3 states and generate a road trip itinerary from the selected state.

	1) Region selection
		○ Provide a list of the regions in the input prompt
		○ Include the states included in that region in the input prompt
		a) Request user provide input
			i. Errors
				1) Input did not match a region
				2) User did not provide an input
				3) Input is not of data type string
	2) City selection
		○ First, list all the cities in the region with a description of each city. 
		a) Request user to select three of those cities to build an itinerary. 

Finally, export that itinerary to the user in an easy-to-read format. 