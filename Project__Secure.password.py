secure = (('a','@') , ('o','0') , ('and','&') , ('s','$'))

def securepasword(password):
    for a,b in secure:
        password = password.replace(a,b)
        return password


if __name__ == "__main__":
    enter = input("enter password :")
    password = securepasword(enter)

    print("your password is :" , password)