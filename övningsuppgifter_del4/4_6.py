import hashlib
# print(hashlib.algorithms_guaranteed)
# hash_object = hashlib.md5(b"Hello World")
# print(hash_object.hexdigest())

def create_hash(path):
    file = open(path, "rb")
    file_content = file.read()
    file.close()
    file_hash = hashlib.sha1(file_content)
    return file_hash.hexdigest()

print(create_hash("C:/Test/test.txt"))