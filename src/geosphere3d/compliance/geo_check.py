from pathlib import Path

class GeoComplianceCheck:
    def check(self, path: Path) -> dict:
        checks = []
        has_config = (path / ".geosphere3d" / "compliance.json").exists()
        checks.append({"standard": "OPEN-DATA", "name": "Open Data", "passed": has_config, "detail": "Compliance config found" if has_config else "No compliance config"})
        has_license = any(f.name.startswith("LICENSE") for f in path.iterdir() if f.is_file())
        checks.append({"standard": "OPEN-SOURCE", "name": "Open Source License", "passed": has_license, "detail": "License found" if has_license else "No license"})
        has_security = any(f.name == "SECURITY.md" for f in path.iterdir() if f.is_file())
        checks.append({"standard": "SECURITY", "name": "Security Policy", "passed": has_security, "detail": "Security policy found" if has_security else "No security policy"})
        has_governance = any(f.name == "GOVERNANCE.md" for f in path.iterdir() if f.is_file())
        checks.append({"standard": "GOVERNANCE", "name": "Governance", "passed": has_governance, "detail": "Governance found" if has_governance else "No governance"})
        has_docs = any(f.name.startswith("README") for f in path.iterdir() if f.is_file())
        checks.append({"standard": "ATTRIBUTION", "name": "Data Attribution", "passed": has_docs, "detail": "Documentation with attribution" if has_docs else "No documentation"})
        has_data = any(f.suffix in (".geojson", ".json", ".czml", ".kml") for f in path.rglob("*") if f.is_file())
        checks.append({"standard": "OPEN-STANDARDS", "name": "Open Formats", "passed": has_data, "detail": "Open geo formats found" if has_data else "No open format data"})
        required_passed = all(c["passed"] for c in checks if c["standard"] in ("OPEN-DATA", "SECURITY", "GOVERNANCE"))
        return {"checks": checks, "passed": required_passed, "total": len(checks), "passed_count": sum(1 for c in checks if c["passed"])}
