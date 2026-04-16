from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        
    @abstractmethod
    def mostrar_rol(self):
        pass
    
class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad
        
    def mostrar_rol(self):
        return f"Nombre: {self.nombre}\nRol: Veterinario\nEspecialidad: {self.especialidad}."
    
    def atender_mascota(self, mascota):
        print (f"{self.nombre} está atendiendo a {mascota.nombre}.")
    
class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"Nombre: {self.nombre}\nRol: Recepcionista."
    
    def registrar_cliente(self, cliente):
        return f"{self.nombre}, registró al cliente {cliente.nombre}"
    
class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = [] # Relacion de uno a muchos: un cliente puede tener varias mascotas
        
    def mostrar_rol(self):
        return f"Nombre: {self.nombre}\nRol: Cliente"
    
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
# Revisar al momento de correr el programa
        return f"{mascota} ha sido agregada a la lista de mascotas de {self.nombre}."
    
    def mostrar_mascotas(self):
        print(f"{self.nombre} tiene las siguientes mascotas: ")
# Revisar como muestra a las mascotas
        for m in self.mascotas:
            print(m.mostrar_info())
    
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad} años\nPeso: {self.peso} kg.\n"
    
class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias
        
    def mostrar_tratamiento(self):
        return f"- {self.nombre} por {self.duracion_dias} días, ${self.costo}"
    
class Consulta:
    def __init__(self, veterinario, mascota, motivo):
        self.veterinario = veterinario
        self.mascota = mascota
        self.motivo = motivo
        self.diagnostico = None
        self.tratamientos = []
        
    def crear_tratamiento(self, nombre, costo, duracion_dias):
        nuevo_tratamiento = Tratamiento(nombre, costo, duracion_dias)
        self.tratamientos.append(nuevo_tratamiento)
        return f"Tratamiento {nombre} creado y agregado a la consulta de {self.mascota.nombre}."
    
    def mostrar_resumen(self):
        print(f"Nombre: {self.mascota.nombre}\nEspecie: {self.mascota.especie}\nAtendida por {self.veterinario.nombre}.\nMotivo: {self.motivo}\nDiagnóstico: {self.diagnostico}\nTratamientos:") 
        for t in self.tratamientos:
            print(t.mostrar_tratamiento())
        print()
# Revisar como imprime los tratameintos

    def calcular_costo_consulta(self):
        return sum(t.costo for t in self.tratamientos)

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass
    
class PagoEfectivo(MetodoPago):
    
    def procesar_pago(self, monto):
        print(f"Procesando pago en efectivo... ${monto:.2f} recibido.")    

class PagoTarjeta(MetodoPago):
    
    def procesar_pago(self, monto):
        print(f"Procesando pago con tarjeta... ${monto:.2f} recibido.")    

class PagoTransferencia(MetodoPago):
    
    def procesar_pago(self, monto):
        print(f"Procesando pago por transferencia... ${monto:.2f} recibido.")    

class Factura:
    def __init__(self, consulta, subtotal=0, impuesto=0.19, total=0):
        self.consulta = consulta
        self.subtotal = subtotal
        self.impuesto = impuesto
        self.total = total
        
    def calcular_total(self):
        self.subtotal = self.consulta.calcular_costo_consulta()
        self.total = self.subtotal + (self.subtotal * self.impuesto)
        return self.total
    
    def pagar(self, metodo_pago):
        metodo_pago.procesar_pago(self.total)


if __name__ == "__main__":
#RECEPCIONISTA
    print("---- HOSPITAL VETERINARIO ----")
    print(" ")
    
    print("---- RECEPCIONISTA ----")
    recep = Recepcionista("Ana", "12345678")
    print(recep.mostrar_rol())
    print(" ")

# VETERINARIO    
    print("---- VETERINARIO ----")
    vet = Veterinario("Dr. Juan", "87654321", "medicina interna")
    print(vet.mostrar_rol())
    print(" ")
    
#CLIENTE
    print("---- CLIENTE ----")
    cliente = Cliente("Carlos", "11223344", "555-1234")
    print(" ")
    print(f"Registro exitoso:\n{recep.registrar_cliente(cliente)}")
    print(" ")
    print(cliente.mostrar_rol())
    print(" ")
    
#MASCOTA
    perro = Mascota("Tommy", "Perro", 5, 20)
    gato = Mascota("Zimba", "Gato", 3, 5)
    pajaro = Mascota("Piolin", "Pájaro", 2, 0.5)
    cliente.agregar_mascota(perro)
    cliente.agregar_mascota(gato)
    cliente.agregar_mascota(pajaro)
    print("--- MASCOTAS DEL CLIENTE ---")
    cliente.mostrar_mascotas()
    
#CONSULTA    
    print("---- CONSULTAS ----")
    print("* Consulta 1:")
    consulta_perro = Consulta(vet, perro, "Fiebre y falta de apetito")
    consulta_perro.diagnostico = "Infección gastrointestinal"
    consulta_perro.crear_tratamiento("Antibióticos", 50, 7)
    consulta_perro.crear_tratamiento("Analgésicos", 30, 5)
    consulta_perro.mostrar_resumen()
    
    print("* Consulta 2:")
    consulta_gato = Consulta(vet, gato, "Vómitos y letargo")
    consulta_gato.diagnostico = "Gastroenteritis"
    consulta_gato.crear_tratamiento("Rehidratación", 40, 3)
    consulta_gato.crear_tratamiento("Antieméticos", 25, 5)
    consulta_gato.mostrar_resumen()
    
    print("* Consulta 3:")
    consulta_pajaro = Consulta(vet, pajaro, "Plumas erizadas y falta de energía")
    consulta_pajaro.diagnostico = "Infección respiratoria"
    consulta_pajaro.crear_tratamiento("Antibióticos", 20, 7)
    consulta_pajaro.crear_tratamiento("Suplementos vitamínicos", 10, 10)
    consulta_pajaro.mostrar_resumen()
    
    print("---- FACTURAS ----")
    print("* Factura para el perro:")
    factura_perro = Factura(consulta_perro)
    print(f"Total a pagar: ${factura_perro.calcular_total()}")
    factura_perro.pagar(PagoEfectivo())
    print(" ")
    
    print("* Factura para el gato:")
    factura_gato = Factura(consulta_gato)
    print(f"Total a pagar: ${factura_gato.calcular_total()}")
    factura_gato.pagar(PagoTarjeta())
    print(" ")
    
    print("* Factura para el pájaro:")
    factura_pajaro = Factura(consulta_pajaro)
    print(f"Total a pagar: ${factura_pajaro.calcular_total()}")
    factura_pajaro.pagar(PagoTransferencia())
    
    

    
