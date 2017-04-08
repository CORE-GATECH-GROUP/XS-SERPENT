"""
- Burnup block writer
	- Input:
		- string denoting burnup structure
			- 'burn <btype> [sequence of floats/patterns]'
			- e1. 'burn bustep 0.2 0.4 0.5R6 0.75R2'
			- e2. 'burn daytot 1 5 10 25 50'
			- <btype> will be a valid SERPENT burnup type (see manual)
	- Output:
		- string with the correct SERPENT style burnup structure
		- the syntax 'xRy' should be a flag to repeat the preceeding x y times (where y is an integer)
			- 0.5R6 -> 0.5 0.5 0.5 0.5 0.5
			O.e1. dep bustep
			            0.2
			            0.4
			            0.5
			            ..
            O.e2. dep daytot
                        1
                        5
                        10
                        25
                        50

            I.e3. burn badburn 0.1 0.2 ....
            O.e3. <FATAL ERROR> no badburn in SERPENT syntax
"""


inputStr = 'burn daytot 1 5 10 25 50'

burnupTypes = ['bustep', 'butot', 'daystep', 'daytot', 'decstep', 'dectot']
splittedString = str.split(inputStr)
if splittedString[0]=='burn':
    if splittedString[1] in burnupTypes:
        print('dep ', splittedString[1])

        for i in range(2, len(splittedString)):

            if 'R' in splittedString[i]:
                 splittedChar = splittedString[i].split('R')
                 for j in range(0, int(splittedChar[1])):
                     print(splittedChar[0])
            elif any(c.isalpha() for c in splittedString[i]):
                print('ERROR')
            else:
                print(splittedString[i])
    else:
        print('ERROR')

else:
    print('ERROR')
