# vulnerable_code.py

# A classic insecure query using an f-string
user_id = "101"
query = f"SELECT * FROM users WHERE id = '{user_id}'"
api_key = "sk-12345-secret-key"
password = "supersecretpassword"
print("Executing: " + query)