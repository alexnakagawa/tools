// Document Traversal and Grouping
d3.select("body") = $("body")
d3.selectAll(".block") = $(".block")

// Stringing Together
d3.select("body")
	.selectAll("p")
		.data(["hello", "hi", "yo", "hey", "hola", "what's up", "why"])
		.enter()
		.append()

// Reading in the dataset
d3.csv("example.csv")
d3.json("example.json")

// 

