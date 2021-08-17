# WHO does not follow you back
# Developed by: @CxrlosKenobi
# # # # # # # # # # # # # # # # 

# Script that return the users that do not follow your instagram account, but you do follow.
import instaloader
import getpass
import time


def who(username, password):
    L = instaloader.Instaloader()
    L.login(username, password)
    target = username

    profile = instaloader.Profile.from_username(L.context, target)
    print('[ ok ] Starting process ...')

    # Retrieve in a list the following of the user
    start = time.time()
    following = profile.get_followees()
    following_list = [f.username for f in following]
    with open(f'{target}_following.txt', 'w') as f:
        for user in following_list:
            f.write(user + '\n')
    end = time.time()
    elapsed = round(end - start, 4)
    print(f'[ ++ ] Elapsed Time: {elapsed}s')
    print(f'[ OK ] Following list saved to {target}_following.txt')
    
    # Retrieve in a list the followers of the user
    start = time.time()
    followers = profile.get_followers()
    followers_list = [f.username for f in followers]
    with open(f'{target}_followers.txt', 'w') as f:
        for user in followers_list:
            f.write(user + '\n')
    end = time.time()

    elapsed = round(end - start, 4)
    print(f'[ ++ ] Elapsed Time: {elapsed}s')
    print(f'[ OK ] Followers list saved to {target}_followers.txt')
    
    with open(f'{target}_following.txt', 'r') as f:
        followingCount = len(f.readlines())

    # print('Estimated time: ')
    
    # Iterate each username in following list
    whois = []
    print('[ OK ] Starting process ...')
    counter = 0
    start = time.time()
    for user in following_list:
        counter += 1
        profile = instaloader.Profile.from_username(L.context, user)
        following = profile.get_followees()
        following_list = [f.username for f in following]
        if target not in following_list:
            print(f'[ ! ] {count} / {followingCount} Found user {user}')
            whois.append(user)
        else:
            print(f'[ - ] {count} / {followingCount} ...')

    end = time.time()
    elapsed = round(end - start, 4)
    print(f'\n\n[ ++ ] Elapsed Time: {elapsed}s')
    print(f'[ OK ] {len(whois)} users found!')

    print(f'[ ! ] Writing to file ...')
    with open(f'{target}_whois.txt', 'w') as f:
        for user in whois:
            f.write(user + '\n')
    print(f'[ OK ] Writing to file completed!')
    

def main():
    # Get credentials
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    who(username, password)

if __name__ == '__main__':
    main()
