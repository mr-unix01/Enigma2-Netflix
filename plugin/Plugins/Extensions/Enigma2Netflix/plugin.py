# -*- coding: utf-8 -*-
# Experimental Enigma2 Netflix integration scaffold.
# Copyright (C) 2026 Enigma2-Netflix contributors.
# SPDX-License-Identifier: GPL-3.0-only

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.Label import Label
from enigma import eServiceReference

try:
    from Components.Language import language
except ImportError:
    language = None


TEST_DASH_URL = "https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps.mpd"


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
        self.previous_service = None
        self.test_started = False
        self["heading"] = Label("Enigma2 Netflix")
        self["description"] = Label(tr(
            "Press OK to test unencrypted MPEG-DASH playback.\nTest video: Big Buck Bunny.",
            "Premi OK per provare la riproduzione MPEG-DASH senza DRM.\nVideo di prova: Big Buck Bunny."
        ))
        self["notice"] = Label(tr(
            "Netflix/DRM compatibility is NOT established.",
            "La compatibilita' Netflix/DRM NON e' verificata."
        ))
        self["footer"] = Label(tr(
            "OK: DASH test    EXIT: Close / restore TV",
            "OK: Test DASH    EXIT: Chiudi / ripristina TV"
        ))
        self["actions"] = ActionMap(
            ["OkCancelActions"],
            {"ok": self.start_test, "cancel": self.close},
            -1
        )
        self.onClose.append(self.restore_service)

    def start_test(self):
        if self.test_started:
            return
        nav = self.session.nav
        self.previous_service = nav.getCurrentlyPlayingServiceReference()
        ref = eServiceReference(4097, 0, TEST_DASH_URL)
        try:
            result = nav.playService(ref)
        except Exception as error:
            self["description"].setText(tr(
                "DASH test failed: %s", "Test DASH fallito: %s"
            ) % str(error))
            return
        if result not in (None, 0):
            self["description"].setText(tr(
                "DASH playback could not be started.",
                "Impossibile avviare la riproduzione DASH."
            ))
            self.restore_service()
            return
        self.test_started = True
        self.hide()

    def restore_service(self):
        if not self.test_started and self.previous_service is None:
            return
        self.test_started = False
        previous = self.previous_service
        self.previous_service = None
        if previous is not None:
            self.session.nav.playService(previous)
        else:
            self.session.nav.stopService()


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
