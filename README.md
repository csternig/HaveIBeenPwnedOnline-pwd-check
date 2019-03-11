# HaveIBeenPwnedOnline-pwd-check
Search the password list from https://haveibeenpwned.com/Passwords online to avoid the large download (12 GB file). 
To improve trustability all password related inputs are processed locally on your machine. Only the SHA1 hash of your password
gets transmitted encrypted to Have I Been Pwned.

## Usage
Start the program with
```shell
python online_search.py
```

After that enter your password and press Enter. The program will display your password SHA1-hash and the quantity of hits. 

A hit means that your password is included in leaked credentials --> **you should change your password!** For further information check https://haveibeenpwned.com/

To exit the program simply press Enter without entering a password.
## Requirements 
```shell
pip install requests
```
