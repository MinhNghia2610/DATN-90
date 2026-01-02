OLLIE – Trợ lý ảo điều khiển bằng giọng nói 

* Tính năng nổi bật

- Nhận diện giọng nói tiếng Việt (offline)
- Phản hồi thông minh bằng AI (Ollama – LLM)
- Phát hiện từ đánh thức (Wake Word)
- Giao diện GUI trực quan
- Điều khiển ứng dụng & dịch vụ bên ngoài
- Kiến trúc module – dễ mở rộng kỹ năng

* Chức năng hiện có

- Nhận diện giọng nói tiếng Việt bằng Vosk
- Xử lý ngôn ngữ tự nhiên bằng Ollama
- Wake Word Detection bằng Porcupine
- Text-to-Speech (phát âm phản hồi)
- Điều khiển Spotify
- Cung cấp thông tin thời tiết
- Điều khiển một số chức năng Windows
- Mở rộng kỹ năng (Skills) theo module
- Công nghệ & Công cụ sử dụng
- Backend & AI

Python 3.14.3

************-Ollama – Large Language Model (LLM)-***************

Vosk – Speech-to-Text tiếng Việt (offline)

---------THƯ VIỆN PYTHON CHÍNH-------
######################################
#   porcupine – Wake word detection  #
#                                    #
#   pyaudio – Xử lý audio realtime   #
#                                    #
#       tkinter – Giao diện GUI      #
#                                    #
#      requests – Giao tiếp HTTP     #
#                                    #
#      spotipy – Spotify Web API     #
######################################

-------------LUỒNG HOẠT ĐỘNG HỆ THỐNG------------

#################################################
#                   Khởi động                   #
#                       ↓                       #
#                 Chờ Wake Word                 #
#                       ↓                       #
#                Ghi âm giọng nói               #
#                       ↓                       #
#              Speech-to-Text (Vosk)            #
#                       ↓                       #
#              AI phân tích (Ollama)            #
#                       ↓                       #
#              Định tuyến kỹ năng               #
#                       ↓                       #
#                 Thực thi lệnh                 #
#                       ↓                       #
#             Text-to-Speech phản hồi           #
#################################################

-------------------------------------------------

OLLIE – Voice AI Assistant
Phát triển bởi [Nhóm 90]
🎓 Đồ án tốt nghiệp / Dự án nghiên cứu AI – Voice Assistant