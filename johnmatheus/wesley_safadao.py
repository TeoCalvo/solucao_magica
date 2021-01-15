import datetime

data = input("Entre com sua data de nascimento: DD-MM-YYYY: ")
data = datetime.datetime.strptime( data, "%d-%m-%Y" )

ano = data.year
mes = data.month
dia = data.day

safadeza = sum( [i for i in range(1, int(mes)+1)] ) + (int(ano)/1000) * (50 - int(dia))
anjo = 100 - safadeza

print("Safadeza: {:.2f}\nAnjo: {:.2f}".format(safadeza, anjo), )
