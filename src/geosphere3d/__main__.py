import sys, json, argparse; from pathlib import Path; from geosphere3d import __version__

def build_parser():
    p = argparse.ArgumentParser(prog="geosphere3d", description="GeoSphere3D - 3D Geospatial Toolkit")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="command")
    sub.add_parser("init", help="Initialize geospatial project").add_argument("name")
    sub.add_parser("validate", help="Validate geospatial config").add_argument("path", nargs="?", default=".")
    sub.add_parser("convert", help="Convert geospatial data").add_argument("input").add_argument("--from", dest="from_fmt").add_argument("--to", dest="to_fmt")
    sub.add_parser("compliance", help="Check geospatial compliance").add_argument("path", nargs="?", default=".")
    sub.add_parser("audit", help="Audit geospatial project").add_argument("path", nargs="?", default=".")
    return p

def main(argv=None):
    args = build_parser().parse_args(argv)
    if not args.command:
        build_parser().print_help(); return 0
    if args.command == "init":
        from geosphere3d.core.project import GeoProject
        print(json.dumps(GeoProject().create(args.name), indent=2)); return 0
    elif args.command == "validate":
        from geosphere3d.core.validator import GeoValidator
        r = GeoValidator().validate(Path(args.path))
        [print(f"  [{'PASS' if c['passed'] else 'FAIL'}] {c['name']}: {c['detail']}") for c in r["checks"]]
        return 0 if r["passed"] else 1
    elif args.command == "convert":
        from geosphere3d.core.converter import GeoConverter
        print(json.dumps(GeoConverter().convert(args.input, args.from_fmt, args.to_fmt), indent=2)); return 0
    elif args.command == "compliance":
        from geosphere3d.compliance.geo_check import GeoComplianceCheck
        r = GeoComplianceCheck().check(Path(args.path))
        [print(f"  [{'PASS' if c['passed'] else 'FAIL'}] {c['standard']}: {c['detail']}") for c in r["checks"]]
        return 0 if r["passed"] else 1
    elif args.command == "audit":
        from geosphere3d.compliance.audit import GeoAuditor
        print(json.dumps(GeoAuditor().audit(Path(args.path)), indent=2)); return 0

if __name__ == "__main__":
    sys.exit(main())
