import concurrent.futures
import pprint
import PyPDF4

def crack_password(password):
    # Open the PDF file in read-binary mode
    with open('FileName.pdf', 'rb') as file:
        # Create a PDF object
        pdf = PyPDF4.PdfFileReader(file)

        # Try to decrypt the PDF using the given password
        if pdf.decrypt(password):
            pprint.pprint('Found password: ' + password)
            return password
        else:
            return None

# Set the known password prefix
password_prefix = '12345'

# Create a list of passwords to try
passwords = []

# Open the wordlist file
with open('wordlist1.txt', 'r') as wordlist:
    # Read through the wordlist, appending each word to the known password prefix
    for word in wordlist:
        passwords.append(password_prefix + word.strip())

# Use a concurrent.futures.ThreadPoolExecutor to try the passwords in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(crack_password, password) for password in passwords]

    # Print a success message for each completed future that returns a result
    for future in concurrent.futures.as_completed(results):
        result = future.result()
        if result:
            pprint.pprint('Found password: ' + result)
            break
        else:
            pprint.pprint('Not Found')
