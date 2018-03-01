class ErrorHandler(object):  # Claye

    def __init__(self):  # constructor
        self.error_dictionary = {  # CLI Errors -----
                                 101: "Command not supported",
                                 # File Errors -----
                                 201: "File not found",
                                 202: "Unable to load file",
                                 203: "Unable to save file",
                                 204: "Unsupported file format",
                                 205: "Unable to edit log file",
                                 206: "Empty data field",
                                 207: "Invalid data field",
                                 208: "File empty",
                                 209: "Database empty",
                                 # Validation Errors -----
                                 301: "Unable to validate data",
                                 }

    def get_error_message(self, error_code):
        return self.error_dictionary[error_code]


i = ErrorHandler()
print(i.get_error_message(301))

