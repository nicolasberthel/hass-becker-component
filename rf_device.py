"""Handling of the Becker USB device."""

import logging

from pybecker.becker import Becker

from .const import DEFAULT_CONF_USB_STICK_PATH

_LOGGER = logging.getLogger(__name__)


class PyBecker:
    """Manages a (single, global) pybecker Becker instance."""

    becker = None

    @classmethod
    def setup(cls, stick_path=None):
        """Setup becker instance."""

        if not stick_path:
            stick_path = DEFAULT_CONF_USB_STICK_PATH

        cls.becker = Becker(stick_path, True)
