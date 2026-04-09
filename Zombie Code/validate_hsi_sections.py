"""
validate_hsi_sections.py
========================
Run this from your project root AFTER running all three notebooks.
It checks that nc_health.csv, nc_mobility.csv, and nc_infrastructure.csv
are present, correctly formatted, and ready for hsi.py to merge.

Usage:
    python validate_hsi_sections.py
"""

import pandas as pd
import sys
import os

PASS = "\033[92m✓\033[0m"
FAIL = "\033[91m✗\033[0m"
WARN = "\033[93m⚠\033[0m"

errors   = []
warnings = []

def check(condition, pass_msg, fail_msg, is_warning=False):
    if condition:
        print(f"  {PASS} {pass_msg}")
    else:
        print(f"  {FAIL if not is_warning else WARN} {fail_msg}")
        (warnings if is_warning else errors).append(fail_msg)

print("=" * 60)
print("HSI SECTION CSV VALIDATION")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# SECTION H — nc_health.csv
# ─────────────────────────────────────────────────────────────
print("\n[ Section H — nc_health.csv ]")

H_PATH = "data/nc_health.csv"
H_REQUIRED_COLS = ["GEOID", "obesity_rate", "ambulatory_disability",
                    "nursing_home_density", "score_H"]

check(os.path.exists(H_PATH), f"File found: {H_PATH}", f"File missing: {H_PATH}")

if os.path.exists(H_PATH):
    df_H = pd.read_csv(H_PATH, dtype={"GEOID": str})

    check(all(c in df_H.columns for c in H_REQUIRED_COLS),
          f"All required columns present: {H_REQUIRED_COLS}",
          f"Missing columns: {[c for c in H_REQUIRED_COLS if c not in df_H.columns]}")

    check(len(df_H) >= 2000,
          f"Row count acceptable: {len(df_H):,} tracts",
          f"Too few tracts: {len(df_H):,} (expected ~2,650)")

    check(df_H["GEOID"].str.startswith("37").all(),
          "All GEOIDs are NC (prefix 37)",
          "Non-NC GEOIDs found in health file")

    check(df_H["GEOID"].str.len().eq(11).all(),
          "All GEOIDs are 11 digits",
          f"Bad GEOID lengths: {df_H['GEOID'].str.len().value_counts().to_dict()}")

    check(df_H["GEOID"].duplicated().sum() == 0,
          "No duplicate GEOIDs",
          f"Duplicate GEOIDs: {df_H['GEOID'].duplicated().sum()}")

    check(df_H["score_H"].between(0, 1).all(),
          f"score_H in [0,1]: range {df_H['score_H'].min():.3f} – {df_H['score_H'].max():.3f}",
          f"score_H out of range: min={df_H['score_H'].min():.3f}, max={df_H['score_H'].max():.3f}")

    null_count = df_H[H_REQUIRED_COLS].isnull().sum().sum()
    check(null_count == 0,
          "No nulls in output columns",
          f"{null_count} null values found in output",
          is_warning=True)

    check(df_H["obesity_rate"].between(15, 65).all(),
          f"Obesity rates plausible: {df_H['obesity_rate'].min():.1f}% – {df_H['obesity_rate'].max():.1f}%",
          f"Implausible obesity values detected",
          is_warning=True)

# ─────────────────────────────────────────────────────────────
# SECTION M — nc_mobility.csv
# ─────────────────────────────────────────────────────────────
print("\n[ Section M — nc_mobility.csv ]")

M_PATH = "data/nc_mobility.csv"
M_REQUIRED_COLS = ["GEOID", "vehicle_access", "transit_dependence",
                    "road_density", "score_M"]

check(os.path.exists(M_PATH), f"File found: {M_PATH}", f"File missing: {M_PATH}")

