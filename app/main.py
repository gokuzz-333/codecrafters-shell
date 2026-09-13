import sys
import shutil,subprocess,os
def execute_command(c):
    for d in os.get_exec_path():
        if os.access(fullpath:=os.path.join(d,c),os.X_OK):
            return fullpath

        
def builtin_commands(c):
    return c in {"echo","exit","type","pwd","cd"}

def parse_echo(text):
    result=""
    i=0
    in_quotes=False

    while i<len(text):

        if text[i]=="'":
            in_quotes=not in_quotes

        elif text[i]==" ":
            if in_quotes:
                result+=" "

            else:
                if result!="" and result[-1]!=" ":
                    result+=" "
                else:
                    result+=text[i]
                i+=1

            return result
def main():
    while True:
        sys.stdout.write("$ ")
        command=input().strip()
        if not command:
            continue

        parts=command.split()
        cmd=parts[0]
        args=parts[1:]

        if builtin_commands(cmd):
            if cmd=="exit":
                break

            elif cmd=="echo":
                text=command[5:]
                print(parse_echo(text).strip())

            elif cmd=="pwd":
                print(os.getcwd())

            elif cmd=="cd":
                try:
                    os.chdir(os.path.expanduser(args[0]))
                except FileNotFoundError:
                    print(f"cd: {args[0]}: No such file or directory")

            elif cmd=="type":
               
                if builtin_commands(args[0]):
                    print(f"{args[0]} is a shell builtin")
                elif full_path:=execute_command(args[0]):
                    print(f"{args[0]} is {full_path}")
                else:
                    print(f"{args[0]}: not found")

        elif execute_command(cmd):
            subprocess.run(parts)

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
