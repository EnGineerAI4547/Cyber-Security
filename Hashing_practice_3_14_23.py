

message='mesage'
print(hash(message))
print(hash(message))
print(hash(message))

message='message'
print(hash(message))

print(hash(message))

message1="I love you *****"
print(hash(message))
message2="I love you mi *****"
print(f" The message {message1} has a hash number of {hash(message1)}")

print(f" The message {message2} has a hash number of {hash(message2)}")



print(f" You can see the hash number of the message1 {hash(message1)} isn't the same as the hash number of the message {hash(message2)}")
print(f"But the hash number of the message1 is always {hash(message1)} and the hash of message 2 if always the same {hash(message2)} ")
