# =========================================================
# SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ
# Programación Orientada a Objetos + Manejo de Excepciones
# =========================================================

from abc import ABC, abstractmethod
from datetime import datetime

# =========================================================
# ARCHIVO DE LOGS
# =========================================================

def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# =========================================================
# EXCEPCIONES PERSONALIZADAS
# =========================================================

class ErrorCliente(Exception):
    pass

class ErrorServicio(Exception):
    pass

class ErrorReserva(Exception):
    pass


# =========================================================
# CLASE ABSTRACTA ENTIDAD
# =========================================================

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# =========================================================
# CLASE CLIENTE
# =========================================================

class Cliente(Entidad):

    def __init__(self, nombre, documento, correo, telefono):

        if not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacío")

        if not documento.isdigit():
            raise ErrorCliente("El documento debe contener solo números")

        if "@" not in correo:
            raise ErrorCliente("Correo inválido")

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_info(self):
        print(f"Cliente: {self.__nombre} - Documento: {self.__documento}")

    def get_nombre(self):
        return self.__nombre


# =========================================================
# CLASE ABSTRACTA SERVICIO
# =========================================================

class Servicio(ABC):

    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =========================================================
# SERVICIO 1 - RESERVA DE SALA
# =========================================================

class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a 0")

        return self.tarifa * horas

    def descripcion(self):
        return "Servicio de reserva de salas"


# =========================================================
# SERVICIO 2 - ALQUILER DE EQUIPOS
# =========================================================

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ErrorServicio("Tiempo inválido")

        costo = self.tarifa * horas

        # Descuento si son más de 5 horas
        if horas > 5:
            costo *= 0.9

        return costo

    def descripcion(self):
        return "Servicio de alquiler de equipos"


# =========================================================
# SERVICIO 3 - ASESORÍA ESPECIALIZADA
# =========================================================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ErrorServicio("La duración no es válida")

        impuesto = 0.19

        return (self.tarifa * horas) * (1 + impuesto)

    def descripcion(self):
        return "Servicio de asesoría especializada"


# =========================================================
# CLASE RESERVA
# =========================================================

class Reserva:

    def __init__(self, cliente, servicio, horas):

        if horas <= 0:
            raise ErrorReserva("La duración debe ser positiva")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        try:
            costo = self.servicio.calcular_costo(self.horas)
            self.estado = "Confirmada"

            print("\nReserva confirmada")
            print(f"Cliente: {self.cliente.get_nombre()}")
            print(f"Servicio: {self.servicio.nombre}")
            print(f"Costo total: ${costo}")

            registrar_log("Reserva confirmada correctamente")

        except Exception as e:
            registrar_log(f"Error al confirmar reserva: {e}")
            print(f"Error: {e}")

    def cancelar(self):

        try:
            self.estado = "Cancelada"
            print("Reserva cancelada")
            registrar_log("Reserva cancelada")

        except Exception as e:
            registrar_log(f"Error al cancelar reserva: {e}")

    def mostrar_estado(self):
        print(f"Estado actual: {self.estado}")


# =========================================================
# PRUEBAS DEL SISTEMA
# =========================================================

print("\n========= SISTEMA SOFTWARE FJ =========\n")

# LISTA PARA GUARDAR RESERVAS
reservas = []

# =========================================================
# OPERACIÓN 1 - CLIENTE VÁLIDO
# =========================================================

try:
    cliente1 = Cliente(
        "Laura Gomez",
        "123456",
        "laura@gmail.com",
        "3001234567"
    )

    cliente1.mostrar_info()

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 2 - CLIENTE INVÁLIDO
# =========================================================

try:
    cliente2 = Cliente(
        "",
        "abc",
        "correo_mal",
        "123"
    )

except Exception as e:
    print(f"Error detectado: {e}")
    registrar_log(e)


# =========================================================
# CREACIÓN DE SERVICIOS
# =========================================================

sala = ReservaSala("Sala VIP", 50000)
equipo = AlquilerEquipo("Computador Gamer", 30000)
asesoria = AsesoriaEspecializada("Asesoría Python", 80000)


# =========================================================
# OPERACIÓN 3 - RESERVA EXITOSA
# =========================================================

try:

    reserva1 = Reserva(cliente1, sala, 3)
    reserva1.confirmar()
    reservas.append(reserva1)

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 4 - RESERVA FALLIDA
# =========================================================

try:

    reserva2 = Reserva(cliente1, equipo, -5)
    reserva2.confirmar()

except Exception as e:
    print(f"Error detectado: {e}")
    registrar_log(e)


# =========================================================
# OPERACIÓN 5
# =========================================================

try:

    reserva3 = Reserva(cliente1, asesoria, 2)
    reserva3.confirmar()
    reservas.append(reserva3)

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 6
# =========================================================

try:

    reserva4 = Reserva(cliente1, equipo, 6)
    reserva4.confirmar()
    reservas.append(reserva4)

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 7
# =========================================================

try:
    reserva1.cancelar()

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 8
# =========================================================

try:

    cliente3 = Cliente(
        "Carlos Ruiz",
        "987654",
        "carlos@gmail.com",
        "3112223344"
    )

    cliente3.mostrar_info()

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 9
# =========================================================

try:

    reserva5 = Reserva(cliente3, sala, 1)
    reserva5.confirmar()

except Exception as e:
    print(e)
    registrar_log(e)


# =========================================================
# OPERACIÓN 10
# =========================================================

try:

    reserva6 = Reserva(cliente3, asesoria, 0)
    reserva6.confirmar()

except Exception as e:
    print(f"Error detectado: {e}")
    registrar_log(e)


# =========================================================
# FINALIZACIÓN
# =========================================================

finally:
    print("\nSistema ejecutado correctamente")