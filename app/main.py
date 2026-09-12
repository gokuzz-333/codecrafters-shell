import sys
import shutil

def main():
    while True:
        sys.stdout.write("$ ")
        command=input()
        cmd=command[5:]
        if command=="exit":
            break
        elif command.startswith("echo"):
            print(command[5:])
        elif command.startswith("type"):
            if cmd in ["echo","type","exit"]:
                print(f"{cmd} is a shell builtin")
            elif path:= shutil.which(cmd):
                print(f"{cmd} is {path}")
            else:
                print(f"{cmd} not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
