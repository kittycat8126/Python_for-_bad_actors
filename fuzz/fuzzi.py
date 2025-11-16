import requests
import sys
import time
import random
import argparse
from param_fuzzer import fuzz_params
from tqdm import tqdm

base_url = "http://127.0.0.1:3000"

min_delay = 0.1
max_delay = 0.5

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "curl/7.81.0",
    "Wget/1.21.1",
    "python-requests/2.31.0"
]

def get_headers():
    return {"User-Agent": random.choice(user_agents)}


# ------------------------------
# READ WORDLIST
# ------------------------------
def load_wordlist(path):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {path}")
        sys.exit(1)


# ------------------------------
# ENDPOINT DISCOVERY
# ------------------------------
def endpoint_discovery(words):
    endpoints = []

    for word in tqdm(words, desc="Discovering endpoints", unit="req"):
        url = f"{base_url}/{word}"

        try:
            res = requests.get(url, headers=get_headers())
            if res.status_code == 404:
                continue

            print(f"[+] Endpoint discovered : {url} ({res.status_code})")
            endpoints.append(word)

        except Exception as e:
            print("Error:", e)

        time.sleep(random.uniform(min_delay, max_delay))

    return endpoints


# ------------------------------
# SAFE INPUT
# ------------------------------
def safe_input(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()        # <-- FIX
    with open("/dev/tty", "r") as tty:
        return tty.readline().strip()



# ------------------------------
# MAIN
# ------------------------------
def main():

    # ARGPARSE → handle -w / --wordlist
    parser = argparse.ArgumentParser(description="API Fuzzer")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    args = parser.parse_args()

    words = load_wordlist(args.wordlist)

    endpoints = endpoint_discovery(words)

    if not endpoints:
        print("[-] No endpoints discovered.")
        return

    print("\n[+] Discovered endpoints:")
    for i, ep in enumerate(endpoints, 1):
        print(f"{i}) /{ep}")

    selection = safe_input("\nSelect endpoints to fuzz (e.g. 1,3): ")

    try:
        selected_indices = [int(x) for x in selection.split(",")]
    except:
        print("[!] Invalid endpoint selection.")
        return

    codes_input = safe_input("Show only which status codes? (e.g. 200,400,500): ")

    try:
        allowed_codes = [int(c.strip()) for c in codes_input.split(",")]
    except:
        print("[!] Invalid status code list.")
        return

    print(f"\n[+] Showing only responses with status codes: {allowed_codes}\n")

    for idx in selected_indices:
        if 1 <= idx <= len(endpoints):
            fuzz_params(base_url, endpoints[idx - 1], get_headers, allowed_codes)
        else:
            print(f"[!] Invalid endpoint index: {idx}")


if __name__ == "__main__":
    main()
