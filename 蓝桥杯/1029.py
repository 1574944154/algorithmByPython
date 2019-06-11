
ok_keys_str = input()
no_keys_str = input()

error_keys = set(list(ok_keys_str.upper()))-set(list(no_keys_str.upper()))

res_keys = []

for c in ok_keys_str.upper():
    if(c in error_keys and c not in res_keys):
        res_keys.append(c)

print("".join(res_keys))