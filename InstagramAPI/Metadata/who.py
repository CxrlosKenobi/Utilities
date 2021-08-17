# WHO does not follow you back
# Developed by: @CxrlosKenobi
# # # # # # # # # # # # # # # # 

# Script that return the users that do not follow your instagram account, but you do follow.
import instaloader
import getpass
import time

from instaloader.exceptions import QueryReturnedNotFoundException


def who(username, password):
    L = instaloader.Instaloader()
    L.login(username, password)
    target = username

    profile = instaloader.Profile.from_username(L.context, target)
    print('[ OK ] Starting process ...')

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
    
    followingCount = []
    with open(f'{target}_following.txt', 'r') as f:
        for line in f:
            followingCount.append(line.strip())
    
    # print('Estimated time: ')
    ## Aux code
    # Read the wholist.txt and pass it to a list
    wholist = []
    with open('wholist.txt', 'r') as f:
        for line in f:
            wholist.append(line.strip())
    # Remove from following list the users that are in the wholist
    aux = 0
    for user in following_list:
        if user in wholist:
            aux += 1
            following_list.remove(user)
    print(f'[ ! ] Following list updated: {aux} users removed')


    # Iterate each username in following list
    whois = []
    print('[ OK ] Starting process ...')
    counter = 0
    start = time.time()
    for user in following_list:
        try:
            counter += 1
            if user not in wholist:
                profile = instaloader.Profile.from_username(L.context, user)
                following = profile.get_followees()
                following_list = [f.username for f in following]
                if target not in following_list:
                    print(f'[ ! ] {counter} / {followingCount} Found user {user}')
                    whois.append(user)
                    with open('wholist.txt', 'a') as f:
                        f.write(user + '\n')
                else:
                    print(f'[ - ] {counter} / {followingCount} ...')
            else:
                print(f'[ ! ] {counter} / {followingCount} Retrieved user {user}')
                with open('wholist.txt', 'a') as f:
                    f.write(user + '\n')

        except QueryReturnedNotFoundException:
            print(f'[ ! ] {counter} / {followingCount} Not Found user {user}')
            continue

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
