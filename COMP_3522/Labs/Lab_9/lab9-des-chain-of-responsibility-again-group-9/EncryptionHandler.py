import base64
from tokenize import String

from des import DesKey
from Handler import Handler


class EncryptionHandler(Handler):

    def next(self, request):
        # Convert key to bytes
        key = DesKey(request.key.encode())
        if not isinstance(request.data_input, bytes):
            request.data_input = request.data_input.encode()

        # Encrypt the data
        request.result = key.encrypt(request.data_input, padding=True)
        request.result = base64.b64encode(request.result).decode()

        print("EncryptionHandler: Data encrypted successfully")

        request.change_state(self.next_handler)



