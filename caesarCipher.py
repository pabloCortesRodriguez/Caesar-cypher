class Encryption:

    abc = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 _:=.+')

    def __init__(self, path, difference):
        self.file = open(path, 'r')
        self.difference = difference
        self.result = []
        self.encrypt_letters = {}
        self.decrypt_letters = {}

    def encrypt(self):
        for line in self.file.readlines():
            line = line.replace(' ', '+')
            if '*' in line:
                self.result.append(line)
            else:
                encrypted_line = ''
                for letter in line:
                    if letter in self.encrypt_letters:
                        try:
                            encrypted_line += self.encrypt_letters[letter]
                        except:
                            print(letter)
                    else:
                        encrypt_letter = self.change_letter(letter, 1)
                        if encrypt_letter is not None:
                            self.encrypt_letters[letter] = encrypt_letter
                            self.decrypt_letters[encrypt_letter] = letter
                            try:
                                encrypted_line += str(self.encrypt_letters[letter])
                            except Exception as e:
                                print(letter)

                encrypted_line = '*' + encrypted_line
                self.result.append(encrypted_line)
        self.file.close()
        self.save()

    def decrypt(self):
        for line in self.file.readlines():
            if '*' in line:
                line = line.strip('*')
                decrypted_line = ''
                for letter in line:
                    # decrypted_line += change_letter(letter, -1)
                    if letter in self.decrypt_letters:
                        decrypted_line += self.decrypt_letters[letter]
                    else:
                        decrypt_letter = self.change_letter(letter, -1)
                        if decrypt_letter is not None:
                            self.decrypt_letters[letter] = decrypt_letter
                            self.encrypt_letters[decrypt_letter] = letter
                            try:
                                decrypted_line += self.decrypt_letters[letter]
                            except Exception as e:
                                print(letter)

                decrypted_line = decrypted_line.replace('+', ' ')
                self.result.append(decrypted_line)
            else:
                self.result.append(line)
        self.file.close()
        self.save()

    def change_letter(self, letter, x):
        # If x = 1 encrypt, if x = -1 decrypt
        n = self.difference * x
        for i in range(len(self.abc)):
            if self.abc[i] == letter:
                i += n
                if i > len(self.abc)-1:
                    i -= len(self.abc)
                    return self.abc[i]
                if i < 0:
                    i += len(self.abc)
                    return self.abc[i]
                else:
                    return self.abc[i]

    def save(self):
        self.file = open(path, 'w')
        for line in self.result:
            self.file.write(line+'\n')
        return self.result



if __name__ == '__main__':
    string = str(input('encrypt -> e \ndecrypt -> d \n->'))
    path = '/home/pablo/Documentos/passwords.txt'
    encryption = Encryption(path,4)
    if string == 'e':
        encryption.encrypt()
    elif string == 'd':
        encryption.decrypt()
    else:
        print('Error')
