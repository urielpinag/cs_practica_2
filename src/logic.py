"""Módulo de lógica de negocio para MiAgendaBot."""


def verificar_disponibilidad(fecha: str) -> bool:
    """Verifica si una fecha está disponible para agendar una cita."""
    if not fecha or not isinstance(fecha, str):
        return False

    fecha_limpia = fecha.strip()
    return len(fecha_limpia) > 0
