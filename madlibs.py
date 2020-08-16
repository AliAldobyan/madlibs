def main():
	# write your code here
	print("Mad libs where libs get mad." + "\nStart below:\n")
	number = input("Enter a number from 1 to 12: ")
	noun = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	sentence = input("Enter any sentence: ")
	verb = input("Enter a verb: ")

	print("\n\nThe story goes...\n\n")

	print("It was %s o'clock when I heard a knock at the door." % (number))
	print("I opened the door and there was a box full of %s with a note saying \"From Mr. %s.\"" % (noun,name.title()))
	print("Just as I closed the door I heard a scream \"%s.\"" %(sentence.upper()))
	print("I froze in place and all I could do was %s." %(verb))











if __name__ == "__main__":
	main()
