#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov 27 11:22:05 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.rf_gain = rf_gain = 20
        self.interp_tune = interp_tune = 1
        self.freq_c = freq_c = 98.7e6
        self.audio_rate = audio_rate = 48e3
        self.audio_interp = audio_interp = 4

        ##################################################
        # Blocks
        ##################################################
        self._interp_tune_tool_bar = Qt.QToolBar(self)
        self._interp_tune_tool_bar.addWidget(Qt.QLabel("interp_tune"+": "))
        self._interp_tune_line_edit = Qt.QLineEdit(str(self.interp_tune))
        self._interp_tune_tool_bar.addWidget(self._interp_tune_line_edit)
        self._interp_tune_line_edit.returnPressed.connect(
        	lambda: self.set_interp_tune(eng_notation.str_to_num(str(self._interp_tune_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._interp_tune_tool_bar)
        self._rf_gain_tool_bar = Qt.QToolBar(self)
        self._rf_gain_tool_bar.addWidget(Qt.QLabel("rf_gain"+": "))
        self._rf_gain_line_edit = Qt.QLineEdit(str(self.rf_gain))
        self._rf_gain_tool_bar.addWidget(self._rf_gain_line_edit)
        self._rf_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rf_gain(eng_notation.str_to_num(str(self._rf_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rf_gain_tool_bar)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(interp_tune*audio_interp*audio_rate),
                decimation=int(samp_rate),
                taps=None,
                fractional_bw=None,
        )
        self._freq_c_range = Range(88e6, 108e6, 1e5, 98.7e6, 200)
        self._freq_c_win = RangeWidget(self._freq_c_range, self.set_freq_c, "freq_c", "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_c_win)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/Users/calebpurcell/Projects/simple_record/samples.raw', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.audio_sink_0 = audio.sink(int(audio_rate), '', False)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=interp_tune*audio_interp*audio_rate,
        	audio_decimation=int(audio_interp),
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        Qt.QMetaObject.invokeMethod(self._rf_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rf_gain)))

    def get_interp_tune(self):
        return self.interp_tune

    def set_interp_tune(self, interp_tune):
        self.interp_tune = interp_tune
        Qt.QMetaObject.invokeMethod(self._interp_tune_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.interp_tune)))

    def get_freq_c(self):
        return self.freq_c

    def set_freq_c(self, freq_c):
        self.freq_c = freq_c

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
