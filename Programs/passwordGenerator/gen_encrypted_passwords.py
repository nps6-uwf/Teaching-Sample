# gen_encrypted_passwords.py
# Name: 
# Id: 

# [] 0 Use construct_password function from gen_pw module.
#     0a) Ask user to enter n # of students.
#     0b) Loop n times, asking user to enter student name each time.
#     0c) Create a password for each user.
#     0d) Write password to csv file named passwords.csv
# ............................................


# [] 1 Create encryption algorithm
#      1a) Caesar cipher OR
#      1b) Xor encryption OR
#      1c) Vigenere cipher 
# ............................................

# [] 2 Encrypt passwords before storing to file
#      2a) Generate a random key.
#      2b) Use random key to encrypt each password.
#      2c) Store password in passwords.csv.
#      2d) Store encryption keys in keys.pickle
# ............................................

# [] 3 Create new file: verify.py
#      3a) Ask user to enter name and password.
#      3b) If password is correct print.  "Welcome {namme}".
#      3c) If password is incorrect give the user 3 attempts.
#      3d) If user has not guessed the correct password after 3
#          attempts print "Security breach detected.  Account Locked."
# ............................................