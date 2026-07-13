from pathlib import Path; import json, pytest

@pytest.fixture
def geo_project(tmp_path):
    p = tmp_path / "my-geo"; p.mkdir()
    (p / "README.md").write_text("# Geo\n")
    (p / "LICENSE").write_text("Apache-2.0")
    (p / "SECURITY.md").write_text("# Security\n")
    (p / "GOVERNANCE.md").write_text("# Governance\n")
    (p / "geospatial.yaml").write_text("service:\n  name: test\n")
    (p / "data.geojson").write_text('{"type": "FeatureCollection"}')
    (p / ".geosphere3d").mkdir(); (p / ".geosphere3d" / "compliance.json").write_text(json.dumps({"ok": True}))
    return p

@pytest.fixture
def empty_geo(tmp_path):
    p = tmp_path / "empty"; p.mkdir(); return p
