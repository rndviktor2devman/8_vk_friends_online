import vk
import getpass


APP_ID = 5653670


def get_user_login():
    login = input("Enter your login")
    return login


def get_user_password():
    password = getpass.getpass("Enter your password")
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=2
    )

    api = vk.API(session)
    id_friends_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=id_friends_online)
    return friends_online


def output_friends_to_console(friends_online):
    print("These friends are online now:")
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
