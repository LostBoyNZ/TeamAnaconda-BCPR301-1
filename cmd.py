import validate_empid

# getattr

# class Cmd():
#
#     def command(self):
#         userCommand = input("> ")
#
#         try:
#             #className = Hi
#             i = userCommand
#             output = i.has_this_many_numbers(i, 3, "302")
#             print(output)
#             #newObject = className
#             #className = userCommand
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

# This checks if an ID is valid
i = validate_empid.ValidateEmpid
output = i.is_valid(i, "a#2@$&*(@&$01")
print(output)