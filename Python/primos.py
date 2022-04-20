from datetime import datetime
now = datetime.now()
# prime number calculator: find all primes up to n
print("---cercatore di numeri primi---")
print("")
opcion = input('vuoi inserire i dati? (s/n): ')

if opcion == 's':
		max = int(input("Fino a quale numero vuoi trovare i numeri primi?? : "))
		count = int(input("Quanti numeri primi vuoi trovare?: "))
else:
		max = 100
		count = 10



primeList = []
#for loop for checking each number
for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
print(primeList)
#-------------------------------------------------------------
# prime number calculator: find the first n primes

primeList = []
x = 2
while len(primeList) < count:
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
	if isPrime:
		primeList.append(x)
	x += 1
print(primeList)

print("fecha y hora=", now)