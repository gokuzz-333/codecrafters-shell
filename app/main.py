import sys
import shutil,subprocess,os

def execute_command(c):
    for d in os.get_exec_path():
        if os.access(fullpath:=os.path.join(d,c),os.X_OK):
            return fullpath

        
def builtin_commands(c):
    return c in {"echo","exit","type","pwd","cd"}

def parse_command(text):
    parts=[]
    current=""
    in_quotes=False
    i=0

    while i<len(text):
        if text[i]=="'":
            in_quotes=not in_quotes
        elif text[i]==" ":
            if in_quotes:
                current+=" "
            else:
                if current!="":
                    parts.append(current)
                    current=""
        else:
            current+=text[i]
        i+=1
    if current!="":
        parts.append(current)
    return parts

def main():
    while True:
        sys.stdout.write("$ ")
        command=input().strip()
        if not command:
            continue

        parts=parse_command(command)
        cmd=parts[0]
        args=parts[1:]

        if builtin_commands(cmd):
            if cmd=="exit":
                break

            elif cmd=="echo":
                print(" ".join(args))

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
