# Python program to remove punctuation from a given string
# Function to remove punctuation
def Punctuation(string):


	# punctuation marks
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


	# traverse the given string and if any punctuation
	# marks occur replace it with null
	for x in string.lower():
		if x in punctuations:
			string = string.replace(x, "")


	# Print string without punctuation
	print(string)


# Driver program
string = "hello, Hello, H’ello, He-LLo"
Punctuation(string)