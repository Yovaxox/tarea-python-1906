### INICIALIZAR VARIABLES
trabajadores=[]
### PARAMETRIZACIONES
mensaje_error_value_type = 'Ha ocurrido un error de Valor o un error de Tipo. '
mensaje_error_por_defecto = 'Ha ocurrido un error inesperado. '
mensaje_error_ingresar = 'Ha ocurrido un error al ingresar '
descuento_salud = 0.07
descuento_afp = 0.12
descuento_liquido = 0.81
cargos = [None,'Todos','CEO','Analista','Desarrollador']

def separar_miles(numero):
    formateado = '{:,}'.format(numero).replace(',','.')
    return formateado

def escribir_trabajador_txt(trabajador, archivo_sueldos):
    nombre = trabajador['Trabajador']
    cargo = trabajador['Cargo']
    bruto = trabajador['Sueldo bruto']
    salud = trabajador['Desc. salud']
    afp = trabajador['Desc. AFP']
    liquido = trabajador['Liquido']
    archivo_sueldos.writelines(nombre)
    archivo_sueldos.write("\t\t")
    archivo_sueldos.writelines(cargo)
    archivo_sueldos.write("\t\t\t")
    archivo_sueldos.write("$" + str(separar_miles(bruto)))
    archivo_sueldos.write("\t\t")
    archivo_sueldos.write("$" + str(separar_miles(salud)))
    archivo_sueldos.write("\t\t")
    archivo_sueldos.write("$" + str(separar_miles(afp)))
    archivo_sueldos.write("\t\t")
    archivo_sueldos.write("$" + str(separar_miles(liquido)))
    archivo_sueldos.write("\n")

def menu():
	print("================================")
	print("          BIENVENIDOS           ")
	print("================================")
	print("1. Registrar trabajador")
	print("2. Listado de trabajadores")
	print("3. Imprimir plantilla de sueldos")
	print("4. Salir del programa")
	print("================================")

### FUNCIONES PARA REGISTRAR USUARIO ###
def registrar():
    try:
        trabajador = {}
        
        llave_trabajador = 'Trabajador'
        nombre = obtener_input(llave_trabajador, "Ingrese " + llave_trabajador + ": ")
        trabajador[llave_trabajador] = nombre

        llave_cargo = 'Cargo'
        cargo = obtener_input(llave_cargo, "Ingrese " + llave_cargo + ": ")
        trabajador[llave_cargo] = cargo

        llave_sueldo_bruto = 'Sueldo bruto'
        sueldo_bruto = obtener_input(llave_sueldo_bruto, "Ingrese " + llave_sueldo_bruto + ": ")
        trabajador[llave_sueldo_bruto] = round(int(sueldo_bruto))

        trabajador['Desc. salud'] = round(trabajador[llave_sueldo_bruto] * descuento_salud)

        trabajador['Desc. AFP'] = round(trabajador[llave_sueldo_bruto] * descuento_afp)

        trabajador['Liquido'] = round(trabajador[llave_sueldo_bruto] * descuento_liquido)

        trabajadores.append(trabajador)
        print("Trabajador añadido con éxito.")
    except(ValueError, TypeError):
        print(mensaje_error_value_type + "registrar")
    except:
        print(mensaje_error_por_defecto + "registrar")
    
def obtener_input(nombre_input, mensaje_input):
    while True:
        try:
            valor = validar_input(nombre_input, input(mensaje_input))
            if valor != '':
                return valor
            else:
                continue
        except(ValueError, TypeError):
            print(mensaje_error_value_type + "obtener_input")
        except:
            print(mensaje_error_por_defecto + "obtener_input")
        
def validar_input(nombre_input, input_usuario):
    try:
        if nombre_input == 'Trabajador' and input_usuario.strip() != "":
            return input_usuario
        elif nombre_input == 'Cargo' and input_usuario in {'CEO', 'Analista', 'Desarrollador'}:
            return input_usuario
        elif nombre_input == 'Sueldo bruto' and int(input_usuario) > 0:
            return input_usuario
        elif nombre_input == 'OpcionImprimir' and (int(input_usuario) >= 1 and int(input_usuario) <= 4):
            return int(input_usuario)
        else:
            print(mensaje_error_ingresar + nombre_input)
            return ''
    except(ValueError, TypeError):
        print(mensaje_error_value_type + "validar_input")
        print(mensaje_error_ingresar + nombre_input)
        return ''
    except:
        print(mensaje_error_por_defecto + "validar_input")
        print(mensaje_error_ingresar + nombre_input)
        return ''
### FIN FUNCIONES PARA REGISTRAR USUARIO ###

def listar():
    try:
        if len(trabajadores) > 0:
            for persona in trabajadores:
                trabajador = persona['Trabajador']
                cargo = persona['Cargo']
                bruto = persona['Sueldo bruto']
                salud = persona['Desc. salud']
                afp = persona['Desc. AFP']
                liquido = persona['Liquido']
                print("================================")
                print("Nombre del trabajador\t: ", trabajador)
                print("Cargo del trabajador\t: ", cargo)
                print("Sueldo bruto\t\t: $", separar_miles(bruto))
                print("Desc. salud\t\t: $", separar_miles(salud))
                print("Desc. AFP\t\t: $", separar_miles(afp))
                print("Sueldo líquido\t\t: $", separar_miles(liquido), '\n')
        else:
            print('No existen trabajadores registrados.')
    except:
        print(mensaje_error_por_defecto + 'listar')

def imprimir():
    try:
        if len(trabajadores) > 0:
            # VARIABLES INICIALIZADAS
            trabajador = []
            # MANEJAR DOCUMENTO
            with open("detalle_sueldos.txt","w") as archivo_sueldos:
                op_imprimir = obtener_input('OpcionImprimir', "1.-Listar todos\n2.-Listar CEO\n3.-Listar Analistas\n4.-Listar Desarrolladores\n[1/2/3/4]\n")
                archivo_sueldos.write("Trabajador | Cargo\t\t\t| Sueldo bruto | Desc. Salud | Desc. AFP | Sueldo liquido\n")
                if op_imprimir == 1:
                    for trabajador in trabajadores:
                        escribir_trabajador_txt(trabajador, archivo_sueldos)
                else:
                    for trabajador in trabajadores:
                        if trabajador['Cargo'] == cargos[op_imprimir]:
                            escribir_trabajador_txt(trabajador, archivo_sueldos)
            archivo_sueldos.close()
            print("Datos guardados exitosamente en detalle_sueldos.txt")
        else:
            print('No existen trabajadores registrados.')
    except:
        print(mensaje_error_por_defecto + 'imprimir')

def imprimir_salida():
    print("Saliendo del programa") 
    print("Ver 1.1 Developed by Guisela Herranz, Samuel Parra")

def principal():
    while True:
        menu()
        try:
            op = int(input("Ingrese su opción [1/2/3/4]: "))
            if op == 1:
                registrar()
            elif op == 2:
                listar()
            elif op == 3:
                imprimir()
            elif op == 4:
                imprimir_salida()
                break
            else:
                 print("Ingrese una opción entre 1 y 4")
        except(ValueError, TypeError):
            print(mensaje_error_value_type + "principal")
        except:
            print(mensaje_error_por_defecto + "principal")

principal()