def save_script(script):
    with open("output.txt", "w") as f:
        f.write(script)

if __name__ == "__main__":
    topic = input("Enter topic: ")
    script = generate_script(topic)
    print(script)
    save_script(script)
