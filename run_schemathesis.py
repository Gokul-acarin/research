import subprocess
import sys


def main(spec_path: str, base_url: str) -> None:
    """Run schemathesis against the given spec and base URL."""
    cmd = ["schemathesis", "run", spec_path, "--base-url", base_url]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_schemathesis.py <spec-path> <base-url>")
        raise SystemExit(1)
    main(sys.argv[1], sys.argv[2])
