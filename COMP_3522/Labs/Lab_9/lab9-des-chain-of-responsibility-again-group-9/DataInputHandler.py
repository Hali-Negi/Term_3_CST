from Handler import Handler


class DataInputHandler(Handler):

    def next(self, request):
        """
        Handles that the request has a non-empty string as the data.
        :param request: The Request to be handled
        """
        try:
            if request.data_input is None:
                raise ValueError
            if len(request.data_input) == 0:
                raise ValueError

            print("DataInputHandler: Data input is valid")
            request.change_state(self.next_handler)
        except ValueError:
            print("DataInputHandler: Data input is not valid")
