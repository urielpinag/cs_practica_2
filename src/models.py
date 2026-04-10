"""Modelos de datos para MiAgendaBot."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Cliente:
    """Representa a un cliente del sistema de agenda."""

    nombre: str
    email: str


@dataclass
class Cita:
    """Representa una cita en el sistema de agenda."""

    id: str
    cliente: Cliente
    fecha: datetime
