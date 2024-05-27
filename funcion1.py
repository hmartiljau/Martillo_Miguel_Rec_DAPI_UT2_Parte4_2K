import csv
from funcion2 import create_email
from funcion3 import calculate_grade


def process_class(ruta):
   """
   Lee los datos y los almacena en una lista de diccionarios donde en cada uno
   de los alumnos las claves serán los datos de la cabecera del archivo CSV
   y los valores serán los datos de cada alumno/a.
   :param ruta: un str con la ruta del fichero (.csv) a abrir.
   :return: None
   """
   datos_reformateados = []
   # Leer fichero csv
   with open(ruta, newline='', encoding="UTF-8") as csvfile:
       reader = csv.DictReader(csvfile)
       for fila in reader:
            # Crear correo electronico
            email = create_email(fila['Nombre'],fila['Apellido'])
            # Calcular la nota final y si esta aprobado
            practica01 = float(fila['Practica01'].replace(',', '.'))
            practica02 = float(fila['Practica02'].replace(',', '.'))
            practica03 = float(fila['Practica03'].replace(',', '.'))
            examen = float(fila['Examen'].replace(',', '.'))
            recuperacion = float(fila['Recuperacion'].replace(',', '.'))
            actitud = float(fila['Actitud'].replace(',', '.'))
            nota_final, aprobado = calculate_grade(practica01, practica02, practica03, examen, recuperacion, actitud)
            nota_final = round(nota_final,2)
            # Incluir datos en lista {nombre, apellido, email, nota, aprobado}
            alumno = {
                'nombre': fila['Nombre'],
                'apellido': fila['Apellido'],
                'email': email,
                'nota_final': nota_final,
                'aprobado': aprobado
            }
            datos_reformateados.append(alumno)
   # Guardar lista en fichero grades.csv  
   with open('grades.csv', mode='w', newline='', encoding="UTF-8") as csvfile:
        fieldnames = ['nombre', 'apellido', 'email', 'nota_final', 'aprobado']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for alumno in datos_reformateados:
            writer.writerow(alumno)


process_class("class.csv")

