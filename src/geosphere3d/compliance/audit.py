from pathlib import Path; from datetime import datetime, timezone

class GeoAuditor:
    def audit(self, path: Path) -> dict:
        findings = []; recommendations = []
        config_files = [f for f in path.iterdir() if f.is_file() and f.name.endswith((".yaml",".yml",".json"))]
        for cfg in config_files:
            try:
                content = cfg.read_text()
                if "geospatial" in content.lower() or "cesium" in content.lower() or "gis" in content.lower():
                    findings.append({"type": "config", "file": cfg.name, "detail": "Geospatial configuration found"})
                if "projection" in content.lower():
                    recommendations.append({"type": "projection", "detail": "Document coordinate reference system"})
            except: pass
        has_compliance = (path / ".geosphere3d" / "compliance.json").exists()
        if has_compliance:
            findings.append({"type": "compliance", "detail": "Compliance configuration present"})
        if not any(f.name == "SECURITY.md" for f in path.iterdir() if f.is_file()):
            recommendations.append({"type": "security", "detail": "Add SECURITY.md"})
        return {"findings": findings, "recommendations": recommendations, "total_findings": len(findings), "total_recommendations": len(recommendations), "audited_at": datetime.now(timezone.utc).isoformat()}
