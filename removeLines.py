import os
import time

start_time = time.time()
makeBackup = False


def listDir(path):
	files = []
	for dirname, dirnames, filenames in os.walk(path):        
		for filename in filenames:
			dir = os.path.join(dirname, filename)
			files.append(dir)
	files.sort()
	return files
	
	
def processFile(fileName, words):
	with open(fileName, "r") as f:
		items = f.readlines()
	
	if makeBackup:
		fileName = fileName + '-after'
		
	with open(fileName, "w") as f:
		index = len(items)-1
		while index > 1 :
			line = items[index].strip("\n")
			for wordLine in words:
				word = wordLine[0]
				removePrev = wordLine[1]
				removeNext = wordLine[2]
				if word in line:
					removingFrom = index - removePrev
					removingTo = index + removeNext + 1	
					del items[removingFrom:removingTo]
			index -= 1
			
		for item in items:
			f.write(item)


#profiles
profileList = listDir("c:\\Data\\profiles\\")

profileWordsToRemove = []
profileWordsToRemove.append(['<name>SendExternalEmailAvailable</name>', 2, 1])
profileWordsToRemove.append(['<name>CreateReductionOrder</name>', 2, 1])
profileWordsToRemove.append(['<recordType>Case.SampleRecordType1</recordType>', 2, 2])
profileWordsToRemove.append(['<field>Contact.SampleField__c</field>', 2, 2])
profileWordsToRemove.append(['<apexClass>SampleApexClass</apexClass>', 1, 2])

for fileName in profileList:
	processFile(fileName, profileWordsToRemove)
	

# permission sets
permSetList = listDir("c:\\Data\\permissionsets\\")
permSetWordsToRemove = []
permSetWordsToRemove.append(['<field>Account.CustomTextField__c</field>', 2, 2])
permSetWordsToRemove.append(['<field>Lead.CustomField__1c</field>', 2, 2])

for fileName in permSetList:
	processFile(fileName, permSetWordsToRemove)

permSetList = listDir("c:\\Data\\permissionsets\\")
permSetWordsToRemove = []
permSetWordsToRemove.append(['<field>Account.CustomTextField__c</field>', 2, 2])
permSetWordsToRemove.append(['<field>Lead.CustomField__1c</field>', 2, 2])

for fileName in permSetList:
	processFile(fileName, permSetWordsToRemove)

	
# show execution time
print("--- %s seconds ---" % (round(time.time() - start_time, 2)))
