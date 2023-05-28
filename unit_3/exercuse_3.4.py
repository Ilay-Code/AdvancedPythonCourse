import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, character, position):
        self.character = character
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.character}' at position {self.position}"


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username must be at least 3 characters long"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username must be at most 16 characters long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password must be at least 8 characters long"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password must be at most 40 characters long"


class MissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class MissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class MissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class MissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    # Check username
    if not all(ch.isalnum() or ch == "_" for ch in username):
        for i, ch in enumerate(username):
            if not ch.isalnum() and ch != "_":
                raise UsernameContainsIllegalCharacter(ch, i)
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    # Check password
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()
    if not any(ch.isupper() for ch in password):
        raise MissingUppercase()
    if not any(ch.islower() for ch in password):
        raise MissingLowercase()
    if not any(ch.isdigit() for ch in password):
        raise MissingDigit()
    if not any(ch in string.punctuation for ch in password):
        raise MissingSpecial()

    print("OK")


def main():
    while True:
        try:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
                PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
            print(e)


if __name__ == "__main__":
    main()