if os.path.exists(M_PATH):
    df_M = pd.read_csv(M_PATH, dtype={"GEOID": str})

    check(all(c in df_M.columns for c in M_REQUIRED_COLS),
          f"All required columns present",
          f"Missing columns: {[c for c in M_REQUIRED_COLS if c not in df_M.columns]}")

    check(len(df_M) >= 2000,
          f"Row count acceptable: {len(df_M):,} tracts",
          f"Too few tracts: {len(df_M):,} (expected ~2,600+)")

    check(df_M["GEOID"].str.startswith("37").all(),
          "All GEOIDs are NC (prefix 37)",
          "Non-NC GEOIDs found in mobility file")

    check(df_M["GEOID"].str.len().eq(11).all(),
          "All GEOIDs are 11 digits",
          f"Bad GEOID lengths found")

    check(df_M["GEOID"].duplicated().sum() == 0,
          "No duplicate GEOIDs",
          f"Duplicate GEOIDs: {df_M['GEOID'].duplicated().sum()}")

    check(df_M["score_M"].between(0, 1).all(),
          f"score_M in [0,1]: range {df_M['score_M'].min():.3f} – {df_M['score_M'].max():.3f}",
          f"score_M out of range: min={df_M['score_M'].min():.3f}, max={df_M['score_M'].max():.3f}")

    # KEY: check for the RUCA code 99 bug
    neg_road = (df_M["road_density"] < 0).sum()
    check(neg_road == 0,
          "No negative road_density values (RUCA code 99 bug fixed)",
          f"RUCA code 99 bug still present: {neg_road} tracts have negative road_density")

    null_count = df_M[M_REQUIRED_COLS].isnull().sum().sum()
    check(null_count == 0,
          "No nulls in output columns",
          f"{null_count} null values found in output",
          is_warning=True)

# ─────────────────────────────────────────────────────────────
# SECTION I — nc_infrastructure.csv
# ─────────────────────────────────────────────────────────────
print("\n[ Section I — nc_infrastructure.csv ]")

I_PATH = "data/nc_infrastructure.csv"
I_REQUIRED_COLS = ["GEOID", "prepper_density", "covid_compliance",
                    "grid_independence", "score_I"]

check(os.path.exists(I_PATH), f"File found: {I_PATH}", f"File missing: {I_PATH}")

if os.path.exists(I_PATH):
    df_I = pd.read_csv(I_PATH, dtype={"GEOID": str})

    check(all(c in df_I.columns for c in I_REQUIRED_COLS),
          f"All required columns present",
          f"Missing columns: {[c for c in I_REQUIRED_COLS if c not in df_I.columns]}")

    check(len(df_I) >= 2000,
          f"Row count acceptable: {len(df_I):,} tracts",
          f"Too few tracts: {len(df_I):,} (expected ~2,647)")

    check(df_I["GEOID"].str.startswith("37").all(),
          "All GEOIDs are NC (prefix 37)",
          "Non-NC GEOIDs found in infrastructure file")

    check(df_I["GEOID"].str.len().eq(11).all(),
          "All GEOIDs are 11 digits",
          f"Bad GEOID lengths found")

    check(df_I["GEOID"].duplicated().sum() == 0,
          "No duplicate GEOIDs",
          f"Duplicate GEOIDs: {df_I['GEOID'].duplicated().sum()}")

    check(df_I["score_I"].between(0, 1).all(),
          f"score_I in [0,1]: range {df_I['score_I'].min():.3f} – {df_I['score_I'].max():.3f}",
          f"score_I out of range: min={df_I['score_I'].min():.3f}, max={df_I['score_I'].max():.3f}")

    null_count = df_I[I_REQUIRED_COLS].isnull().sum().sum()
    check(null_count == 0,
          "No nulls in output columns",
          f"{null_count} null values found in output",
          is_warning=True)

# ─────────────────────────────────────────────────────────────
# SECTION X — nc_sectionname.csv
# ─────────────────────────────────────────────────────────────
print("\n[ Section X — nc_sectionname.csv ]")

X_PATH = "data/nc_sectionname.csv"
X_REQUIRED_COLS = ["GEOID", "sub_factor_1", "sub_factor_2", "score_X"]

