d = float(input('Uma distância em metros: '))
km = d/1000
hm = d/100
dam = d/10
dm = d*10
cm = d*100
mm = d*1000
print('A medida de {:.1f}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(d, km, hm, dam, dm, cm, mm))
