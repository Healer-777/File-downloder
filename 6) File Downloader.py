import requests

# Head
print("_____Files Downloader_____")
print("you can download images, videos, documents,... from this. ")

print(" ")

# get download url
get_file_url = input("Link to download(url): ")
print("Downloading File...")

# code to connect with the file
r = requests.get(get_file_url)

# give path and name
print("Put a file format that matched to url")
file_name = input("File name & format : ")
file_path = input("Enter the path to download file: ")

# code to download file
with open(file_path + '/' + file_name, 'wb') as f:
    f.write(r.content)

print("File has downloaded!")
