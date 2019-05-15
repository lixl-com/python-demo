import os

## read all user and bash home from passwd file
with open('/etc/passwd', 'r') as passwdFile:
    allLines = passwdFile.readlines();
    for line in allLines:
        userInfo = line.split(":")
        user_name = userInfo[0]  ## get user_name
        user_home = userInfo[5]  ## get user_home
        # print(user_name+" "+user_home);

        bash_history_file_name = user_home + '/.bash_history'
        ## judge bash_history exists ??
        if (os.path.exists(bash_history_file_name)):
            ## read user bash history from userHome
            with open(bash_history_file_name, 'r') as sourceFile:
                ## wirte bash history info to log file (name with userName)
                logFile = '/home/lixl/PycharmProjects/demo/output/' + user_name + '.log';
                print(logFile)
                with open(logFile, 'w') as outputFile:
                    outputFile.write(sourceFile.read())

