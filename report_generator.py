import pandas as pd

def build_report(metrics, cycles, orphans):
    df = pd.DataFrame(metrics)
    df['has_cycle'] = df['name'].isin([c[0] for c in cycles])
    df['is_orphan'] = df['name'].isin(orphans)
    df.to_excel('config_report.xlsx', index=False)
    return df
