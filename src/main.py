import argparse, os, time, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default=os.getenv("APP_ENV", "dev"))
    parser.add_argument("--run-id", default=os.getenv("RUN_ID", "local"))
    args = parser.parse_args()

    api_key = os.getenv("API_KEY")
    print(f"[pipeline] env={args.env} run_id={args.run_id} api_key_set={bool(api_key)}")
    time.sleep(1)
    print("[pipeline] done.")

if __name__ == "__main__":
    sys.exit(main())
