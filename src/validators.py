"""Módulo de validadores para MiAgendaBot."""

import re


def validar_email(email: str) -> bool:
    """Valida el formato de una dirección de correo electrónico."""
    patron_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron_email, email))
