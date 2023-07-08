

# How can we implement a context manager for our own classes?
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        print("Entered")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception has been handled")
        print("Exit")
        return True

with ManagedFile('notes2.txt') as file:
    print("Doing stuff...")
    file.write("something")
print("Continuing")
