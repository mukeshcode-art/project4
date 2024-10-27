
log_file_path = "key_log.txt"

def log_key(key):
    with open(log_file_path, "a") as log_file:
        log_file.write(key)

def main():
    print("Simple Keylogger Simulation. Type 'exit' to stop logging.")
    
    while True:
       
        key = input("Enter key (or 'exit' to stop): ")

        
        if key.lower() == "exit":
            print("Keylogger stopped.")
            break

        
        if key == " ":
            log_key(" [space] ")
        elif key == "\n":
            log_key("\n")
        elif key.lower() == "enter":
            log_key("\n")
        elif key:
            log_key(f"{key}")

if __name__ == "__main__":
    main()
