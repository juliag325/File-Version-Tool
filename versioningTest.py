import maya.cmds as cmds 
import maya.mel as mel 
import sys 

def run(): 
	
	# Basic path information
	path = cmds.file (q =1, sn = 1) # This is our path! 
	name = path.split('/')[-1]
	direct = path.replace(name, '')

	num = name.split('_')[-1]
	num = num.replace('.ma','')
	digits = len(num)
	print digits

	newNum = int(num) + 1
	print newNum
	newDigits = len(str(newNum))
	print newDigits

	for i in range(digits - newDigits): 
		newNum = '0{}'.format(newNum)


	newName = name.replace(num, newNum)
	print newName

	fileSave = cmds.file (rn = path.replace(name,newName))
	cmds.file (save = 1)

	sys.stdout.write ('Saved {}'.format (fileSave))