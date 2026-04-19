from pathlib import Path
import json
import re

def parse_ipconfig_file(file_path):
    text = Path(file_path).read_text(encoding="utf-16", errors="ignore")

    adapters = []

    current = None

    for sor in text.splitlines():
        is_indented = sor.startswith(" ") or sor.startswith("\t")
        stripped = sor.strip()

        if not stripped:
            continue

        if not is_indented and stripped.endswith(":") and "Windows IP Configuration" not in stripped:
            if current is not None:
                adapters.append(current)
            current = {
                "adapter_name": stripped[:-1],
                "description": "",
                "physical_address": "",
                "dhcp_enabled": "",
                "ipv4_address": "",
                "subnet_mask": "",
                "default_gateway": "",
                "dns_servers": []
            }
            continue

        if current is None:
            continue

        if " : " in stripped:

            parts = stripped.split(" : ", 1)

            key = parts[0].strip(" .")

            value = parts[1].strip().replace("(Preferred)", "").replace("(Deferred)", "").strip()

            if "Description" in key:
                current["description"] = value
            elif "Physical Address" in key:
                current["physical_address"] = value
            elif "DHCP Enabled" in key:
                current["dhcp_enabled"] = value
            elif "Autoconfiguration IPv4" in key:
                if not current["ipv4_address"]:
                    current["ipv4_address"] = value
            elif "IPv4 Address" in key:
                if not current["ipv4_address"]:
                    current["ipv4_address"] = value
            elif "Subnet Mask" in key:
                current["subnet_mask"] = value
            elif "Default Gateway" in key:
                if value:
                    current["default_gateway"] = value
            elif "DNS Servers" in key:
                if value:
                    current["dns_servers"].append(value)

    if current is not None:
        adapters.append(current)

    return adapters

def main():

    eredmenyek = []

    for file_path in sorted(Path(".").glob("*.txt")):
        adapters = parse_ipconfig_file(file_path)
        eredmenyek.append({
            "file_name": file_path.name,
            "adapters": adapters
        })

    output = json.dumps(eredmenyek, indent=2, ensure_ascii=False)
    print(output)
    Path("output.json").write_text(output, encoding="utf-8")

if name == "main":
    main()