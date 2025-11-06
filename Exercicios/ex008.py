medida = float(input('uma distância de: '))
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
dm = medida * 10
km = medida / 1000
print(f'A medida de {medida} metros corresponde a {cm:.1f}cm, {mm:.1f}mm, {dam:.1f}dam, {hm:.1f}hm, {dm:.1f}dm e {km:.1f}km')
#print(f'A medida de {medida} corresponde a {cm}cm e {mm}mm')