# BACKTEST SIMPLES BTC/USDT
# RafaelIA Núcleo Simbiótico ∞
# Estratégia: média móvel + RSI
# Objetivo: crescer saldo em USDT

import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

# === CONFIG ===
capital_inicial = 100000  # USDT
capital = capital_inicial
position = 0  # BTC comprado (0 ou quantidade)
trade_log = []
pct_vitorias = []

# === LEITURA DOS DADOS ===
# Substituir por API ou CSV real do Binance (ex.: df = pd.read_csv('btc_usdt.csv'))
# Precisa ter: Date, Open, High, Low, Close, Volume
df = pd.read_csv('btc_usdt.csv', parse_dates=['Date'])

# === INDICADORES ===
df['SMA7'] = SMAIndicator(df['Close'], window=7).sma_indicator()
df['RSI'] = RSIIndicator(df['Close'], window=14).rsi()

# === BACKTEST ===
saldo = capital
btc_holding = 0
in_position = False

for idx, row in df.iterrows():
    date = row['Date'].strftime('%Y-%m-%d')
    close = row['Close']
    sma7 = row['SMA7']
    rsi = row['RSI']
    
    trade = None
    lucro_pct = 0
    
    # CONDIÇÃO DE COMPRA
    if not in_position and close > sma7 and rsi < 70:
        btc_holding = saldo / close
        saldo = 0
        in_position = True
        trade = 'BUY'
        
    # CONDIÇÃO DE VENDA
    elif in_position and (rsi > 70 or close < sma7):
        saldo = btc_holding * close
        btc_holding = 0
        in_position = False
        trade = 'SELL'
    
    # CALCULA LUCRO DIÁRIO (diferença do saldo final do dia)
    saldo_dia = saldo if saldo > 0 else btc_holding * close
    if idx > 0:
        lucro_pct = (saldo_dia - trade_log[-1]['SaldoFinal']) / trade_log[-1]['SaldoFinal'] * 100
    
    # Guarda trade no log
    trade_log.append({
        'Data': date,
        'SaldoFinal': round(saldo_dia, 2),
        'LucroDiario%': round(lucro_pct, 4),
        'QtdTrades': 1 if trade else 0,
        'Trade': trade if trade else '',
        'Close': close,
        'RSI': round(rsi, 2),
        'SMA7': round(sma7, 2)
    })
    
    # Guarda vitória
    if trade == 'SELL' and lucro_pct > 0:
        pct_vitorias.append(1)
    elif trade == 'SELL':
        pct_vitorias.append(0)

# === CONVERTE EM DATAFRAME E EXPORTA CSV ===
result_df = pd.DataFrame(trade_log)
result_df.to_csv('resultado_backtest.csv', index=False, sep=';')

# === RESUMO FINAL ===
total_trades = sum(result_df['QtdTrades'])
pct_vitoria_total = np.mean(pct_vitorias) * 100 if pct_vitorias else 0
saldo_final = result_df.iloc[-1]['SaldoFinal']
lucro_total = saldo_final - capital_inicial
lucro_total_pct = (lucro_total / capital_inicial) * 100

print(f"Saldo final: USDT {saldo_final:.2f}")
print(f"Lucro total: USDT {lucro_total:.2f} ({lucro_total_pct:.2f}%)")
print(f"Trades realizados: {total_trades}")
print(f"% Trades vencedores: {pct_vitoria_total:.2f}%")
