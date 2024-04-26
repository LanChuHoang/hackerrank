import hashlib


def sha256(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


def find_nonce(n, base_string, padding_char="0"):
    nonce = 1000  # equivalent to ee(1e3) initializing nonce
    while True:
        # Prepare the input by concatenating the base string with the padded nonce
        input_string = f"{base_string}{str(nonce).rjust(32, padding_char)}"
        hashed = sha256(input_string)
        print(input_string, hashed)

        # Check if the first n characters of the hash are zeros
        if int(hashed[:n], 16) == 0:
            print(hashed[:n])
            # return nonce
            return input_string

        nonce += 1
        # Optional: delay to prevent excessive CPU usage, can be adjusted or removed
        # time.sleep(0.01)


# Usage example
n = 4  # Number of leading zeros in the hash
base_string = "PSUl3lw1fQWLcXqpNOc7JVPhXIvrMKx0"  # The initial part of the input to the hash function
found_nonce = find_nonce(n, base_string)
print(f"Found nonce: {found_nonce}")
