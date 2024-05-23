# name: str = input("Enter your name: ")
# print(f'WITAJ {name}')

data_of_users: list = [
    {'name': 'Kacper', 'surname': 'Skrzypczak', 'posts': 5, 'location': 'Hrubieszów'},
    {'name': 'Julia', 'surname': 'Szklarzewska', 'posts': 15, 'location': 'Hajnówka'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 8, 'location': 'Rzeszów'},
    {'name': 'Sebastian', 'surname': 'Dudek', 'posts': 12, 'location': 'Siedlce'},
]
print(f'WITAJ {data_of_users[0]["name"]}')


def read(users: list) -> None:
    """
    this is a function to show users from an list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'twój znajomy: {user['name']}, opublikował: {user["posts"]}')


read(data_of_users)
