ECHO Test 1
python crypto.py abcd1234 -s "Test data to be encrypted"

ECHO Test 2
python crypto.py abcd1234 -f "inputFile.txt"

ECHO Test 3
python crypto.py -f "inputFile.txt" abcd1234

ECHO Test 4
python crypto.py abcd1234 --file "inputFile.txt"

ECHO Test 5
python crypto.py abcd1234 -f "inputFile.txt" -m en

ECHO Test 6
python crypto.py abcd1234 -f "test_byte.txt" -m de

ECHO Test 7
python crypto.py abcd1234 -f "test_byte.txt" -m de --output print

ECHO Test 8
python crypto.py abcd1234 -s "Some Test Data that is encrypted" -m de --output "outputFile.txt"