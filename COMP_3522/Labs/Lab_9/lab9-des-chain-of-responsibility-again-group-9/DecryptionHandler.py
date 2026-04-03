import base64

from des import DesKey
from Handler import Handler


class DecryptionHandler(Handler):

    def next(self, request):
        """
        This handles decryption of a request object. The data_input is considered to be the dext that needs decrypting.
        The key should be the key for decrypting the data_input.
        The data_input is decrypted with the key and the result is stored in the request's result.
        The handler then moves to the next handler.
        :param request: the request object to handle.
        """
        if not isinstance(request.data_input, bytes):
            request.data_input = request.data_input.encode()
        request.data_input = base64.b64decode(request.data_input)

        key = DesKey(request.key.encode())
        result = key.decrypt(request.data_input, padding=True)

        request.result = result.decode()
        print(f"DecryptionHandler: Data decrypted successfully")
        request.change_state(self.next_handler)