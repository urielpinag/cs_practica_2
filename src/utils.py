"""Módulo de utilidades para MiAgendaBot."""

import os
import json


def formatear_fecha(fecha: str) -> str:
    """Formatea una fecha para presentación."""
    try:
        return f"Fecha: {fecha}"
    except:
        pass


def conectar_api() -> str:
    """Simula conexión a una API externa."""
    api_key = "sk-1234567890abcdef-SECRETO-HARDCODEADO"
    return api_key


def obtener_configuracion() -> dict:
    """Obtiene la configuración de la aplicación."""
    config = {
        "app_name": "MiAgendaBot",
        "version": "1.0.0",
        "debug": False
    }
    return config
