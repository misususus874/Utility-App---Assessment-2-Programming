import pygame
import vlc
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QDialog
from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSignal


class ProCountdown(QWidget):
    video_finished = pyqtSignal()
    video_finished2 = pyqtSignal()
    video_finished3 = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.flash_state = False
        self.setWindowTitle("Countdown")
        self.setGeometry(550, 200, 700, 700)
        self.count_text = QLabel("How long do you want to procrastinate?",self)
        self.count_instruct = QLabel("Format: 0Hours:0Minutes:0Seconds",self)
        self.user_input = QLineEdit(self)
        self.start_butt = QPushButton("Start",self)
        self.countdown = QTime(0,0,0)
        self.time_label = QLabel("00:00:00", self)
        self.timer = QTimer(self)
        self.instance = vlc.Instance('--no-video-title-show', '--avcodec-hw=none')
        self.media_player = self.instance.media_player_new()
        self.media_player2 = self.instance.media_player_new()
        self.media_player3 = self.instance.media_player_new()
        self.video_frame = QDialog(self)
        self.video_frame2 = QDialog(self)
        self.video_frame3 = QDialog(self)
        self.video_frame.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.video_frame2.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.video_frame3.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.video_finished.connect(self.close_video)
        self.video_finished2.connect(self.close_video2)
        self.video_finished3.connect(self.close_video3)

        self.initUI()


    def initUI(self):
        vbox = QVBoxLayout()

        vbox.addSpacing(100)
        vbox.addWidget(self.count_text)
        vbox.addWidget(self.count_instruct)
        vbox.addSpacing(100)

        vbox.addWidget(self.user_input)
        vbox.addWidget(self.start_butt)
        vbox.addStretch()


        vbox.addWidget(self.time_label)
        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        vbox.addStretch()
        vbox.addWidget(self.video_frame)
        vbox.addWidget(self.video_frame2)
        vbox.addWidget(self.video_frame3)



        self.setLayout(vbox)

        self.count_text.setAlignment(Qt.AlignHCenter)
        self.count_instruct.setAlignment(Qt.AlignHCenter)
        self.user_input.setAlignment(Qt.AlignHCenter)
        self.time_label.setAlignment(Qt.AlignHCenter)

        self.count_text.setStyleSheet("font-size: 50px; font-family: times new roman;")
        self.count_instruct.setStyleSheet("font-size: 30px; color: gray;"
                                          "font-family: times new roman; font-weight: bold;")
        self.user_input.setStyleSheet("font-size: 80px;")
        self.start_butt.setStyleSheet("font-size: 60px; font-family: times new roman")
        self.time_label.setStyleSheet("font-size: 200px;")
        self.video_frame.setStyleSheet("background-color: black")
        self.video_frame.setGeometry(8,50, 500, 500)
        self.video_frame.setFixedSize(500,300)
        self.video_frame.setWindowTitle("BONK! STOP PROCRASTINATING!")

        self.video_frame2.setStyleSheet("background-color: black")
        self.video_frame2.setGeometry(1390,30, 500, 500)
        self.video_frame2.setFixedSize(500,300)
        self.video_frame2.setWindowTitle("BONK! STOP PROCRASTINATING!")


        self.video_frame3.setStyleSheet("background-color: black")
        self.video_frame3.setGeometry(200,700, 500, 500)
        self.video_frame3.setFixedSize(500,300)
        self.video_frame3.setWindowTitle("BONK! STOP PROCRASTINATING!")

        if sys.platform == "win32":
            self.media_player.set_hwnd(int(self.video_frame.winId()))
            self.media_player2.set_hwnd(int(self.video_frame2.winId()))
            self.media_player3.set_hwnd(int(self.video_frame3.winId()))



        self.start_butt.clicked.connect(self.start_countdown)
        self.timer.timeout.connect(self.format_time)

        self.time_label.hide()
        self.video_frame.hide()


    def start_countdown(self):
            time_str = self.user_input.text()

            try:
                h, m, s = map(int, time_str.split(":"))
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Enter time as HH:MM:SS")
                return

            self.countdown = h * 3600 + m * 60 + s  # Total seconds
            if self.countdown <= 0:
                QMessageBox.warning(self, "Invalid Time", "Time must be greater than zero.")
                return

            self.format_time()
            self.timer.start(1000)


    def format_time(self):
        if self.countdown <= 0:
            self.timer.stop()
            self.time_label.setText("00:00:00")
            self.flashing_background()
            self.alarm_sound()

            QTimer.singleShot(5000, self.play_video)
            QTimer.singleShot(8000, self.play_video2)
            QTimer.singleShot(12000, self.play_video3)


            def bring_to_front():
                self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
                self.show()
                self.raise_()
                self.activateWindow()
                self.setWindowState(self.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)

            QTimer.singleShot(50, bring_to_front)

            return

        # Calculate H:M:S from seconds
        hours = self.countdown // 3600
        minutes = (self.countdown % 3600) // 60
        seconds = self.countdown % 60

        # Display the time
        self.time_label.show()
        self.count_text.hide()
        self.start_butt.hide()
        self.user_input.hide()
        self.count_instruct.hide()

        self.time_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        # Decrease countdown for the next tick
        self.countdown -= 1

    def flashing_background(self):
        self.flash_state = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.toggle_flash)
        self.timer.start(50)

    def toggle_flash(self):
        if self.flash_state:
            self.setStyleSheet("background-color: white")
        else:
            self.setStyleSheet("background-color: red")
        self.flash_state = not self.flash_state

    def alarm_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("I got burgers on my mind.mp3")
        pygame.mixer.music.play(-1)

    def play_video(self):
        self.video_frame.show()
        video = "hidamari_bonk.mp4"
        media = self.instance.media_new(video)
        self.media_player.set_media(media)

        event_manager = self.media_player.event_manager()
        event_manager.event_attach(
            vlc.EventType.MediaPlayerEndReached,
            lambda event: self.video_finished.emit()
        )
        self.media_player.play()

    def play_video2(self):
        self.video_frame2.show()
        video = "hidamari_bonk.mp4"
        media = self.instance.media_new(video)
        self.media_player2.set_media(media)

        event_manager = self.media_player2.event_manager()
        event_manager.event_attach(
            vlc.EventType.MediaPlayerEndReached,
            lambda event: self.video_finished2.emit()
        )
        self.media_player2.play()

    def play_video3(self):
        self.video_frame3.show()
        video = "hidamari_bonk.mp4"
        media = self.instance.media_new(video)
        self.media_player3.set_media(media)

        event_manager = self.media_player3.event_manager()
        event_manager.event_attach(
            vlc.EventType.MediaPlayerEndReached,
            lambda event: self.video_finished3.emit()
        )
        self.media_player3.play()

    def close_video(self):
        self.media_player.stop()
        self.video_frame.hide()
    def close_video2(self):
        self.media_player2.stop()
        self.video_frame2.hide()
    def close_video3(self):
        self.media_player3.stop()
        self.video_frame3.hide()



def main():
    app = QApplication(sys.argv)
    proc_timer = ProCountdown()
    proc_timer.show()
    sys.exit(app.exec())
main()