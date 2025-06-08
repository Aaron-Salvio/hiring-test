import requests

API_URL = "https://api.recruitment.shq.nz"
API_KEY = "h523hDtETbkJ3nSJL323hjYLXbCyDaRZ"
CLIENT_ID = 100


def get_domains():
    response = requests.get(f"{API_URL}/domains/{CLIENT_ID}?api_key={API_KEY}")
    response.raise_for_status()
    return response.json()


def get_zone_records(zone_id):
    response = requests.get(f"{API_URL}/zones/{zone_id}?api_key={API_KEY}")
    response.raise_for_status()
    return response.json()


def main():
    domains_data = get_domains()

    print("=== Domains and DNS Records ===")
    for domain in domains_data:
        print(f"\n📦 Domain: {domain['name']}")

        for zone in domain.get("zones", []):
            # 🧪 Print the raw zone data for debugging
            print(f"  🔍 Raw zone data: {zone}")

            zone_id = zone.get("zone_id") or zone.get("id")
            if not zone_id:
                print("  ⚠️ Zone is missing 'id' or 'zone_id' key. Skipping.")
                continue

            print(f"  🌐 Zone ID: {zone_id}")

            records = get_zone_records(zone_id)

            for record in records:
                record_type = record.get("type", "UNKNOWN")
                name = record.get("name", "No Name")
                value = record.get("value", "No Value")
                print(f"    🧾 Record: {record_type} | {name} -> {value}")


if __name__ == "__main__":
    main()
