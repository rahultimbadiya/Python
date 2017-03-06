class Scheduling():
    ''' this class compute the scheduling of different algorithms in different mode '''

    list_of_process = []  #contains the all process in list
    num_process = 0  #contains the number opf process
    total_time = 0  #contains the total final time

    def __init__(self):
        ''' this is constructor class and it will be called when object wiill be created    '''
        self.list_of_process = self.file_read() #read the data from putside file
        self.list_of_process.sort(key=lambda e:e[1]) #sort the incoming processe


    def calc_time(self):
        '''  this method calculate the total computation time for all the processes
        '''
        for e in range(0,self.num_process):
            self.total_time = self.total_time + self.list_of_process[e][2] #it will contain the total time of processes
            self.total_time = self.total_time + self.list_of_process[0][1]

    def file_read(self):
        ''' this is the method to read the data from text file and append it to list to process it '''

        with open('textfile.txt', 'r') as file:  #it will open the text file from outside and read it
            listl1 = []
            for line in file:
                listl1.append([int(e) for e in line.split()])  #it will read the arrival time from text file
                self.num_process+=1
            return (listl1)



    def SRJF_Nonverbose(self):
        ''' This method computes shortest remaining job first algorithm in Non verbose mode'''
        print("Shortest job first algorithm in verbose mode:")
        turn1 = 0
        turn2 = 0
        skip_turn = 0
        turn_over = 1
        list_current = []   # it contains the current process who are currently processing by cpu
        list_ready = []   # it contains the process who are ready for processed
        time_list = []   # it contains the process id and completion time to print at the end

        for p in range(0,self.total_time+1):   # it will go through o to total time to perform the algorithm

            if skip_turn == 0:

                if p == self.list_of_process[turn1][1]:
                    list_ready.append(self.list_of_process[turn1])
                    list_ready.sort(key=lambda x:x[2])  # sort the ready list for future use

                    if turn1 == 0:
                        list_current = self.list_of_process[turn1]

                    turn1 = turn1 + 1

                    if turn1<self.num_process-1 and self.list_of_process[turn1][1]==self.list_of_process[turn1+1][1]:
                        turn1 += 1

                    if turn1 == self.num_process:
                        skip_turn = 1

            if turn2<self.num_process:

                if turn1>0 and list_current != list_ready[turn2] and list_ready[turn2][2] !=0:
                    list_current = list_ready[turn2]

                if turn1>0:
                    if list_ready[turn2][2] == 0:

                        time_list.append([list_ready[turn2][0],p]) # append the process and its time to the time list
                        time_list.sort(key=lambda x:x[0]) # it will sort the time_list list with lambda function

                        turn2 += 1
                        turn_over = 0
                    if p < self.total_time+1 and turn2 < self.num_process:

                        list_ready[turn2][2] -= 1

                    if turn_over == 0 and turn2< self.num_process:
                        list_current = list_ready[turn2]
                        turn_over = 1

        print("\nJob id\t Completion time\n")   #it will print the job id and completion time in nonverbose mode
        for t in range(0,self.num_process):     #it will go through the loop to print the job id and completion time
            print("  ",time_list[t][0],"---->",time_list[t][1])

    def FCFS_Nonverbose(self):
        '''  This method computes first come first serve algorithm in non verbose mode
        '''
        print("First come first serve algorithm in Non-verbose mode:")
        turn1 = 0
        counter = self.list_of_process[0][1]  # variable that contain arrival time of first process in beginning
        turn2 = 0
        turn_over = 1
        skip_turn = 0
        time_list = [ ] # it contains the process id and completion time to print at the end

        for p in range(0,self.total_time+1):   # it will go through 0 to total time to perform the algorithm
            if skip_turn == 0:
                if p == self.list_of_process[turn1][1]:
                    pass

                    if turn1 == 0:
                        pass

                    if turn1 < self.num_process-1 and self.list_of_process[turn1][1] == self.list_of_process[turn1+1][1]:
                        turn1 += 1

                    turn1 = turn1 + 1

                    if turn1 == self.num_process:
                        skip_turn = 1

            if turn2<self.num_process:
                if p == self.list_of_process[turn2][2]+ counter:

                    counter += self.list_of_process[turn2][2]
                    time_list.append([self.list_of_process[turn2][0],p]) #append the process and its time to the time list
                    #print(time_list)
                    turn2 += 1
                    turn_over = 0


                if turn_over == 0 and turn2<self.num_process:
                    turn_over = 1

        print("\nJob id\t Completion time\n")   #it will print the job id and completion time in nonverbose mode
        for t in range(0,self.num_process):    #it will go through the loop to print the job id and completion time
            print("  ",time_list[t][0],"--->",time_list[t][1])




    def RR_Nonverbose(self):
        # this method is implemented to calculate the round robin algorithm in non verbose mode
        list_ready = []
        time_slice = 8  # time slice value that every process will get in turn to processed by cpu
        turn1 = 0
        turn2 = 0
        time_list = []  # it contains the process id and completion time to print at the end
        skip_turn = 0
        counter = 0
        item_list = 0

        for p in range(0,self.total_time+1): # it will go through o to total time to perform the algorithm
            if skip_turn == 0:
                if p == self.list_of_process[turn1][1]:

                    list_ready.append(self.list_of_process[turn1])
                    item_list += 1

                    if turn1 == 0:
                        pass

                    turn1 += 1

                    if turn1<self.num_process-1 and self.list_of_process[turn1][1]==self.list_of_process[turn1+1][1]:
                        turn1+=1


                    if turn1 == self.num_process:
                        skip_turn = 1

            if len(list_ready) > 0:
                if counter >= time_slice:

                    counter = 0
                    turn2 += 1

                    if turn2 == item_list:
                        turn2 = 0


                list_ready[turn2][2] -= 1
                counter += 1
                if list_ready[turn2][2] == 0:
                    time_list.append([list_ready[turn2][0],p]) #append the process and its time to the time list
                    time_list.sort(key=lambda P:P[0]) #it will sort the time_list list with lambda function

                    del list_ready[turn2] # this is function to delete the list that will given by python default
                    counter = 0
                    item_list -= 1
                    turn2 += 1

                    if turn2 >= item_list:
                        turn2 = 0

                    if len(list_ready) > 0:
                        pass

        print("\nJob id\t Completion time\n")   #it will print the job id and completion time in nonverbose mode
        for t in range(0,self.num_process):    #it will go through the loop to print the job id and completion time
            print("  ",time_list[t][0],"---->",time_list[t][1])




    def FCFS_verbose(self):
        ''' This method computes the first come first serve algorithm in verbose mode with all details '''

        print("First come first serve algorithm in verbose mode:")
        turn1 = 0
        counter = self.list_of_process[0][1] # variable that contain arrival time of first process in beginning
        turn2 = 0
        turn_over = 1
        skip_turn = 0

        for p in range(0,self.total_time+1):   # it will go through o to total time to perform the algorithm
            if skip_turn == 0:
                if p == self.list_of_process[turn1][1]:
                    print("\nAt time",p,"process",self.list_of_process[turn1][0],"ready")
                    if turn1 == 0:
                        print("\nAt time",p,"process",self.list_of_process[turn1][0],"ready -> running")
                    if turn1 < self.num_process-1 and self.list_of_process[turn1][1] == self.list_of_process[turn1+1][1]:
                        turn1 = turn1 + 1
                        print("\nAt time",p,"process",self.list_of_process[turn1][0],"ready")
                    turn1+=1
                    if turn1 == self.num_process:
                        skip_turn = 1

            if turn2<self.num_process:
                if p == self.list_of_process[turn2][2]+ counter:
                    print("\nAt time",p,"process",self.list_of_process[turn2][0],"running -> terminated")
                    counter += self.list_of_process[turn2][2]
                    turn2 += 1
                    turn_over = 0

                if turn_over==0 and turn2<self.num_process:
                    print("\nAt time",p,"process",self.list_of_process[turn2][0],"ready -> running")
                    turn_over=1


    def RR_verbose(self):
        # this method is implemented to calculate the round robin algorithm scheduling in verbose mode

        list_ready = []  # it contains the process who are ready for processed
        time_slice = 8
        turn1 = 0
        turn2 = 0
        skip_turn = 0
        counter = 0
        item_list = 0

        for p in range(0,self.total_time+1):   # it will go through o to total time to perform the algorithm
            if skip_turn == 0:
                if p == self.list_of_process[turn1][1]:
                    print("\nAt time",p,"process ",self.list_of_process[turn1][0],"ready")
                    list_ready.append(self.list_of_process[turn1])
                    item_list += 1

                    if turn1 == 0:
                        print("\nAt time ",p,"process ",self.list_of_process[turn1][0]," Ready -> Running.")

                    turn1 += 1

                    if turn1<self.num_process-1 and self.list_of_process[turn1][1]==self.list_of_process[turn1+1][1]:
                        turn1+=1
                        print("\nAt time ",p,"process ",self.list_of_process[turn1][0],"ready")

                    if turn1 == self.num_process:
                        skip_turn = 1

            if len(list_ready) > 0:
                if counter >= time_slice:
                    print("\nAt time ",p,"process", list_ready[turn2][0],"running -> ready")
                    counter = 0
                    turn2 += 1

                    if turn2 == item_list:
                        turn2 = 0

                    print("\nAt time",p,"process",list_ready[turn2][0],"ready -> running ")
                list_ready[turn2][2] -= 1
                counter += 1
                if list_ready[turn2][2] == 0:
                    print("\nAt time ",p,"process ",list_ready[turn2][0],"running -> terminated")

                    del list_ready[turn2]
                    counter = 0
                    item_list -= 1
                    turn2 += 1

                    if turn2 >= item_list:
                        turn2 = 0

                    if len(list_ready) > 0:
                        print("\nAt time",p,"process ",list_ready[turn2][0],"ready -> running")



    def SRJF_verbose(self):
        ''' This method computes shortest remaining job first algorithm in verbose mode with all details '''
        print("Shortest job first algorithm in verbose mode:")
        turn1 = 0
        turn2 = 0
        skip_turn = 0
        turn_over = 1
        list_current = []  # it contains the current process who are currently processing by cpu
        list_ready = []  # it contains the process who are ready for processed

        for p in range(0,self.total_time+1):   # it will go through o to total time to perform the algorithm

            if skip_turn == 0:

                if p == self.list_of_process[turn1][1]:

                    print("\nAt time",p,"process",self.list_of_process[turn1][0],"ready")
                    list_ready.append(self.list_of_process[turn1])
                    list_ready.sort(key=lambda x:x[2])

                    if turn1 == 0:

                        print("\nAt time",p,"process",self.list_of_process[turn1][0],"ready -> running")
                        list_current = self.list_of_process[turn1]
                    turn1 += 1

                    if turn1<self.num_process-1 and self.list_of_process[turn1][1]==self.list_of_process[turn1+1][1]:
                        turn1 += 1

                        print("\nAt time",p,"process",self.list_of_process[turn1][0],"ready")


                    if turn1 == self.num_process:

                        skip_turn = 1

            if turn2<self.num_process:

                if turn1>0 and list_current != list_ready[turn2] and list_ready[turn2][2] !=0:

                    print("\nAt time ",p," process ",list_current[0]," running -> ready.")
                    print("\nAt time ",p," process ",list_ready[turn2][0]," ready -> running.")
                    list_current = list_ready[turn2]
                if turn1>0:
                    if list_ready[turn2][2] == 0:

                        print("\nAt time ",p," process ",list_ready[turn2][0]," running ->terminated.")
                        turn2 += 1
                        turn_over = 0
                    if p < self.total_time+1 and turn2 < self.num_process:

                        list_ready[turn2][2] -= 1
                    if turn_over == 0 and turn2< self.num_process:

                        print("\nAt time ",p," process ",list_ready[turn2][0]," ready -> running.")
                        list_current = list_ready[turn2]
                        turn_over = 1


