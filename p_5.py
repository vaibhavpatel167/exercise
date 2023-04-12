"""Admission_ID = # get and process input for a list of the number of admission ID
 CAP_Rank = # get and process input rank of the student in CAP # Information to be sent to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship. \n\n" # write a for loop that iterates through each set of names, Admission_ID, and CAP ranks to print each student's message."""

names = input("Enter a list of names, separated by commas: ").split(",")

admission_ids = input("Enter a list of admission IDs, separated by commas: ").split(",")

cap_ranks = input("Enter a list of CAP ranks, separated by commas: ").split(",")

for name, admission_id, cap_rank in zip(names, admission_ids, cap_ranks):
    message = "Hi {},\n\nCongratulations...! You got selected for the next round of recruitment process. Please submit your academic credentials, including primary and secondary certificates. Your admission ID is {} and you will be eligible for the next round of interview with a CAP rank of {}. If you submit all the documents on time, the university might offer you a scholarship.\n\n".format(name.strip(), admission_id.strip(), cap_rank.strip())
    print(message)