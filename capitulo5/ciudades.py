ciudades = {'Bogota': 7715778, 'Medellín': 2490164, 'Cali': 2205680, 'Barranqilla': 1273646, 'Cúcuta': 748948}
#se crea lista para guardar la poblacion
poblacionTotal= list()
#
a=ciudades.get('Bogota'); b=ciudades.get('Medellín'); c=ciudades.get('Cali'); d=ciudades.get('Barranquilla'); e=ciudades.get('Cucúta')
poblacionTotal.append(a); poblacionTotal.append(b); poblacionTotal.append(c); poblacionTotal.append(d); poblacionTotal.append(e)
total=sum(poblacionTotal)
bogota=a/total; medellin=b/total; cali=c/total; barranquilla=d/total; cucuta=e/total
bo=bogota*100; me=medellin*100; ca=cali*100; ba=barranquilla*100; cu=cucuta*100
print(f'''total:{total},\ntotal_bogota:{bogota:.2f} fr:{bo:.1f}% ''')