# Proyecto realizado por: 
(Nombre y Link a GitHub del proyecto)

- Adriana Ximena Guzman Rojas - https://github.com/Xime182026/Proyecto-tienda-veterinaria.git
- Carolina Gil - https://github.com/dcelcirculo/M1PF-HospitalVeterinario.git
- Roberto Deart Pérez - https://github.com/Rdeart/Sistema-de-gesti-n-de-hospital-veterinario
- Juan Carlos Corrales Ramírez

# Sistema de Gestión de Hospital Veterinario

## Descripción

Este proyecto consiste en el desarrollo de un sistema básico para gestionar un hospital veterinario utilizando Programación Orientada a Objetos (POO) en Python.

El sistema permite organizar:
- Personas (clientes, veterinarios y recepcionistas)
- Mascotas
- Consultas
- Tratamientos
- Facturación y pagos

Lo principal fue aplicar conceptos de POO como herencia, asociación, agregación, composición y polimorfismo.

## Clases

### 1. Persona (Clase abstracta)

Es la clase base del sistema.

Tiene:
- nombre
- documento

De esta clase heredan:
- Veterinario
- Recepcionista
- Cliente

Incluye un método obligatorio:
- mostrar_rol()

#### 1.1. Veterinario

Representa al doctor que atiende las mascotas.

***Tiene:***
- especialidad

***Puede:***
- mostrar su rol
- atender mascotas

#### 1.2. Recepcionista

Encargada de registrar clientes.

***Puede:***
- mostrar su rol
- registrar clientes en el sistema

#### 1.3. Cliente

Representa al dueño de las mascotas.

***Tiene:***
- teléfono
- lista de mascotas

***Puede:***
- agregar mascotas
- mostrar sus mascotas

### Mascota

Representa a los animales del sistema.

***Tiene:***
- nombre
- especie
- edad
- eso

***Puede:***
- mostrar su información

### Consulta

Representa una consulta médica.

***Tiene:***
- veterinario
- mascota
- motivo
- diagnóstico
- ratamientos

***Puede:***
- crear tratamientos
- mostrar un resumen
- calcular el costo total


### Tratamiento

Representa el tratamiento médico que se crea en la consulta.

**Tiene:**
- nombre
- costo
- duración

### Método Pago (Clase abstracta)

Define cómo se procesan los pagos.

De esta clase heredan:
- Pago en efectivo
- Pago con tarjeta
- Pago por transferencia

Cada uno implementa:
- procesar_pago()

### Factura

Representa el cobro de una consulta.

***Tiene:***
- consulta
- subtotal
- impuesto
- total

***Puede:***
- calcular el total
- procesar el pago usando diferentes métodos

## Relaciones entre clases

### 1. Herencia

#### 1.1. Las clases:
- Veterinario
- Recepcionista
- Cliente

heredan de Persona.

#### 1.2. Las clases:
- Pago en efectivo
- Pago con tarjeta
- Pago por transferencia

heredan de MetodoPago

### 2. Agregación

Un Cliente tiene mascotas, pero las mascotas pueden existir sin él.

    - Cliente → Mascota

### 3. Asociación

Una Consulta conecta: un veterinario - una mascota

    - Consulta → Veterinario / Mascota

### 4. Composición

Los Tratamientos nacen dentro de una Consulta.

    - Consulta → Tratamiento

### 5. Polimorfismo

La Factura puede usar distintos métodos de pago sin cambiar su lógica.

    - MetodoPago → PagoEfectivo / PagoTarjeta / PagoTransferencia

## ▶ Ejecución del programa

El programa es una simulación del flujo básico de un hospital veterinario:
1.	Se crea el personal (recepcionista y veterinario)
2.	Se registra un cliente
3.	Se agregan mascotas al cliente
4.	Se crean consultas para cada mascota
5.	Se agregan tratamientos
6.	Se generan facturas
7.	Se realizan pagos con diferentes métodos
