import requests

def scan_github_repository(repository_url):
    # Retrieve the repository information
    response = requests.get(f"https://api.github.com/repos/{repository_url}")

    if response.status_code != 200:
        print("Failed to retrieve repository information.")
        return
    repository = response.json()

    if repository["private"]:
        print("The repository is private.")
        return
    # Retrieve repository contents
    response = requests.get(repository["contents_url"].replace("{+path}", ""))

    if response.status_code != 200:
        print("Failed to retrieve repository contents.")
        return
    contents = response.json()

    # Go through the repository and check for exposed secrets in files
    for file in contents:
        if file["type"] != "file":
            continue
        print(f"Scanning file: {file['name']}")
        # Retrieve file content
        file_response = requests.get(file["download_url"])

        if file_response.status_code != 200:
            continue
        file_content = file_response.text
        
        if "secret" in file_content:
            print(f"Secrets found in file: {file['name']}\n")
            print(file_content)

def main():
    scan_github_repository("YM2992/41182SystemSecurity")

if __name__ == "__main__":
    main()


