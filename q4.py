# # banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# my_file=open("file-question4.txt","a")
# # for i in my_file:
# my_file.write("Kotak\nHDFC\nRBL\nSBI\nBank of Baroda\n")
#     # print(my_file.read())
# my_file.close()

# my_file=open("file-question4.txt","r")
# print(my_file.read())
# my_file.close()

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file=open("file-question4.txt","a")
for i in range(len(banks_list)):
    a=my_file.write()
    print(banks_list[i])
my_file.close()

my_file=open("file-question4.txt","r")
print(my_file.read())
my_file.close()