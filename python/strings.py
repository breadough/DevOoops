def string_negative_indexing():
	b = "Hello, World!"
	print(b[-5:-2])

def string_slicing():
	b = "Hello World!"
	print(b[2:5])

def string_slice_from_start():
	b = "Hello World!"
	print(b[:5])

def string_slice_to_end():
	b = "Hello World!"
	print(b[2:])

def string_to_upper(b):
	print(b.upper())

def string_to_lower(b):
	print(b.lower())

def string_strip(b):
	print(b.strip())

def string_replace(a):
	print(a.replace("H","G"))

def string_format():
	x = 5
	txt = 'This is text and a number {}'
	print(txt.format(x))

#main function
b = "Hello, World!  "
print(b)
string_negative_indexing()
string_slicing()
string_slice_from_start()
string_slice_to_end()
string_to_upper(b)
string_to_lower(b)
string_strip(b)
string_replace(b)
string_format()

txt = "Company12"

x = txt.isalnum()

print(x)