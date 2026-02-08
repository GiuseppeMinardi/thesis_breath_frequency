import pandas as pd


def normalize_columns(df_: pd.DataFrame) -> pd.DataFrame:
    df_.columns = [col.strip().lower().replace(" ", "_") for col in df_.columns]
    return df_


def convert_time_to_seconds(time_str: str) -> int:
    if isinstance(time_str, str):
        hours, minutes, seconds = time_str.split(":")
        minutes = int(minutes) + int(hours) * 60
        seconds = int(seconds) + minutes * 60
        return seconds
    else:
        raise ValueError(f"Expected a string in the format 'HH:MM:SS', got {time_str}")


def correct_df_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Strip whitespace from all string columns
    str_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    # 2. Attempt to convert string columns to numeric where possible
    for col in str_cols:
        # check if the column is primarily digits/decimals
        # errors='ignore' keeps it as string if it's not a number
        converted = pd.to_numeric(df[col], errors="coerce")

        # If the conversion didn't result in all NaNs (meaning it was actually numbers)
        if not converted.isna().all():
            df[col] = converted

    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_mapping = {
        "work_(watts)": "work_watts",
        "vo2_(ml/kg/min)": "vo2_ml_per_kg_min",
        "vo2_(ml/min)": "vo2_ml_per_min",
        "vco2_(ml/min)": "vco2_ml_per_min",
        "rer": "rer",
        "rr_(br/min)": "rr_br_per_min",
        "vt_btps_(l)": "vt_btps_l",
        "ve_btps_(l/min)": "ve_btps_l_per_min",
        "br_(%)": "breathing_reserve_pct",
        "hr_(bpm)": "hr_bpm",
        "hrr_(%)": "hrr_pct",
        "peto2_(mmhg)": "peto2_mmhg",
        "petco2_(mmhg)": "petco2_mmhg",
        "rr_(br/min)copy": "rr_br_per_min_copy",
        "vo2/pred(%)": "vo2_pred_pct",
        "ti/ttot": "ti_ttot_ratio",
        "ti_(sec)": "ti_sec",
        "te_(sec)": "te_sec",
        "ttot_(sec)": "ttot_sec",
        "msec": "rr_interval_msec",
        "msec_diff_quad": "rr_interval_diff_squared_msec",
        "rmssq": "rmssd_ms",
        "patient": "patient_id",
        "time_seconds": "time_seconds",
    }
    return df.rename(columns=rename_mapping)
