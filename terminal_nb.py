import os 

if __name__ == "__main__":
    while True:
        cmd = str(input('> ')).split(' ') 
        os.execvp(cmd[0], cmd[1:]) 

