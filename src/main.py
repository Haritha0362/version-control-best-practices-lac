# main.py
# Sample Python file for LAC Version Control Project

def welcome_message():
    return "Welcome to the LAC Version Control Project!"

def list_best_practices():
    practices = [
        "Use meaningful commit messages",
        "Create branches for new features",
        "Use .gitignore to avoid unnecessary files",
        "Review pull requests before merging",
        "Keep documentation updated"
    ]
    return practices

if __name__ == "__main__":
    print(welcome_message())
    for p in list_best_practices():
        print("-", p)

