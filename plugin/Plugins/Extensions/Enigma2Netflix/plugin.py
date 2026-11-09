# -*- coding: utf-8 -*-
# Experimental Enigma2 Netflix integration scaffold.
# Copyright (C) 2026 Enigma2-Netflix contributors.
# SPDX-License-Identifier: GPL-3.0-only

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label

try:
    from Components.Language import language
except ImportError:
    language = None


def is_italian():
    try:
        return language is not None and language.getLanguage().lower().startswith("it")
    except Exception:
        return False


def tr(english, italian):
    return italian if is_italian() else english


class NetflixExperimentalScreen(Screen):
    skin = """
    <screen name="NetflixExperimentalScreen" position="center,center"
            size="720,420" title="Enigma2 Netflix">
        <widget name="heading" position="35,35" size="650,48"
                font="Regular;32" foregroundColor="#ffffff" />
        <widget name="description" position="35,110" size="650,160"
                font="Regular;24" foregroundColor="#ffffff" />
        <widget name="notice" position="35,295" size="650,65"
                font="Regular;20" foregroundColor="#ffcc66" />
        <widget name="footer" position="35,375" size="650,32"
                font="Regular;20" foregroundColor="#ffffff" />
    </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.setTitle("Enigma2 Netflix - Experimental")
        self["heading"] = Label("Enigma2 Netflix")
        self["description"] = Label(tr(
            "Initial integration screen.\nDASH and DRM playback tests are not implemented yet.",
            "Schermata iniziale.\nI test di riproduzione DASH e DRM non sono ancora implementati."
        ))
        self["notice"] = Label(tr(
            "Netflix compatibility has NOT been established.",
            "La compatibilita' con Netflix NON e' stata verificata."
        ))
        self["footer"] = Label(tr("OK / EXIT / BACK: Close", "OK / EXIT / BACK: Chiudi"))
        self["actions"] = ActionMap(
            ["OkCancelActions"],
            {"ok": self.close, "cancel": self.close},
            -1
        )


def open_plugin(session, **kwargs):
    session.open(NetflixExperimentalScreen)


def Plugins(**kwargs):
    return [
        PluginDescriptor(
            name="Enigma2 Netflix (Experimental)",
            description="Experimental Netflix integration for DreamOS",
            where=PluginDescriptor.WHERE_PLUGINMENU,
            fnc=open_plugin
        )
    ]
