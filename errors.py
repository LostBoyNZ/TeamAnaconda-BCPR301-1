class ErrorHandler(object):  # Claye

    @staticmethod
    def get_error_message(error_code, name = ""):

        error_dictionary = {  # CLI Errors -----
            101: "Command not supported",
            102: "Invalid Input, please try again",
            103: "Illegal file path, please try again",
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
            # System File Errors ----- # Graham
            401: "Warning - {} file could not be created".format(name),
            402: "Warning - Unknown error creating {} file".format(name),
            403: "Warning - {} not found".format(name),
            404: "Fatal Error - {} not found".format(name),
            405: "Error - {} file is read only".format(name),
            # Database Errors ----- # Graham
            501: "Error - {} key is not valid, please try again".format(name),
        }
        return error_dictionary[error_code]
