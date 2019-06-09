import argparse
import os


# --- Functions ---


# Verify if the file's name respect the format. '0042.png' if length is 4
is_valid = lambda s: s.isdigit() and (len(s) == length if length else s[0] != '0')

# Return the name without extension. 'foo.png' -> 'foo'
clean = lambda s: s[:s.rfind('.')] if '.' in s else s

# '0042' -> '0043'
inc = lambda s: '0' * (length - len(str(int(s) + 1))) + str(int(s) + 1)


# --- Argument Management ---


parser = argparse.ArgumentParser()
# The path where the files are
parser.add_argument('path', help='The path where the files are')
# The length
parser.add_argument('-l', '--length', type=int,
					help='the length of the new names. default = 4')
# Activate the warning message
parser.add_argument('-v', '--verbose', action='store_true',
					help='Display a confirmation message')
args = parser.parse_args()

path = args.path
if not os.path.exists(path):
	raise FileNotFoundError
	exit(1)

length = args.length if args.length else 0
verbose = args.verbose


# --- Script ---

# Loading the list of the names to verify
names = []
for name in sorted(os.listdir(path)):
	if os.path.isfile(os.path.join(path, name)):
		names.append(name)
if path == '.':
	names.remove(__file__)

# Loading the list of invalid names
valid_names = []
invalid_names = []
last_name = '0' * length if length else '0'
for name in names:
	if is_valid(clean(name)) and clean(name) == inc(clean(last_name)):
		valid_names.append(name)
		last_name = clean(name)
	else:
		invalid_names.append(name)

# Renaming the invalid names
for name in invalid_names:
	
	# The new valid name is the incrementation of the last one
	new_name = inc(last_name)
	last_name = new_name

	# Adding the extension
	final_name = new_name + name[name.rfind('.'):]

	# The user confirm the change
	if args.verbose:
		input(f'Renaming <{name}> into <{final_name}>... [Enter/CTRL+C]')
		print('✔ Done ✔.')

	os.rename(os.path.join(path, name), os.path.join(path, final_name))
	
