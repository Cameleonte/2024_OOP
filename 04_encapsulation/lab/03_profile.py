class Profile:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value) -> None:
        if 5 < len(value) < 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value) -> None:
        is_long = len(value) >= 8
        is_upper = len([ch for ch in value if ch.isupper()]) > 0
        is_digit = len([ch for ch in value if ch.isdigit()]) > 0

        if is_long and is_upper and is_digit:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')
profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
