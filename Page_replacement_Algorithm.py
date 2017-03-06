

class PageReplacement:
    '''This is the main class that implement the page replacement algorithms'''


    def __init__(self):
        '''Constructor of class used to initialised the variables while creating the object of class '''
        str = ''
        str2 = ''

    def FIFO(self):
        '''This method implement the FIFO page replacement algorithm'''
        print("FIFO algorithm")
        list_fifo = []  # list that contains the current page frame
        count = 0  # variable that used to count the page faults happen in algorithm
        pos = 0
        i = int(input("Enter the number of memory slots you want: "))  # take the input from user
        a = input("Enter the string you want:  ")  # take the string of page frames from user

        for x in range(0,len(a)):  # loop it will run until the last page frame entered by the user and after it stops
            if a[x] in list_fifo:  # check whether new incoming page is in list or not
                print(a[x],":",list_fifo)  # print the list that contains the current page frames
                x += 1  # increment the pointer for next incoming page frame
            else:
                if len(list_fifo) < i:  # condition to check whether length of list is less than the memory slot entered by user or not
                    list_fifo.append(a[x])  # append the value to the end of the list
                    print(a[x],":",list_fifo)  # print the list that contains the current page frames
                    x += 1  # increment the pointer for next incoming page frame
                    count += 1  # increment counter variable to consider the page fault in the algorithm

                else:
                    list_fifo[pos] = a[x]  # if list is full and new page frame come then replace the first frame from the list with the new frame
                    print(a[x],":",list_fifo)  # print the list that contains the current page frames

                    x += 1  # increment the pointer for next incoming page frame
                    count += 1  # increment the counter for page faults
                    if pos < i-1:
                        pos += 1
                    else:
                        pos = 0

        print("The number of page faults in FIFO are:",count)  # print the total number of page faults at the end of method
        pr.start_again()  # call the function to start the program again

    def LRU(self):
        '''This method implement the LRU page replacement algorithm'''
        print("LRU algorithm")
        list_lru = []  # list that contain the current page frames
        temp_list = []  # temporary list that used to keep the least recently used frames and switch with the original list
        p = 0  # variable that carry the index of temporary list
        count = 0  # variable that used to count the page faults happen in algorithm
        q = 0  # variable that carry the index of main current page frame list

        i = int(input("Enter the number of memory slots you want: "))  # take the input from user
        a = input("Enter the string you want:  ")  # take the string of page frames from user

        for x in range(0,len(a)):  # loop it will run until the last page frame entered by the user and after it stops
            if a[x] in list_lru:  # check whether new incoming page is in list or not
                print(a[x],":",list_lru)  # print the list that contains the current page frames

                p = temp_list.index(a[x])  # it hold the index of the page frame from the temporary list that match with the incoming page frame and it used to delete from the temp list
                del temp_list[p]  # delete the page frame with the index we got before
                temp_list.append(a[x])  # append the new incoming page into end of the list

                x += 1  # increment the pointer for next incoming page frame

            else:
                if len(list_lru) < i:  # check the condition whether length of list is less than the page frame size
                    list_lru.append(a[x])  # append the new incoming page into end of the main list
                    temp_list.append(a[x])  # append the new incoming page into end of the temp list
                    print(a[x],":",list_lru)  # print the list that contains the current page frames
                    x += 1  # increment the pointer for next incoming page frame
                    count += 1  # increment the counter for page faults
                else:
                    q = list_lru.index(temp_list[0])  # get the index of value from main list that match with the first value of the temp list
                    list_lru[q] = a[x]  # exchange the new incoming page with at the index of main list
                    print(a[x],":",list_lru)  # print the list that contains the current page frames

                    del temp_list[0]  # delete the first value from the temp list
                    temp_list.append(a[x])  # append the new incoming page into end of the temp list
                    x += 1  # increment the pointer for next incoming page frame
                    count += 1  # increment the counter for page faults

        print("The number of page faults in LRU are:",count)  # print the total number of page faults at the end of method
        pr.start_again()

    def Optimal(self):
        '''This method implement the OPTIMAL page replacement algorithm'''
        print("OPTIMAL algorithm")
        main_list = []  # list that contain the current page frames
        temp_list = []  # temporary list that used to keep the least recently used frames and switch with the original list
        p = 0
        count = 0  # variable that used to count the page faults happen in algorithm

        i = int(input("Enter the number of memory slots you want: "))  # take the input from user
        a = input("Enter the string you want:  ")  # take the string of page frames from user

        for x in range(i):
            temp_list.append(a[x])
            x += 1
        pos = i

        for x in range(0,len(a)):
            if len(main_list) < i:
                if temp_list[0] not in main_list:
                    main_list.append(temp_list[0])  # first value of temp_list append to main list
                    print(a[x],":",main_list)  # print the list that contains the current page frames
                    count += 1
                    del temp_list[0]  # delete the first value from the temp list
                    if pos < len(a):
                        temp_list.append(a[pos])  # append the new incoming page into end of the temp list
                        pos += 1
                else:
                    print(a[x],":",main_list)  # print the list that contains the current page frames
                    del temp_list[0]  # delete the first value from the temp list
                    if pos < len(a)-1:
                        temp_list.append(a[pos])  # append the new incoming page into end of the temp list
                        pos += 1
            else:
                if len(temp_list) != 0 and temp_list[0] in main_list:
                    print(a[x],":",main_list)  # print the list that contains the current page frames
                    del temp_list[0]  # delete the first value from the temp list

                    if pos < len(a):
                        temp_list.append(a[pos])  # append the new incoming page into end of the temp list
                        pos += 1
                    else:
                        pass
                else:
                    true = 0
                    for p in range(i):
                        if main_list[p] not in temp_list and len(temp_list) != 0 and true == 0:
                            main_list[p] = temp_list[0]  # swap the first valur of temp list with main list
                            true = 1
                            print(a[x],":",main_list)  # print the list that contains the current page frames
                            count += 1
                            del temp_list[0]  # delete the first value from the temp list
                            if pos < len(a):
                                temp_list.append(a[pos])  # append the new incoming page into end of the temp list
                                pos += 1

        print("The number of page faults in OPTIMAL algorithm are:",count)   # print the total number of page faults at the end of method
        pr.start_again()

    def start_function(self):

        str = input("Enter the command you want from following:\n"
                       "1. F (for FIFO page replacement algorithm)\n"
                       "2. L (for LRU page replacement algorithm)\n"
                       "3. O (for OPTIMAL page replacement algorithm):   ")  # take the input from user which algorithm he wnats to run

        if str == 'F':  # if user enter F then following function will be called
            pr.FIFO()
        elif str == 'L':  # if user enter L then following function will be called
            pr.LRU()
        elif str == 'O':  # if user enter O then following function will be called
            pr.Optimal()

        else:
            print("Invalid key try again")  # if user entered invalid key then call the main unction again for input
            pr.start_function()

    def start_again(self):  # this method is used to start the program again as it take the input from the user whether they want to start again or not

        str2 = input("Want to start again?(press y or n): ")
        if str2 == 'y':  # if user press y then start function will be called
            pr.start_function()
        else:
            exit()  # if user press any other button then exit the program


pr = PageReplacement()  # create the object
pr.start_function()  # call the main function from that the program will start











