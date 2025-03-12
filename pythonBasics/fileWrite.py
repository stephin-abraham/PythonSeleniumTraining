from urllib3.filepost import writer

with open('demo.txt', 'r') as reader:
    content=reader.readlines()
    #reverse the content
    reversed(content)
    with open('demo.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
