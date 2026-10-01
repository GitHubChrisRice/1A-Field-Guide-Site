#!/usr/bin/env python3
"""Validate the public nationwide jurisdiction shell against its canonical dataset."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
JUR_DIR=ROOT/"docs"/"jurisdictions"
DATA_PATH=JUR_DIR/"jurisdictions.json"
EXPECTED={
"FED":"Federal",
"AL":"Alabama",
"AK":"Alaska",
"AZ":"Arizona",
"AR":"Arkansas",
"CA":"California",
"CO":"Colorado",
"CT":"Connecticut",
"DE":"Delaware",
"FL":"Florida",
"GA":"Georgia",
"HI":"Hawaii",
"ID":"Idaho",
"IL":"Illinois",
"IN":"Indiana",
"IA":"Iowa",
"KS":"Kansas",
"KY":"Kentucky",
"LA":"Louisiana",
"ME":"Maine",
"MD":"Maryland",
"MA":"Massachusetts",
"MI":"Michigan",
"MN":"Minnesota",
"MS":"Mississippi",
"MO":"Missouri",
"MT":"Montana",
"NE":"Nebraska",
"NV":"Nevada",
"NH":"New Hampshire",
"NJ":"New Jersey",
"NM":"New Mexico",
"NY":"New York",
"NC":"North Carolina",
"ND":"North Dakota",
"OH":"Ohio",
"OK":"Oklahoma",
"OR":"Oregon",
"PA":"Pennsylvania",
"RI":"Rhode Island",
"SC":"South Carolina",
"SD":"South Dakota",
"TN":"Tennessee",
"TX":"Texas",
"UT":"Utah",
"VT":"Vermont",
"VA":"Virginia",
"WA":"Washington",
"WV":"West Virginia",
"WI":"Wisconsin",
"WY":"Wyoming",
"DC":"District of Columbia",
}
QUALIFICATION={"Inactive","Field Guide Development","Active"}
FACILITY={"Unresearched","Researching","Established"}

def fail(message:str)->None:
    raise SystemExit(f"jurisdiction-shell: {message}")

def main()->None:
    data=json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rows=data.get("jurisdictions",[])
    if len(rows)!=52: fail(f"expected 52 jurisdiction records, found {len(rows)}")
    by_code={}
    slugs=set()
    for row in rows:
        code=row["code"]
        if code in by_code: fail(f"duplicate code {code}")
        by_code[code]=row
        slug=row["slug"]
        if slug in slugs: fail(f"duplicate slug {slug}")
        slugs.add(slug)
        status=row["qualification_status"]
        maturity=row.get("facility_research_status")
        if status not in QUALIFICATION: fail(f"{code}: invalid qualification_status {status!r}")
        if status=="Active":
            if maturity not in FACILITY: fail(f"{code}: Active requires facility_research_status")
        elif maturity is not None:
            fail(f"{code}: facility_research_status must be null before Active")
        page=JUR_DIR/f"{slug}.md"
        if not page.exists(): fail(f"{code}: missing generated page {page.relative_to(ROOT)}")
        text=page.read_text(encoding="utf-8")
        marker=(f"<!-- generated-from: jurisdictions.json; code: {code}; "
                f"qualification_status: {status}; facility_research_status: "
                f"{'null' if maturity is None else maturity} -->")
        if marker not in text: fail(f"{code}: page marker does not match canonical dataset")
        visible_label = (
            "Not yet qualified" if status == "Inactive"
            else "Field Guide in development" if status == "Field Guide Development"
            else f"Field Guide active — {maturity}"
        )
        if f"<strong>{visible_label}</strong>" not in text:
            fail(f"{code}: visible status label does not match canonical dataset")
        if row["summary"] not in text:
            fail(f"{code}: visible summary does not match canonical dataset")
    if set(by_code)!=set(EXPECTED):
        fail(f"jurisdiction set mismatch; missing={sorted(set(EXPECTED)-set(by_code))} extra={sorted(set(by_code)-set(EXPECTED))}")
    for code,name in EXPECTED.items():
        if by_code[code]["name"]!=name: fail(f"{code}: expected name {name!r}, got {by_code[code]['name']!r}")
    if by_code["CA"]["qualification_status"]!="Active": fail("California must remain Active after formal activation unless a deliberate deactivation changes the canonical dataset")
    if by_code["FED"]["qualification_status"]!="Field Guide Development": fail("Federal must remain Field Guide Development until formal activation")
    county_path=ROOT/"docs"/"california"/"county-coverage-units.json"
    if not county_path.exists(): fail("California Active status requires county-coverage-units.json")
    county_data=json.loads(county_path.read_text(encoding="utf-8"))
    units=county_data.get("units",[])
    if len(units)!=58: fail(f"California county inventory must contain 58 units, found {len(units)}")
    geoids=[u.get("stable_geographic_code") for u in units]
    if len(set(geoids))!=58: fail("California county inventory contains duplicate geographic codes")
    expected_geoids={f"06{i:03d}" for i in range(1,116,2)}
    if set(geoids)!=expected_geoids:
        fail(f"California county GEOID set mismatch; missing={sorted(expected_geoids-set(geoids))} extra={sorted(set(geoids)-expected_geoids)}")
    for unit in units:
        if unit.get("state_jurisdiction_id")!="CA": fail(f"county unit {unit.get('id')}: state_jurisdiction_id must be CA")
        if unit.get("unit_type")!="county": fail(f"county unit {unit.get('id')}: unit_type must be county")
        if unit.get("coverage_status") not in FACILITY: fail(f"county unit {unit.get('id')}: invalid coverage_status")
        if not unit.get("inventory_source_ref"): fail(f"county unit {unit.get('id')}: missing inventory_source_ref")
    rank={"Unresearched":0,"Researching":1,"Established":2}
    county_statuses=[u.get("coverage_status") for u in units]
    aggregate=("Established" if all(s=="Established" for s in county_statuses)
               else "Researching" if any(rank[s]>=1 for s in county_statuses)
               else "Unresearched")
    if county_data.get("facility_research_status")!=aggregate:
        fail(f"California county aggregate status mismatch; expected {aggregate}, got {county_data.get('facility_research_status')!r}")
    if by_code["CA"].get("facility_research_status")!=aggregate:
        fail(f"California jurisdiction facility_research_status must match county aggregate {aggregate}")
    index=(JUR_DIR/"index.md").read_text(encoding="utf-8")
    home=(ROOT/"docs"/"index.md").read_text(encoding="utf-8")
    active=sum(r["qualification_status"]=="Active" for r in rows)
    development=sum(r["qualification_status"]=="Field Guide Development" for r in rows)
    inactive=sum(r["qualification_status"]=="Inactive" for r in rows)
    index_snapshot=f"{active} Active · {development} Field Guide Development · {inactive} Not yet qualified"
    if index_snapshot not in index:
        fail("nationwide index snapshot counts do not match canonical dataset")
    for expected in (
        f"**{active} Active**",
        f"**{development} Field Guide Development:**",
        f"**{inactive} Not yet qualified**",
    ):
        if expected not in home:
            fail(f"home-page status summary does not match canonical dataset: {expected}")
    for row in rows:
        if f'href="{row["slug"]}/"' not in index: fail(f"{row['code']}: nationwide index missing jurisdiction link")
    generated={p.stem for p in JUR_DIR.glob("*.md") if p.name!="index.md"}
    if generated!=slugs: fail(f"generated page set differs from dataset; missing={sorted(slugs-generated)} extra={sorted(generated-slugs)}")
    print("jurisdiction-shell: OK — "
          f"{len(rows)} jurisdictions; "
          f"{sum(r['qualification_status']=='Active' for r in rows)} Active; "
          f"{sum(r['qualification_status']=='Field Guide Development' for r in rows)} Development; "
          f"{sum(r['qualification_status']=='Inactive' for r in rows)} Inactive")
if __name__=="__main__":
    main()
