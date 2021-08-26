# WHO does not follow you back
# Developed by: @CxrlosKenobi
# # # # # # # # # # # # # # # # 

# Script that return the users that do not follow your instagram account, but you do follow.
from instaloader.exceptions import QueryReturnedNotFoundException
from colorama import Fore, Back, Style
import OAuthLogInto as Auth
import instaloader
import time

def who(username, password):
    L = instaloader.Instaloader()
    L.login(username, password)
    target = username

    profile = instaloader.Profile.from_username(L.context, target)
    print(Fore.GREEN + '[ OK ]' + Style.RESET_ALL + ' Starting process ...')

    # Retrieve in a list the following of the user
    try:
        following_list = []
        with open(f'{target}_following.txt') as f:
            for line in f:
                following_list.append(line.strip())
        print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + 'Following list loaded from file')
    except FileNotFoundError:
        print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + 'Following list not found. Creating new file')
        start = time.time()
        following = profile.get_followees()
        following_list = [f.username for f in following]
        with open(f'{target}_following.txt', 'w') as f:
            for user in following_list:
                f.write(user + '\n')
        end = time.time()
        elapsed = round(end - start, 4)
        print(Fore.GREEN + '[ ++ ] ' + Style.RESET_ALL + f'Elapsed Time: {elapsed}s')
        print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + f'Following list saved to {target}_following.txt')    
    followingCount = len(following_list)

    # Retrieve in a list the followers of the user
    try:
        followers_list = []
        with open(f'{target}_followers.txt') as f:
            for line in f:
                followers_list.append(line.strip())
        print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + 'Followers list loaded from file')
    except FileNotFoundError:
        print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + 'Followers list not found. Creating new file')
        start = time.time()
        followers = profile.get_followers()
        followers_list = [f.username for f in followers]
        with open(f'{target}_followers.txt', 'w') as f:
            for user in followers_list:
                f.write(user + '\n')
        end = time.time()
        elapsed = round(end - start, 4)
        print(Fore.GREEN + '[ ++ ] ' + Style.RESET_ALL + f'Elapsed Time: {elapsed}s')
        print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + f'Followers list saved to {target}_followers.txt')

    ## Aux code
    retrieved = []
    # Add the users from who.txt to the retrieved without duplicates
    try:
        with open('who.txt', 'r') as f: # Already scanned that does not follow me 
            for line in f:
                if line.strip() not in retrieved:
                    retrieved.append(line.strip())
        with open('whoyes.txt', 'r') as f: # Already scanned that indeed follow me 
            for line in f:
                retrieved.append(line.strip())
    except FileNotFoundError:
        pass

    # Remove from following list the users that are in the retrieved and who.txt
    following_list = [user for user in following_list if user not in retrieved]
    print(Fore.YELLOW + '[ ! ] ' + Style.RESET_ALL + f'Updating following list in case of retrieved users: {len(retrieved)} users retrieved')

    # Iterate each username in following list
    whois = []
    print(Fore.GREEN + '[ OK ] ' + Style.RESET_ALL + 'Starting process ...')
    counter = 0
    start = time.time()
    for user in following_list:
        try:
            counter += 1
            if user not in retrieved:
                profile = instaloader.Profile.from_username(L.context, user)
                following = profile.get_followees()
                following_list = [f.username for f in following]
                if target not in following_list:
                    print(Fore.CYAN + '[ ! ] ' + Style.RESET_ALL + f'{counter + len(retrieved)} / {followingCount} Found user' + Fore.CYAN + f' {user}' + Style.RESET_ALL)
                    whois.append(user)
                    with open('who.txt', 'a') as f:
                        f.write(user + '\n')
                else:
                    print(f'[ - ] {counter + len(retrieved)} / {followingCount} ...')
                    with open('whoyes.txt', 'a') as f:
                        f.write(user + '\n')
            else:
                print(Fore.CYAN + '[ ! ] ' + Style.RESET_ALL + f'{counter + len(retrieved)} / {followingCount} Retrieved user {user}')
                with open('who.txt', 'a') as f:
                    f.write(user + '\n')

        except QueryReturnedNotFoundException:
            print(Fore.RED + '[ ! ] ' + Style.RESET_ALL + f'{counter + len(retrieved)} / {followingCount} Not Found user {user}')
            continue

    end = time.time()
    elapsed = round(end - start, 4)
    print(Fore.GREEN + '\n\n[ ++ ] ' + Style.RESET_ALL + f'Elapsed Time: {elapsed}s')
    print(Fore.GREEN + '[ OK ]' + Style.RESET_ALL + f'{len(whois)} users found!')
    print(Fore.GREEN + '[ OK ]' + Style.RESET_ALL + 'Writing to file completed!')

def main():
    try:
        username, password = Auth.login()
        who(username, password)
        print(Fore.YELLOW + '[ - ] ' + Style.RESET_ALL + 'Logging in ...')
    except KeyboardInterrupt:
        print(Fore.YELLOW + '\n\n[ ! ]' + Style.RESET_ALL + ' Script interrupted by user')
        exit()
    
if __name__ == '__main__':
    main()
