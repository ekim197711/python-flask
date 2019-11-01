import secrets

mysecret = secrets.token_hex(18)
print(f'My new secret: { mysecret }')