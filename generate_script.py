def generate_script(topic):
    return f"""
HOOK: This is what would happen if you used {topic} every day...

BODY:
Most people ignore this, but {topic} can completely change your results.
The problem is that no one explains it properly.
Once you understand this, everything becomes easier.

CTA:
If you see the orange cart, don’t think twice.
"""

if __name__ == "__main__":
    topic = input("Enter topic: ")
    print(generate_script(topic))
