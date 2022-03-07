def caesarCipherEncryptor(string, key):
    res= ''
	for i in string:
		newChar = ( ord(i) - ord('a') + key ) % 26 + ord('a')
		res += chr(newChar)
	return res
		