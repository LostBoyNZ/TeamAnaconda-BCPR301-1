class Command:

    my_command_line = None
    user_string = ""

    def __init__(self, switches_and_data, command_line):
        if __name__ == "__main__":
            pass
        else:
            self.go(switches_and_data, command_line)

    def go(self, switches_and_data, command_line):
        self.my_command_line = command_line

        # extract and run switch methods and extract user data, e.g. file name, from the command
        if switches_and_data:
            methods_to_run, self.user_string = self.my_command_line.split_input(switches_and_data, self)
            if methods_to_run:
                self.run_switch_methods(methods_to_run)

        self.default()

    def run_switch_methods(self, methods_to_run):
        for method in methods_to_run:
            try:
                method()
            except TypeError:
                pass