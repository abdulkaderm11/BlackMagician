'''
	Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

	Sample Input:
	9 27

	Sample Output:

	------------.|.------------
	---------.|..|..|.---------
	------.|..|..|..|..|.------
	---.|..|..|..|..|..|..|.---
	----------WELCOME----------
	---.|..|..|..|..|..|..|.---
	------.|..|..|..|..|.------
	---------.|..|..|.---------
	------------.|.------------

'''

if __name__ == "__main__":
	# common usage method
    n, m = map(int, input().split())
    
    mid = int(n/2)+1
    
    for i in range(1, mid):
        print(('.|.'*(2*i-1)).center(m,'-'))
    
    print('WELCOME'.center(m,'-'))
    
    for j in range(mid+1,n+1):
        print(('.|.'*(2*(n-j)+1)).center(m,'-'))

