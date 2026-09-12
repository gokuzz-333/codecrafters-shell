import sys
import shutil,subprocess,os
def execute_command(c):
    for d in os.get_exec_path():
        if os.access(fullpath:=os.path.join(d,c),os.X_OK):
            return fullpath

        
def builtin_commands(c):
    return c in {"echo","exit","type"}


def main():
    while True:
        sys.stdout.write("$ ")
        command=input().strip()
        if not command:
            continue

        parts=command.split()
        cmd=parts[0]
        args=parts[1:] if len(parts)>1 else ""

        if builtin_commands(cmd):
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
        elif execute_command(cmd):
            subprocess.run(parts)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
