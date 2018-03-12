# Graham
import sys

try:
    from errors import ErrorHandler as err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - errors.py not found.")
    sys.exit()


class LogFileHandler(object):

    def open_file(self, file_name, mode):
        try:
            file = open(file_name, mode)
        except FileNotFoundError:
            try:
                print(err.get_error_message(403, "log"))
                print("Creating log file...")
                self._create_file(self, file_name)
            except OSError:
                print(err.get_error_message(401, "log"))
            except:
                print(err.get_error_message(402, "log"))
            else:
                print("log.txt file created")

        return file

    @staticmethod
    def close_file(file):
        file.close()

    def load_file_data(self, file_name):
        file_contents = []

        try:
            with self.open_file(self, file_name, "r") as file:
                for line in file:
                    a_line = line.rstrip()
                    file_contents.append(a_line)
            self.close_file(file)
        except FileNotFoundError:
            try:
                print(err.get_error_message(403, "log"))
                print("Creating log file...")
                self._create_file(self, file_name)
            except OSError:
                print(err.get_error_message(401, "log"))
            except:
                print(err.get_error_message(402, "log"))
            else:
                print("log.txt file created")

        return file_contents

    def file_is_empty(self, file_name):
        result = False

        file_contents = self.load_file_data(self, file_name)

        if len(file_contents) == 0:
            result = True

        return result

    def wipe_file(self, file_name):
        try:
            file = self.open_file(self, file_name, "r+")
            file.truncate()
            self.close_file(file)
        except PermissionError:
            print(err.get_error_message(405, "log"))

        if self.file_is_empty(self, file_name):
            print("Log file wiped")
        else:
            print("Log file not wiped")

    def _create_file(self, file_name):
        file = self.open_file(self, file_name, "w+")
        self.close_file(file)

    def output_file(self, file_contents, direction):
        if direction == "r":
            for line in file_contents[::-1]:
                print(line)
        else:
            for line in file_contents:
                print(line)

    @staticmethod
    def append_file(file_name, data_to_write):
        file = open(file_name, "a+")
        file.write(data_to_write + "\n")
        print("\"{}\" written to log file".format(data_to_write))