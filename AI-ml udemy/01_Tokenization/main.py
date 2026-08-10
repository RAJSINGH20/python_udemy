import tiktoken


# Get the tokenizer for GPT-4o
enc = tiktoken.encoding_for_model("gpt-4o")


# Text to encode
text = "hey there my name is raj singh"

# Encode text into tokens
tokens = enc.encode(text)

print("After Encoded the token will be :")
print(tokens)
# Example output:
# [48467, 1354, 922, 1308, 382, 46358, 6211, 71]


# Decode tokens back into text
decoded = enc.decode(tokens)

print("After Decoded the token will be :")
print(decoded)