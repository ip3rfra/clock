# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

from typing import Dict
from datetime import datetime
from . import dtfunctions
from . import paths
import config
import nvwave
import ui
import synthDriverHandler
import os
import wx
from . import formats
from winKernel import GetTimeFormatEx


# A function for getting wav file duration (inspired from this topic:
# https://emiliomm.com/index.php/2016/09/24/getting-duration-of-audio-file-in-python/).
def getWaveFileDuration(sound: str) -> int:
	"""
	A function for calculating the duration of the wave file to be launched at regular intervals.
	It allows to delay the announcement of the time immediately after the sound is launched.
	@param sound: The path to the WAV file.
	@type sound: basestring.
	@returns: The duration of the wav file in seconds.
	@rtype: int.
	"""
	import wave
	with wave.open(sound, 'r') as f:
		frames = f.getnframes()
		rate = f.getframerate()
		duration = frames / rate
	return int(duration)

def getApproxSpeechDuration(message: str) -> int:
	"""
	Get the approximate duration for a given message to be spoken, in milliseconds.
	Note: This is a basic heuristic and may not be entirely accurate for all synthesizers 
	or languages. The method estimates the speech duration based on an average speech 
	rate of 200ms per word. This is a generalization and may vary depending on the 
	actual synthesizer's speed settings and the natural duration of specific words.
	@param message: The message string for which we want to estimate the speech duration.
	@type message: str
	@return: The estimated time in milliseconds it would take for the message to be spoken.
	@rtype: int
	"""
	words = message.split()
	return len(words) * 200 # 200ms per word is an estimate


AutoAnnounceIntervalEvery10Mins = 1
AutoAnnounceIntervalEvery15Mins = 2
AutoAnnounceIntervalEvery30Mins = 3
AutoAnnounceIntervalEveryHour = 4


autoAnnounceIntervals: Dict[int, int] = {
	AutoAnnounceIntervalEvery10Mins: 10,
	AutoAnnounceIntervalEvery15Mins: 15,
	AutoAnnounceIntervalEvery30Mins: 30,
	AutoAnnounceIntervalEveryHour: 60,
}


class Clock(object):

	def __init__(self) -> None:
		self._autoAnnounceClockTimer = wx.PyTimer(self._handleClockAnnouncement)
		self._autoAnnounceClockTimer.Start(1000)

	def terminate(self) -> None:
		self._autoAnnounceClockTimer.Stop()
		del self._autoAnnounceClockTimer

	def _handleClockAnnouncement(self) -> None:
		now = datetime.now()
		if now.second != 0:
			return
		autoAnnounce = config.conf["clockAndCalendar"]["autoAnnounce"]
		if autoAnnounce not in autoAnnounceIntervals:
			return
		if divmod(now.minute, autoAnnounceIntervals[autoAnnounce])[1] == 0:
			self.reportClock()

	def reportClock(self) -> None:
		now = datetime.now()
		if self.quietHoursAreActive():
			return
		totalDelay = 5000
		waveFile = os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeReportSound"])
		if config.conf["clockAndCalendar"]["timeReporting"] != 1:
			nvwave.playWaveFile(waveFile)
		if config.conf["clockAndCalendar"]["timeReporting"] != 2:
			msg = GetTimeFormatEx(None, None, now, formats.rgx.sub(formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]))
			totalDelay += getApproxSpeechDuration(msg)
			if config.conf["clockAndCalendar"]["timeReporting"] == 0:
				waveFileDuration = getWaveFileDuration(waveFile)
				totalWaveFileDuration = 10 + (1000 * waveFileDuration)
				totalDelay += totalWaveFileDuration
				self.switchToAlternateSynthesizer()
				wx.CallLater(totalWaveFileDuration, ui.message, msg)
				wx.CallLater(totalDelay, self.switchBackToCurrentSynthesizer)
			else:
				self.switchToAlternateSynthesizer()
				ui.message(msg)
				wx.CallLater(totalDelay, self.switchBackToCurrentSynthesizer)

	def quietHoursAreActive(self) -> bool:
		if not config.conf["clockAndCalendar"]["quietHours"]:
			return False
		qhStartTime = config.conf["clockAndCalendar"]["quietHoursStartTime"]
		qhEndTime = config.conf["clockAndCalendar"]["quietHoursEndTime"]
		if not qhStartTime or not qhEndTime:
			return False
		nowTime = dtfunctions.strfNowTime(config.conf["clockAndCalendar"]["input24HourFormat"])
		if dtfunctions.timeInRange(
			qhStartTime, qhEndTime, nowTime, config.conf["clockAndCalendar"]["input24HourFormat"]
		):
			return True
		return False

	def switchToAlternateSynthesizer(self):
		if not config.conf["clockAndCalendar"]["useAlternateSynthesizer"]:
			return
		self.currentSynthName = synthDriverHandler.getSynth().name
		self.currentSynthVoiceId = synthDriverHandler.getSynth().voice
		configuredSynthId = config.conf["clockAndCalendar"]["alternateSynth"]
		configuredVoiceId = config.conf["clockAndCalendar"]["alternateSynthVoice"]
		synthDriverHandler.setSynth(configuredSynthId)
		availableVoices = synthDriverHandler.getSynth().availableVoices
		if configuredVoiceId in availableVoices:
			synthDriverHandler.getSynth().voice = configuredVoiceId

	def switchBackToCurrentSynthesizer(self):
		if not config.conf["clockAndCalendar"]["useAlternateSynthesizer"]:
			return
		synthDriverHandler.setSynth(self.currentSynthName)
		synthDriverHandler.getSynth().voice = self.currentSynthVoiceId
