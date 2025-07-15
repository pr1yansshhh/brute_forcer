import zipfile
import time

def brute_force_zip(zip_file, wordlist):
    try:
        zf = zipfile.ZipFile(zip_file)
    except FileNotFoundError:
        print("❌ ZIP file not found!")
        return

    with open(wordlist, 'r') as file:
        passwords = file.readlines()

    start_time = time.time()
    for pwd in passwords:
        pwd = pwd.strip()
        try:
            zf.extractall(pwd=pwd.encode('utf-8'))
            print(f"\n✅ Password found: {pwd}")
            print(f"⏱️ Time taken: {round(time.time() - start_time, 2)} seconds")
            return
        except:
            print(f"❌ Tried: {pwd}")
    print("\n❌ Password not found in wordlist.")

# Run it
brute_force_zip('secret.zip', 'wordlist.txt')
