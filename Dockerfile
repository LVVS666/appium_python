# Используем официальный образ Ubuntu в качестве базового
FROM ubuntu:20.04

# Отключаем интерактивные запросы и устанавливаем временную зону
ENV TZ=Asia/Krasnoyarsk
ENV DEBIAN_FRONTEND=noninteractive

# Устанавливаем необходимые пакеты и зависимости
RUN apt-get update && \
    apt-get install -y \
    openjdk-11-jdk \
    wget \
    unzip \
    python3 \
    python3-pip \
    curl \
    tzdata \
    libstdc++6 \
    libncurses5 \
    libbz2-1.0 \
    zlib1g && \
    rm -rf /var/lib/apt/lists/*

# Настраиваем временную зону
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# Устанавливаем Node.js LTS версии и npm
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# Устанавливаем Appium версии 2.10.3 и Appium Doctor
RUN npm install -g appium@2.10.3
RUN npm install -g appium-doctor

# Устанавливаем Android SDK cmdline-tools
RUN mkdir -p /opt/android-sdk/cmdline-tools && \
    cd /opt/android-sdk/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip -O cmdline-tools.zip && \
    unzip cmdline-tools.zip && \
    rm cmdline-tools.zip

# Принятие лицензий
RUN yes | /opt/android-sdk/cmdline-tools/cmdline-tools/bin/sdkmanager --licenses

# Обновление SDK Manager с флагом --no_https
RUN /opt/android-sdk/cmdline-tools/cmdline-tools/bin/sdkmanager --update --no_https

# Установка необходимых компонентов SDK
RUN /opt/android-sdk/cmdline-tools/cmdline-tools/bin/sdkmanager --no_https "platform-tools" "platforms;android-30" "build-tools;30.0.3"

# Устанавливаем зависимости Python
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Устанавливаем переменные окружения для Android SDK
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH="$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools"

# Копируем тесты в контейнер
COPY tests /app/tests

# Открываем порт для Appium
EXPOSE 4723

# Проверяем установку
RUN appium-doctor --android

# Запускаем Appium сервер и тесты
CMD ["sh", "-c", "appium & sleep 5 && pytest /app/tests"]
