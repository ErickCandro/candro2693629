from empresa import *
salario_actual = float(input("Ingrese el salario actual del empleado: "))
empleado = Empresa(salario_actual)

salario_hora = Empresa.salarioHora()
print("El empleado gana", salario_hora, "por hora.")

ipc_actual = float(input("Ingrese el IPC actual (%): "))
incremento_ipc = Empresa.incrementoIpc(ipc_actual)
print("El incremento salarial es de", incremento_ipc, "de acuerdo al IPC.")