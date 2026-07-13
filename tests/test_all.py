from pathlib import Path
from geosphere3d.core.validator import GeoValidator
from geosphere3d.core.converter import GeoConverter
from geosphere3d.compliance.geo_check import GeoComplianceCheck
from geosphere3d.compliance.audit import GeoAuditor

def test_validate_ok(geo_project):
    assert GeoValidator().validate(geo_project)["passed"] is True
def test_validate_bad(empty_geo):
    assert GeoValidator().validate(empty_geo)["passed"] is False
def test_convert(tmp_path):
    f = tmp_path / "d.json"; f.write_text('{"name": "test"}')
    r = GeoConverter().convert(str(f), "json", "geojson")
    assert "error" in r or r.get("converted") is False
def test_compliance_ok(geo_project):
    assert GeoComplianceCheck().check(geo_project)["passed"] is True
def test_compliance_bad(empty_geo):
    assert GeoComplianceCheck().check(empty_geo)["passed"] is False
def test_audit(geo_project):
    assert GeoAuditor().audit(geo_project)["total_findings"] > 0
