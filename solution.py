#QUESTION
# In this problem, you are given a set of house listings and your job is to return a list of the most recent listing of each address.
# There could be multiple listings of the same address, and you must ensure your ouput contains only one listing per address (the most
# recent one). A listing contains a name, address, and date.

# For example:

# Input:
#L4, 123 kings road,2022
#L1, 123 kings road,2020
#L2, 20 queen road,1990
#L3, 20 queen road,1992

# Expected Output:
# (L4, L3)

# In the above example, there are two listings with the same address "123 kings road", and two listing with the same address "20 queen road".
# The output includes the most recent listing with the address "123 kings road" (2022 > 2020) which is L4, and the most recent listing with
# the address "20 queen road" (1992 > 1990) which is L3, hence (L4, L3).



#Shaheer Khan's Solution

#I assume I just have to return the index of the address aka L3, L4 in a list and not the entire address
#Another assumption to make is the input will be given to me in the console in one long String and I have to parse that string and store it in a list. 
#I decided to parse by new line because I am a bit confused as to how we are meant to recieve Input  
#The input is also assumed to be always formatted like "L1, address, date" etc... I did not implement input checking as I thought it to be unnessecary  

#AFTER PUTTING INPUT PRESS ENTER TWICE TO TEST

#The way I will approach this is 
#Step 1, Parse input
#Step 2) Loop through all objects while going through the input. 
#Step 3), Store object in dict using address as a hash key for location, while storing if collision is detected and address is the same than store the most recent object by date (Address)
#step 4, Get all items in dict with loop and store into a list and output, I just output the final list so it shows all the index in one line 


#This solution will take O(n) time, as it goes through the loop all the way through. 
#Space complexity will be each O(n) for the hashmap and the list. 


#Step 1
lines=[]
print("Hey team KnockNow, insert input here all in one string: \n")
while True:
    initial_str=input()
    if initial_str:
        lines.append(initial_str)
    else: 
        break

#Step 2-3
new_dict = dict() 
list = []
for x in range (0,len(lines)):
    temp= lines[x].split(",")
    index= temp[0]
    address=temp[1]
    date= temp[2]
    #If address exists 
    if address in new_dict:
        oldAdd= new_dict.get(address)
        oldDate,oldIndex= oldAdd[0], oldAdd[1]
        if (oldDate <= date) and (oldIndex!=index):
            list= [date,index]
            new_dict[address]=list
    #if address is new
    else:
        list= [date, index]
        new_dict.__setitem__(address,list)


#Step 4
temp=[]
for key in new_dict:
    temp.append(new_dict.get(key)[1])
print(temp)

        

    






