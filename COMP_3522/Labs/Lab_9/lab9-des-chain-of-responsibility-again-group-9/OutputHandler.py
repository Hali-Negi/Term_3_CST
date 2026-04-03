import pathlib
from operator import contains

from Handler import Handler
from CryptoModeEnum import CryptoMode


class OutputHandler(Handler):

    def next(self, request):
        """
        Checks the output setting of the request and handles accordingly.
        -o is the default, this prints the results to the console.
        If set to a file name with an extension, results will be written to the file
        If set to a file name with no extension, the following rules are applied:
            - Unencrypted strings written to a file use .txt extension
            - Encrypted data is written to a file use .bin extension
        :param request: the request object to handle.
        """
        output_type = request.output
        result = request.result
        encryption_type = request.encryption_state

        # Default or -o should be printed
        if output_type is None or output_type == "print":
            print(f"OutputHandler: Result: {result}")
        # If the output is the name of a file that contains an extension, write to the file
        elif contains(output_type, '.'):
            extension = output_type.split('.', 1)[1]
            if extension == "txt" or extension == "bin":
                path = pathlib.Path(output_type)
                with open(path, mode="w") as file:
                    if isinstance(result, bytes):
                        result = result.decode()
                    file.write(result)
        # If the output is the name of the file with no extension, determine the extension then write to the file
        else:
            if encryption_type == CryptoMode.EN:
                extension = ".bin"
                mode = "wb"
                if isinstance(result, str):
                    result = result.encode()
            else:
                extension = ".txt"
                mode = "w"
                if isinstance(result, bytes):
                    result = result.decode()
            file_name = output_type + extension
            path = pathlib.Path(file_name)
            with open(path, mode=mode) as file:
                file.write(result)

        print("OutputHandler: Output handled successfully")
        request.change_state(None)