check(os.path.exists(X_PATH), f"File found: {X_PATH}", f"File missing: {X_PATH}")

if os.path.exists(X_PATH):
    df_X = pd.read_csv(X_PATH, dtype={"GEOID": str})
    # ... same checks as H, M, I

# ─────────────────────────────────────────────────────────────
# SECTION X — nc_sectionname.csv
# ─────────────────────────────────────────────────────────────
print("\n[ Section X — nc_sectionname.csv ]")

X_PATH = "data/nc_sectionname.csv"
X_REQUIRED_COLS = ["GEOID", "sub_factor_1", "sub_factor_2", "score_X"]

check(os.path.exists(X_PATH), f"File found: {X_PATH}", f"File missing: {X_PATH}")

if os.path.exists(X_PATH):
    df_X = pd.read_csv(X_PATH, dtype={"GEOID": str})
    # ... same checks as H, M, I


# ─────────────────────────────────────────────────────────────
# SECTION X — nc_sectionname.csv
# ─────────────────────────────────────────────────────────────
print("\n[ Section X — nc_sectionname.csv ]")

X_PATH = "data/nc_sectionname.csv"
X_REQUIRED_COLS = ["GEOID", "sub_factor_1", "sub_factor_2", "score_X"]

check(os.path.exists(X_PATH), f"File found: {X_PATH}", f"File missing: {X_PATH}")

if os.path.exists(X_PATH):
    df_X = pd.read_csv(X_PATH, dtype={"GEOID": str})
    # ... same checks as H, M, I
# ─────────────────────────────────────────────────────────────
# MERGE CHECK — can hsi.py join all three?
# ─────────────────────────────────────────────────────────────
print("\n[ Merge Compatibility Check ]")

all_exist = all(os.path.exists(p) for p in [H_PATH, M_PATH, I_PATH])
if all_exist:
    df_H = pd.read_csv(H_PATH, dtype={"GEOID": str})
    df_M = pd.read_csv(M_PATH, dtype={"GEOID": str})
    df_I = pd.read_csv(I_PATH, dtype={"GEOID": str})

    merged = df_H.merge(df_M[["GEOID","score_M"]], on="GEOID", how="inner") \
                 .merge(df_I[["GEOID","score_I"]], on="GEOID", how="inner") \
                 .merge(df_E[["GEOID","score_E"]], on="GEOID", how="inner") \  # Lenner
                 .merge(df_C[["GEOID","score_C"]], on="GEOID", how="inner") \  # Kiana
                 .merge(df_G[["GEOID","score_G"]], on="GEOID", how="inner") \  # Rebecca

    check(len(merged) >= 2000,
          f"Inner merge produces {len(merged):,} tracts — sufficient for analysis",
          f"Inner merge too small: {len(merged):,} tracts — check GEOID format mismatches")

    check(merged[["score_H","score_M","score_I"]].isnull().sum().sum() == 0,
          "No nulls after merge — all three scores present for every tract",
          f"Nulls after merge: {merged[['score_H','score_M','score_I']].isnull().sum().to_dict()}")

    # Preview the merged output
    print(f"\n  Preview of merged data ({len(merged):,} tracts):")
    print(merged[["GEOID","score_H","score_M","score_I"]].head(5).to_string(index=False))
else:
    print(f"  {WARN} Cannot run merge check — one or more files missing")

# ─────────────────────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
if not errors:
    print(f"{PASS} ALL CHECKS PASSED — CSVs are ready for hsi.py")
    if warnings:
        print(f"{WARN}  {len(warnings)} warning(s) — review above but not blocking")
else:
    print(f"{FAIL} {len(errors)} ERROR(S) — fix before running hsi.py:")
    for e in errors:
        print(f"   • {e}")
    if warnings:
        print(f"{WARN}  {len(warnings)} warning(s) also found")
print("=" * 60)

sys.exit(0 if not errors else 1)
