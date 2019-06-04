import os

length = 4

# The file's name respect the format. 0042.png
is_valid = lambda s: len(s) == length and s.isdigit()

# Return the name without extension. foo.png -> foo
clean = lambda s: s[:s.rfind('.')] if '.' in s else s

# Given an integer k return the equivalent in string valid format. 42 -> 0042
make_name = lambda k: '0' * (length - len(str(k))) + str(k)

valid_names = {name for name in sorted(os.listdir()) if is_valid(clean(name))}
not_valid_names = set(os.listdir()) - valid_names

previous_name = '0' * length
valid_names.remove(__file__)
for name in sorted(valid_names):
	if clean(name) != make_name(int(clean(previous_name)) + 1):
		not_valid_names.add(name)
		valid_names.remove(name)
	else:
		previous_name = clean(name)

last_valid_name = previous_name
for name in list(not_valid_names):
	new_name = make_name(int(last_valid_name) + 1) + name[name.rfind("."):]
	last_valid_name = clean(new_name)
	input(f'Renaming <{name}> into <{new_name}>. Press Enter..')
	os.rename(name, new_name)
	print('Done ✔.')
