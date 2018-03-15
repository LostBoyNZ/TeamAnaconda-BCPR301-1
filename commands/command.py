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
        has_switches = False

        # extract and run switch methods and extract user data
        # e.g. file name, from the command
        if switches_and_data:
            methods_to_run, self.user_string = self.get_switch_and_data(
                switches_and_data, self)
            if methods_to_run:
                self._run_switch_methods(methods_to_run)
                has_switches = True

        if not has_switches:
            self._default()

    def _run_switch_methods(self, methods_to_run):
        for method in methods_to_run:
            try:
                method()
            except TypeError:
                pass

    def get_switch_and_data(self, user_data, my_command):
        methods_to_run = []
        strings_to_keep = []
        split_user_data = user_data.split(" ")

        for data in split_user_data:
            try:
                if data[0] == "/" and len(data) == 2:
                    switch = my_command.get_switch(data[1])
                    methods_to_run.append(switch)
                else:
                    not_a_switch = data
                    strings_to_keep.append(not_a_switch)
            except IndexError:
                pass

        user_string = " ".join(strings_to_keep)
        return methods_to_run, user_string
