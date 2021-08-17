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
    try:
        following_list = []
        with open(f'{target}_following.txt') as f:
            for line in f:
                following_list.append(line.strip())
        print(f'[ OK ] Following list loaded from file')
    except FileNotFoundError:
        print(f'[ OK ] Following list not found. Creating new file')
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
    followingCount = len(following_list)

    # Retrieve in a list the followers of the user
    try:
        followers_list = []
        with open(f'{target}_followers.txt') as f:
            for line in f:
                followers_list.append(line.strip())
        print(f'[ OK ] Followers list loaded from file')
    except FileNotFoundError:
        print(f'[ OK ] Followers list not found. Creating new file')
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

    # print('Estimated time: ')


    ## Aux code
    wholist = []
    with open('wholist.txt', 'r') as f: # Already scanned that does not follow me backup
        for line in f:
            wholist.append(line.strip())
    # Add the users from who.txt to the wholist without duplicates
    with open('who.txt', 'r') as f: # Already scanned that does not follow me 
        for line in f:
            if line.strip() not in wholist:
                wholist.append(line.strip())
    with open('whoyes.txt', 'r') as f: # Already scanned that indeed follow me 
        for line in f:
            wholist.append(line.strip())

    # Remove from following list the users that are in the wholist and who.txt
    following_list = [user for user in following_list if user not in wholist]

    print(f'[ ! ] Following list updated: {len(wholist)} users removed')


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
                    print(f'[ ! ] {counter + len(wholist)} / {followingCount} Found user {user}')
                    whois.append(user)
                    with open('who.txt', 'a') as f:
                        f.write(user + '\n')
                else:
                    print(f'[ - ] {counter + len(wholist)} / {followingCount} ...')
                    with open('whoyes.txt', 'a') as f:
                        f.write(user + '\n')
            else:
                print(f'[ ! ] {counter + len(wholist)} / {followingCount} Retrieved user {user}')
                with open('who.txt', 'a') as f:
                    f.write(user + '\n')

        except QueryReturnedNotFoundException:
            print(f'[ ! ] {counter + len(wholist)} / {followingCount} Not Found user {user}')
            continue

    end = time.time()
    elapsed = round(end - start, 4)
    print(f'\n\n[ ++ ] Elapsed Time: {elapsed}s')
    print(f'[ OK ] {len(whois)} users found!')
    print(f'[ OK ] Writing to file completed!')
    

def main():
    # Get credentials
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    try:
        who(username, password)
    except KeyboardInterrupt:
        print('\n[ ! ] Script interrupted by user')
        exit()
    
if __name__ == '__main__':
    main()
