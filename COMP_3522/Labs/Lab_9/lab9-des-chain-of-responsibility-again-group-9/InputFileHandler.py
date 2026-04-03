from Handler import Handler



class InputFileHandler(Handler):

    def next(self, request):

        if request.input_file is None:
            if self.next_handler:
                print("InputFileHandler: Input file not specified (handler skipped)")
                request.change_state(self.next_handler)
                return

        try:
            with open(request.input_file, "rb") as f:
                request.data_input = f.read()
            print(f"InputFileHandler: Input file '{request.input_file}' ")

        except FileNotFoundError:
            print(f"InputFileHandler: Input file '{request.input_file}' not found")
            return

        request.change_state(self.next_handler)