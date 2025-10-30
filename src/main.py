# main.py
"""
Version Control Best Practices for LAC Projects
Author: Bommaraju Haritha
"""

def show_best_practices():
    practices = [
        "1. Use meaningful commit messages.",
        "2. Create branches for new features or fixes.",
        "3. Review and merge using pull requests.",
        "4. Keep documentation updated.",
        "5. Avoid committing large files or sensitive data.",
        "6. Sync your fork or branch regularly.",
    ]
    print("Version Control Best Practices:\n")
    for p in practices:
        print(p)

if __name__ == "__main__":
    show_best_practices()
