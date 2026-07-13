import json; from pathlib import Path

class GeoProject:
    def create(self, name: str) -> dict:
        d = Path.cwd() / name; d.mkdir(parents=True, exist_ok=True)
        for fname, content in {
            "geospatial.yaml": f'service:\n  name: "{name}"\n  type: 3d-geospatial\n  format: Cesium3DTiles\n  projection: EPSG:4326\ncompliance:\n  open_data: true\n  attribution: true\n  licensing: true\n',
            "README.md": f"# {name}\n\n3D geospatial project scaffolded with GeoSphere3D.\n",
        }.items():
            (d / fname).write_text(content)
        compliance_dir = d / ".geosphere3d"; compliance_dir.mkdir(exist_ok=True)
        (compliance_dir / "compliance.json").write_text(json.dumps({
            "compliance_baked_in": True, "standards": ["OPEN-DATA", "ATTRIBUTION", "OPEN-STANDARDS"], "version": "0.1.0",
        }, indent=2))
        for x in ["data", "tiles", "docs", "tests"]: (d / x).mkdir(exist_ok=True); (d / x / ".gitkeep").write_text("")
        return {"project": name, "directory": str(d), "compliance": "baked in"}
