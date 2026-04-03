from Handler import Handler

class KeyHandler(Handler):

    def next(self, request):

        # Check key length is 8, 16, or 24
        if len(request.key) not in [8, 16, 24]:
            print(f"Error: Invalid key length '{len(request.key)}'. "
                  f"Key must be 8, 16, or 24 characters.")
            return

        print(f"KeyHandler: Key is valid (length={len(request.key)})")

        # Pass to next handler in the chain
        request.change_state(self.next_handler)