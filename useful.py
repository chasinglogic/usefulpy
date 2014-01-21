#!/usr/bin/python

# This script extracts the ids from an html file and adds them to the top of any other text file as a
# block comment that is valid in CSS or JavaScript.

import sys

# I guess I should start with duck typing scares me.

#function junction
def extractIds(lines):
	ids = ["\nID'S:"]
	for li in lines:
		ids.append('\t' + li.partition('id="')[-1].partition('"')[0])
	return ids

# def extractClasses(lines):
# 	classes = ["CLASSES:\n\n"]
# 	for li in lines:
# 		classes.append(li.partition('class="')[-1].partition('"')[0])
# 	return classes

def findHits(filename, what):
	with open(filename, "r") as source:
		hits = []
		for line in source:
			# Finds all occurrences of id= and returns those lines
			if line.find(what) != -1:
				hits.append(line)

		return hits

# Patent Prepending* TM
def patentPrepending(filename):
	# just nabs all the text that was already there.
	with open(filename, "r") as f:
		origin = f.read()
		return origin

# This will find the ids that were already there, we are going to only check
# anywhere between the first set of /* */ comments though because it could get nasty
# if we don't add an id to the top of the file just because you mention it elsewhere.
def findDuplicates(text, ids):
	dupes = []
	workingText = text[text.find("/*")+1 : text.find("*/")]
	for i in ids:
		if i in workingText:
			dupes.append(i)
	# tuples ftw
	if len(dupes) != 0:
		return dupes, True
	else:
		return dupes, False

def removeDuplicates(dupes, ids):
	newIds = ids
	for dup in dupes:
		newIds.remove(dup)		

	return newIds

def writeIdsToFile(filename, ids):
	# We have to read the entire file into memory so we can 
	# "fake" prepend to the file since there is no easy or safe
	# way to do this.
	originalText = patentPrepending(filename)
	# find duplicates if there are any in the original text.
	dupes, dupesyes = findDuplicates(originalText, ids)
	# if we find dupes then remove them otherwise keep living life.
	if dupesyes:
		newIds = removeDuplicates(dupes, ids)
	# This is a little weird but it was the best solution I came up with. Feel free to make me look like an idiot.
	else:
		newIds = ids
	# if there are no newIds (i.e. everything already existed or for some god awful reason no ids existed in the html) 
	# we don't want to write at all.	
	if len(newIds) > 0:
		# Writes all ids as a block comment to target file
		with open(filename, "w") as target:
			target.write("/*")
			for names in newIds:
				target.write(names + '\n')
			target.write("*/\n\n")
			target.write(originalText)
			return True

def main():
	if len(sys.argv) != 3:
		print("Try python useful.py file.html targetFile1")
		print("or useful sourceFile.html targetFile1 if you're fancy.")
		sys.exit("Incorrect Usage")

	sourceFile = sys.argv[1]
	targetFile = sys.argv[2]
	# hits holds all the lines that contain id=
	idHits    = findHits(sourceFile, "id=")
	# classHits = findHits(sourceFile, "class=")
	# ids holds all the ids from the html file.
	ids     = extractIds(idHits)
	# classes = extractClasses(classHits)
	# this will write the ids in the form of a comment
	# to the top of our css or js file.
	success = writeIdsToFile(targetFile, ids)

	if success:
		print("Done completed successfully")
	else:
		print("Done but there were errors.")

main()