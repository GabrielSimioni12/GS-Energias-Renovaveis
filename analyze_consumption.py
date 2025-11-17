"""Análise de consumo e simulação de adoção solar"""
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv("data/consumo_simulado_90dias.csv", parse_dates=["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["weekday"] = df["timestamp"].dt.weekday
df["is_office_time"] = ((df["hour"] >= 8) & (df["hour"] <= 18) & (df["weekday"] < 5))
df_daily = df.groupby(df['timestamp'].dt.date).consumption_kW.sum().reset_index(name="daily_kWh")
print(df_daily.head())
hourly_avg = df.groupby("hour").consumption_kW.mean().reset_index()
plt.plot(hourly_avg["hour"], hourly_avg["consumption_kW"])
plt.xlabel("Hora do dia")
plt.ylabel("Consumo médio (kW)")
plt.title("Perfil horário médio de consumo")
plt.tight_layout()
plt.savefig("analysis/hourly_profile.png")
print("Saved analysis/hourly_profile.png")
