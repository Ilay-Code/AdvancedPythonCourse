def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    decrypted_password = ''.join(chr(ord(char) + 2) if char.isalpha() else char for char in password)
    print(decrypted_password)


if __name__ == '__main__':
    main()
