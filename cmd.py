import validator

# class Cmd():
#
#     def command(self):
#         userCommand = input("> ")
#
#         try:
#             className = Hi
#             newObject = className()
#             #userCommand()
#         except NameError:
#             print("Command not found")
#
# class Hi():
#     def run(self):
#         print("hi")
#
#     print("hello")
#
# i = Cmd()
# i.command()

output = validator.Validator.has_this_many_numbers(3, "302")
print(output)