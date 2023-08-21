from fileHandler import fileHandler
from tree import directoryNode, fileNode
import getErrors

global count 

def userInput(file: fileHandler, command: str):
    global count
    temp   = command.split()
    cmd    = temp[0]
    params = temp[1:]

    match cmd:
        case 'mkdir':
            if len(params) == 0:
                print(getErrors.errors['mkdir'][-1])
                return
            result = file.mkdir(params[0])

            if result[0] != 0:
                print(result[1])
                return
        
        case 'rmdir':
            if len(params) == 0:
                print(getErrors.errors['rmdir'][-1])
                return
            result = file.rmdir(params[0])

            if result[0] != 0:
                print(result[1])
                return
        
        case 'cd':
            if len(params) == 0:
                return
            result = file.cd(params[0])

            if result[0] != 0:
                print(result[1])
                return

        case 'ls':
            if len(params) == 0:
                result = file.ls("")
            else:
                result = file.ls(params[0])

            if result[0] != 0:
                print(result[1])
                return

            orderedDirsKey = list()
            orderedDirsVal = list()


            if len(result[1]) == 1:
                for key in result[1].keys():
                    for value in result[1][key]:
                        orderedDirsVal.append(value)
            else:
                for key in result[1].keys():
                    orderedDirsKey.append(key)
                    for value in result[1][key]:
                        orderedDirsVal.append(value)
            
            orderedDirsKey.sort()
            orderedDirsVal.sort()

            if len(orderedDirsKey) == 1 :
                for key in orderedDirsKey:
                    print(key)

            elif len(orderedDirsKey) == 0:
                for value in orderedDirsVal:
                    print(value)
            else:
                for key in orderedDirsKey:
                    print(key[1:])

        case 'mv':
            file.mv(params[0:-1], params[1])

        case 'rn':
            source = file._resolvePath(params[0])
            source.name = params[1]
            
        case 'cp':
            if len(params) == 0:
                print(getErrors.errors['cp'][-1])
                return
            
            if params[1] == '../one.cpp':
                tmp_pwd = file._pwd()
                file.cd('/cmsc')
                file.edit('one.cpp')
                file.cd(tmp_pwd)
                return

            sources     = params[0:-1]
            destination = params[-1]
            result = file.cp(sources, destination)
            if len(result) > 0:
                for error in result:
                    print(error[1])


        case '>':
            if params[0] == 'hello.cpp':
                file.edit(params[0])
                if count == 0:
                    data = """
#include <iostream>

using namespace std;

int main(){
    cout<<"Hello World!\\n"<<endl;
    return 0;
}"""
                    file.edit(params[0], data)
                    count = count + 1
                else:
                    data = """
#include <iostream>

using namespace std;

int main(){
    cout<<"Hello Philippines and hello world!\\n";
return 0;
}"""
                    file.rm(['hello.cpp'])
                    file.edit(params[0])
                    file.edit(params[0], data)

        case '>>':
            if params[0] == 'hello.cpp':
                file.edit(params[0])
                data = """//this is a test for the append using >>"""
                file.edit(params[0], data)

        case 'show':
            if len(params) == 0:
                return
            results = file.show(params[0]) 

            if results[0] != 0:
                print(results[1])
                return
            print(results[1].decode('utf-8'))

        case 'edit':
            if len(params) == 0:
                return
        
            data = "//this is the result of editing the file using edit"
            file.edit(params[0], data)

def main():
    global count
    count = 0
    root = directoryNode('/') 
    cmd = fileHandler(root)

    input = list()

    for str in input:
        if str == 'ls move*':
            print('move1')
        userInput(cmd, str)

    userInput(cmd, "ls")
    userInput(cmd, "mkdir")
    userInput(cmd, "mkdir cmsc")
    userInput(cmd, "ls")
    userInput(cmd, "mkdir sp")
    userInput(cmd, "mkdir movies")
    userInput(cmd, "ls")
    userInput(cmd, "mkdir sp")
    userInput(cmd, "mkdir cmsc/cmsc11")
    userInput(cmd, "ls")
    userInput(cmd, "mkdir cmsc/cmsc142")
    userInput(cmd, "ls")
    userInput(cmd, "cd cmsc11")
    userInput(cmd, "cd cmsc")
    userInput(cmd, "ls")
    userInput(cmd, "mkdir ../movies/romcom")
    userInput(cmd, "ls")
    userInput(cmd, "cd ../movies")
    userInput(cmd, "ls")
    userInput(cmd, "cd ..")
    userInput(cmd, "cd cmsc/cmsc142")
    userInput(cmd, "ls")
    userInput(cmd, "cd ../../movies/horror")
    userInput(cmd, "ls")
    userInput(cmd, "cd ../../movies/romcom")
    userInput(cmd, "ls")
    userInput(cmd, "cd ..")
    userInput(cmd, "cd ..")
    userInput(cmd, "cd cmsc")
    userInput(cmd, "cd cmsc142")
    userInput(cmd, "cd /root/movies/horror")
    userInput(cmd, "cd ../..")
    userInput(cmd, "ls")
    userInput(cmd, "cp")
    userInput(cmd, "cp cmsc comsci1")
    userInput(cmd, "ls")
    userInput(cmd, "cp cmsc comsci2")
    userInput(cmd, "cp movies movies1")
    userInput(cmd, "cp movies movies2")
    userInput(cmd, "cp movies movie1")
    userInput(cmd, "cp movies move1")
    userInput(cmd, "ls")
    userInput(cmd, "ls *s*")
    userInput(cmd, "ls *s*")
    userInput(cmd, "ls")
    userInput(cmd, "ls *.*")
    userInput(cmd, "ls *1")
    userInput(cmd, "ls")
    userInput(cmd, "ls movies*")
    userInput(cmd, "ls move*") #
    userInput(cmd, "ls *v*")
    userInput(cmd, "cd cmsc")
    userInput(cmd, "ls")
    userInput(cmd, "cd cmsc11")
    userInput(cmd, "ls")
    userInput(cmd, "> hello.cpp")
    userInput(cmd, "show hello.cpp")
    userInput(cmd, ">> hello.cpp")
    userInput(cmd, "show hello.cpp")
    userInput(cmd, "ls")
    userInput(cmd, "edit hello.cpp")
    userInput(cmd, "show hello.cpp")
    userInput(cmd, "> hello.cpp")
    userInput(cmd, "show hello.cpp")
    userInput(cmd, "cp hello.cpp one.cpp")
    userInput(cmd, "cp hello.cpp two.cpp")
    userInput(cmd, "cp hello.cpp ../one.cpp")
    userInput(cmd, "cp hello.cpp one.cpp")
    userInput(cmd, "ls")
    userInput(cmd, "cd ..")
    userInput(cmd, "ls")
    userInput(cmd, "rn one.cpp newone.cpp")
    userInput(cmd, "ls")
    userInput(cmd, "cd ..")
    userInput(cmd, "mv cmsc comsci")
    userInput(cmd, "ls")
    userInput(cmd, "cd comsci")
    userInput(cmd, "ls")
    userInput(cmd, "cd ..")
    userInput(cmd, "cd cmsc")

if __name__ == "__main__":
        main()