# Roshani assignment-4
#file handling
def read_data(filenames):        #function read_data
    feedback_data = []            #list feedback_data

    for filename in filenames:       #put each file name from filenames to filename
        try:
            with open(filename, 'r') as file:       #open file
                for line in file:        #read each line from file
                    feedback_data.append(line.strip())    #append line of file in feedback_data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    return feedback_data

def process_data(feedback_data):           #function process_data
    totalf = 0       #total feedback
    totalr = 0.0      #total rating

    list = []

    for feedback in feedback_data:      #put each feedback data from feedback_data to feedback
        num = feedback.split(': ')      #split feedback from : and store in num
        if len(num) == 2:           #check length of num is 2 or not
            customer_name = num[0]    #value of 0 index of num store at customer_name
            rating_comment = num[1]   #value of 1 index of num store at rating_comment

            rating,comment = rating_comment.split(' - ')
            rating = int(rating)         #convert string datatype of rating to int
            totalr = totalr + rating
            totalf = totalf + 1

            # Format and store processed feedback
            list.append(f"{customer_name}: {rating} - {comment}")


    avg = totalr / totalf
    return list, avg

def summary_file(list, totalf, avg, output_filename):     #function summary_file
    with open(output_filename, 'w') as file:
        file.write(f"Total Feedback: {totalf}\n")   #write sentence in a file
        file.write(f"Average Rating: {avg:.2f}\n\n")

        for feedback_entry in list:
            file.write(f"{feedback_entry}\n")

filenames = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt']   #store 3 file name in filenames
feedback_data = read_data(filenames)     #call read_data and store output in feedback_data

process_data, avg = process_data(feedback_data)    #call process_data and store output in process_data,avg
totalf = len(process_data)   #find length of process_data and store in totalf


summary_file(process_data, totalf, avg, 'feedback_summary.txt')   #call to summary_file

print("Summary file 'feedback_summary.txt' has been generated successfully.")