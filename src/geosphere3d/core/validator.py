from pathlib import Path

class GeoValidator:
    def validate(self, path: Path) -> dict:
        checks = []
        has_config = any(f.name in ("geospatial.yaml", "geospatial.yml", "geospatial.json") for f in path.iterdir() if f.is_file())
        checks.append({"name": "Geo config", "passed": has_config, "detail": "Config found" if has_config else "No geospatial config"})
        has_readme = any(f.name.startswith("README") for f in path.iterdir() if f.is_file())
        checks.append({"name": "Documentation", "passed": has_readme, "detail": "README found" if has_readme else "No README"})
        has_license = any(f.name.startswith("LICENSE") for f in path.iterdir() if f.is_file())
        checks.append({"name": "License", "passed": has_license, "detail": "License found" if has_license else "No license"})
        has_compliance = (path / ".geosphere3d" / "compliance.json").exists()
        checks.append({"name": "Compliance config", "passed": has_compliance, "detail": "Compliance config found" if has_compliance else "No compliance config"})
        has_data = any(f.suffix in (".geojson", ".json", ".czml", ".kml", ".gml") for f in path.rglob("*") if f.is_file())
        checks.append({"name": "Geo data files", "passed": has_data, "detail": "Geo data found" if has_data else "No geospatial data files"})
        has_code = any(f.suffix == ".py" for f in path.rglob("*") if f.is_file() and ".venv" not in str(f))
        checks.append({"name": "Source code", "passed": has_code, "detail": "Code found" if has_code else "No source code"})
        has_security = any(f.name == "SECURITY.md" for f in path.iterdir() if f.is_file())
        checks.append({"name": "Security policy", "passed": has_security, "detail": "Security policy found" if has_security else "No security policy"})
        return {"checks": checks, "passed": all(c["passed"] for c in checks if c["name"] in ("Geo config", "Documentation", "License", "Compliance config")), "total": len(checks), "passed_count": sum(1 for c in checks if c["passed"])}
