directory = input('please input your filepath')
filename = input('please give me a name for your file')
name = input('Please enter your name')
address = input('please enter your address')
phone = input('please enter your phone number')
with open(os.path.join(directory, 'w')) as file_object:
  file_object.write(name)
  file_object.write(address)
  file_object.write(phone)
f = open(filename, "r")
print(f.read())