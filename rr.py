from cryptography.fernet import Fernet, MultiFernet
def Algo1_extented(filename, key1, key2):
	f = MultiFernet([Fernet(key1),Fernet(key2)])
