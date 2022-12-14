### Goal: Pull data from a text file for stored knowledge and also be able to write new information to it


### Text File Define ###
Text_File = "readme.txt"
### Text File Define ###


### Read Start ###
TopicRead = ''
### Read End ###


### Write Start ###
TopicWrite = ''
Data = ''
### Write End ###



User_Input_Mod = (TopicRead + ":")
User_Topic_Input_Mod = (TopicWrite + ":")
Notes_Mod = ["", TopicWrite + ":" + " " + Data]



if TopicRead > "":
    with open(Text_File, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(User_Input_Mod) != -1:
                x = line.split(":", 1)[1]
                print(x)
                break
        else:
            print('information under that name does not exist')



if TopicWrite > "":
    with open(Text_File, 'r') as f:
        for l_no, line in enumerate(f):
            # search string
            if User_Topic_Input_Mod in line:
                print('Information already exists under that Topic name.')
                break
        else:
            with open(Text_File, 'a') as f:
                f.write('\n'.join(Notes_Mod))

