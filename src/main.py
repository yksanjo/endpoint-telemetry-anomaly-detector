from datetime import datetime, timezone


def main() -> None:
    print("endpoint-telemetry-anomaly-detector initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
