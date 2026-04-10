"""Punto de entrada principal para MiAgendaBot."""

from datetime import datetime
from models import Cliente, Cita
from validators import validar_email
from logic import verificar_disponibilidad
from database import guardar_cita
from notifications import enviar_confirmacion


def agendar_cita(
    nombre_cliente: str,
    email_cliente: str,
    fecha_cita: str,
    id_cita: str = "001"
) -> None:
    """Orquesta el flujo completo de agendamiento de una cita."""
    cliente = Cliente(nombre=nombre_cliente, email=email_cliente)
    print(f"Cliente creado: {cliente.nombre}")

    if not validar_email(cliente.email):
        print(f"Error: Email inválido - {cliente.email}")
        return

    print(f"Email validado: {cliente.email}")

    try:
        fecha_datetime = datetime.fromisoformat(fecha_cita)
    except ValueError:
        fecha_datetime = datetime.strptime(fecha_cita, "%Y-%m-%d")

    if not verificar_disponibilidad(fecha_cita):
        print(f"Error: Fecha no disponible - {fecha_cita}")
        return

    print(f"Fecha disponible: {fecha_cita}")

    cita = Cita(id=id_cita, cliente=cliente, fecha=fecha_datetime)

    guardar_cita(cita)

    enviar_confirmacion(cliente.email)


def main() -> None:
    """Función principal que ejecuta el flujo de ejemplo."""
    print("=" * 50)
    print("Bienvenido a MiAgendaBot")
    print("=" * 50)

    agendar_cita(
        nombre_cliente="Juan Pérez",
        email_cliente="juan.perez@ejemplo.com",
        fecha_cita="2026-04-15"
    )

    print("\n" + "=" * 50)
    print("Proceso completado")
    print("=" * 50)


if __name__ == "__main__":
    main()
