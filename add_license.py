from github import Github
import os

# GitHub credentials
github_username = "ducanh-ho2296"
github_token = "your_token"
repo_name = "create-tsi-test"

# License header to add
license_header = """# SPDX-FileCopyrightText: 2024 Deutsche Telekom AG, LlamaIndex, Vercel, Inc.
#
# SPDX-License-Identifier: MIT
"""

def add_license_to_files(repo):
    # Iterate through all files in the repository
    for file in repo.get_contents(""):
        if file.type == "file":
            # Read the file content
            file_content = file.decoded_content.decode()

            # Check if the license header is already present
            if not file_content.startswith("# SPDX"):
                # Add the license header to the file content
                file_content_with_license = license_header + "\n" + file_content

                # Update the file with the license header
                repo.update_file(file.path, "Add license header", file_content_with_license, file.sha)
                print(f"Added license header to: {file.path}")

def main():
    # Initialize PyGithub with credentials
    g = Github(github_token)

    # Get the repository
    repo = g.get_repo(f"{github_username}/{repo_name}")

    # Add license header to files
    add_license_to_files(repo)

if __name__ == "__main__":
    main()
