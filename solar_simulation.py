"""Simulação simplificada de sistema solar"""
tariff_brl_per_kwh = 0.8
cost_per_kwp_brl = 4000.0
cover_fraction = 0.7

import pandas as pd
df = pd.read_csv("data/consumo_simulado_90dias.csv", parse_dates=["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.weekday
df["is_office_time"] = ((df["hour"] >= 8) & (df["hour"] <= 18) & (df["weekday"] < 5))
daytime_df = df[df["is_office_time"]]
avg_daytime_kwh_per_day = daytime_df.groupby(daytime_df['timestamp'].dt.date).consumption_kW.sum().mean()
required_kwp = (avg_daytime_kwh_per_day * cover_fraction) / 4.0
system_cost_brl = required_kwp * cost_per_kwp_brl
annual_energy_offset_kwh = avg_daytime_kwh_per_day * cover_fraction * 365.0
annual_savings_brl = annual_energy_offset_kwh * tariff_brl_per_kwh
payback_years = system_cost_brl / annual_savings_brl if annual_savings_brl>0 else None
print("Consumo médio em horário de expediente (kWh/dia):", round(avg_daytime_kwh_per_day,2))
print("Potência do sistema (kWp) para cobrir", int(cover_fraction*100),"%:", round(required_kwp,2))
print("Custo estimado do sistema: R$", round(system_cost_brl,2))
print("Savings anual estimado: R$", round(annual_savings_brl,2))
print("Payback aproximado (anos):", round(payback_years,1))
