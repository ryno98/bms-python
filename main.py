import sys

balance = 20
amount = 10

with open("account.txt", "w") as f:
	f.write("Adding line to file.")

def create_account():
	username = input("Please Enter A Username: ")
	password = input("Please Enter A Password: ")

	with open("{}.txt".format(username), "w") as f:
		f.write("{} {}".format(username, password))

def login():
	username = input("Username: ")
	password = input("Password: ")

	with open("{}.txt".format(username), "r") as f:
		pin = f.readline().split(" ")[1]

	if password != pin:
		print("Incorrect Password.")

def deposit(balance, amount):
	balance += amount
	return balance

def withdraw(balance, amount):
	balance -= amount
	return balance

def transfer(balance, amount, account):
	balance -= amount
	#account.balance += amount
	return balance

def check_balance():
	return balance

def main():
	login()

if __name__ == '__main__':
	main()

#file = open("account.txt", "r")
#print(file.read())