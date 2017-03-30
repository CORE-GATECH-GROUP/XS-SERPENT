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
