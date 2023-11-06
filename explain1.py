import hashlib

difficulty = 3

def calculate_hash(nonce):
    data = "test" + str(nonce)
    return hashlib.sha256(data.encode()).hexdigest()

def find_hash(difficulty):
    nonce = 0
    prefix = '0' * difficulty

    while True:
        hash_value = calculate_hash(nonce)
        if hash_value[:difficulty] == prefix:
            return hash_value
        nonce += 1

hash_result = find_hash(difficulty)
print(f"Hash value with difficulty {difficulty}: {hash_result}")