str1 = input("Enter the following options for scheduling of algorithm:\n"
             "1. -f -textfile.txt -v    (for FCFS algorithm in verbose mode)\n"
             "2. -f -textfile.txt       (for FCFS algorithm in Non verbose mode)\n"
             "3. -srjf -textfile.txt -v (for SRJF algorithm in verbose mode)\n"
             "4. -srjf -textfile.txt    (for SRJF algorithm in Non verbose mode)\n"
             "5. -rr -textfile.txt -v   (for RR algorithm in verbose mode)\n"
             "6. -rr -textfile.txt      (for RR algorithm in Non verbose mode)\n"
             "Enter your command here:")

s1 = Scheduling()  # create the object of class scheduling and init main will be executed
s1.calc_time()   # call the method to calculate the time

if str1 == "-f -textfile.txt -v": # if this string will enter by user then next line method will be executed
    s1.FCFS_verbose()

elif str1 == "-f -textfile.txt": # if this string will enter by user then next line method will be executed
    s1.FCFS_Nonverbose()

elif str1 == "-srjf -textfile.txt -v": # if this string will enter by user then next line method will be executed
    s1.SRJF_verbose()

elif str1 == "-srjf -textfile.txt": # if this string will enter by user then next line method will be executed
    s1.SRJF_Nonverbose()

elif str1 == "-rr -textfile.txt -v": # if this string will enter by user then next line method will be executed
    s1.RR_verbose()

elif str1 == "-rr -textfile.txt": # if this string will enter by user then next line method will be executed
    s1.RR_Nonverbose()














