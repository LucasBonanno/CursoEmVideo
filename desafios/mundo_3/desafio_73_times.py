times = ('santos','palmeiras','flamengo','botafogo','gremio','lusa','corinthians')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os três primeiros times são: {times[:3]}')
print('-=' * 15)
print(f'Os 2 últimos colocados são: {times[-2:]}')
print('-=' * 15)
print(f'Os times em ordem alabética: {sorted(times)}')
print('-=' * 15)
print(f'O {times[3]} está na posição {times.index("botafogo")} da lista de times')