import requests
import random
import time
from tqdm import tqdm

def jitter():
    time.sleep(random.uniform(0.1, 0.35))

def should_show(res, allowed_codes):
    return (allowed_codes is None) or (res.status_code in allowed_codes)

# Your lists remain the same
COMMON_PARAM_NAMES = [
    "id", "user", "username", "email", "q", "debug", "search",
    "token", "page", "admin", "role", "status", "type", "active"
]

COMMON_PARAM_VALUES = [
    "1", "0", "true", "false", "null", "admin", "test", "guest",
    "A", "abc", "123", "-1", "[]", "{}", "<>", "' OR 1=1 --",
]


def fuzz_params(base_url, path, headers, allowed_codes):
    url = f"{base_url}/{path}"
    print(f"\n[+] Starting parameter fuzzing on: {url}\n")

    # -------------------------------
    # 1) PARAMETER NAME FUZZING
    # -------------------------------
    print("[*] Fuzzing parameter NAMES...")
    for pname in tqdm(COMMON_PARAM_NAMES, desc="Name fuzzing", unit="param"):
        test_url = f"{url}?{pname}=test"
        try:
            res = requests.get(test_url, headers=headers())
            if should_show(res, allowed_codes):
                print(res.status_code, test_url)
        except:
            pass
        jitter()

    # -------------------------------
    # 2) PARAMETER VALUE FUZZING
    # -------------------------------
    print("\n[*] Fuzzing parameter VALUES...")
    for pvalue in tqdm(COMMON_PARAM_VALUES, desc="Value fuzzing", unit="value"):
        test_url = f"{url}?param={pvalue}"
        try:
            res = requests.get(test_url, headers=headers())
            if should_show(res, allowed_codes):
                print(res.status_code, test_url)
        except:
            pass
        jitter()

    # -------------------------------
    # 3) COMBO FUZZING (name + value)
    # -------------------------------
    print("\n[*] Fuzzing NAME + VALUE combos...")
    for pname in tqdm(COMMON_PARAM_NAMES, desc="Combo fuzzing", unit="combo"):
        for pvalue in COMMON_PARAM_VALUES:
            test_url = f"{url}?{pname}={pvalue}"
            try:
                res = requests.get(test_url, headers=headers())
                if should_show(res, allowed_codes):
                    print(res.status_code, test_url)
            except:
                pass
            jitter()

    print("\n[+] Parameter fuzzing completed.\n")
