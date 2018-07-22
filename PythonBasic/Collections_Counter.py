'''
Input Format

The first line contains X, the number of shoes. 
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers. 
The next N lines contain the space separated values of the shoe size desired by the customer and x(i), the price of the shoe.

Output Format

Print the amount of money earned by Raghu.

Sample Input:

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output:

200

Explanation

Customer 1: Purchased size 6 shoe for $55. 
Customer 2: Purchased size 6 shoe for $45. 
Customer 3: Size 6 no longer available, so no purchase. 
Customer 4: Purchased size 4 shoe for $40. 
Customer 5: Purchased size 18 shoe for $60. 
Customer 6: Size 10 not available, so no purchase.

Total money earned =  55 + 45 + 40 + 60 = $200
'''

from collections import Counter

if __name__ == "__main__":
    X = int(input().strip())
    shoe_lst = list(map(int, input().split()))
    N = int(input().strip())
    
    total = 0
    shoe_dict = Counter(shoe_lst)
    for _ in range(N):
        k,p = map(int, input().split())
        if shoe_dict[k] > 0:
            shoe_dict[k] -= 1
            total += p
    
    print(total)






