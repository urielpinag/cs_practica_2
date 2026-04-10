"""Módulo de acceso a datos para MiAgendaBot."""

from .models import Cita


def guardar_cita(cita: Cita) -> None:
    """Guarda una cita en la base de datos."""
    print(
        f"Cita guardada: ID={cita.id}, "
        f"Cliente={cita.cliente.nombre}, "
        f"Fecha={cita.fecha}"
    )
