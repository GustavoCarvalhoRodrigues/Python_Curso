# Escreva um programa que leia um
# valor em metros e o exiba convertido
# em centímetros e milímetros.

valor_metros = float(input('Digite um valor: '))
m_mm = valor_metros * 1000
m_cm = valor_metros * 100
m_dm = valor_metros * 10
m_dam = valor_metros / 10
m_hec = valor_metros / 100
m_km = valor_metros / 1000
print(f'Conversão de metros para milimetro {m_mm:.0f}')
print(f'Conversão de metros para centímetro: {m_cm:.0f}')
print(f'Conversão de metros para decimetro {m_dm:.0f}')
print(f'Conversão de metros para decâmetro {m_dam:.2f}')
print(f'Conversão de metros para hectômetro {m_hec:.2f}')
print(f'Conversão de metros para quilômetro {m_km:.2f}')