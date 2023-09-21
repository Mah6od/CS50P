file_name = input("File name: ").lower().strip()

file_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

extentions = None

if '.' in file_name:
    parts = file_name.split('.')
    extentions = '.' + parts[-1]

if extentions in file_types:
    file_types = file_types[extentions]
else:
    file_types = "application/octet-stream"

print(file_types)