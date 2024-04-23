def func():

	class Account():

		def __init__(self,user = input("Quien esta iniciando sesion: "), database= {"jose":"josesito123","juan":"juansito123","roman":"romancito123"},shoplist = {"apple":5,"potatoe":2,"banana":10},balance = 0,obj= []):

			self.user = user

			self.database = database

			self.shoplist = shoplist

			self.balance = balance

			self.obj = obj

		def initialize(self):

			allowed1 = True

			allowed2 = True

			if self.user in self.database:

				print(f"Welcome {self.user}")

				psw = input("Now enter your password: ")

				if psw == self.database[self.user]:

					print("You can continue now")

					return True

				else:

					print("Access denied")

					allowed2 = False

					return allowed2
			else:

				print("You are not in the database")

				allowed1 = False

				return allowed1

		def modify_balance(self):

			q = input(f"Your balance is {self.balance}, what do you want to do (whithdraw or deposit): ")

			if q == "whithdraw":

				x = int(input("How much money do you want to withdraw: "))

				if self.balance =< x:

					self.balance -= x

					print(f"Your new balance is {self.balance}")

				else:

					print("You dont have enough money")

			elif q == "deposit":

				y = int(input("How much money do you want to deposit: "))

				self.balance += y

				print(f"Your new balance is {self.balance}")


		def shop(self):

			for obj,price in self.shoplist:

				print("Objeto: ")

				print(obj)

				print("Precio: ")

				print(price)

			f = input("Que objeto queres comprar: ")

			if f in self.shoplist:

				if self.balance > self.shoplist[f]:

					self.balance -= self.shoplist[f]

					self.obj.append(f)

				else:

					print("You dont have enough money")
			else:
				print("The object isnt in the shop")


	instance = Account()

	ask = " "

	while ask not in "stop":

		x = instance.initialize()

		if x == True:

			ask = input("Que queres hacer ahora: ")

		else:

			break

		if ask == "modify balance":

			instance.modify_balance()

		elif ask == "shop":

			instance.shop()

func()