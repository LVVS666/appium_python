# Используем официальный образ Ubuntu в качестве базового
FROM ubuntu:20.04

# Устанавливаем необходимые пакеты и зависимости
RUN apt-get update && \
    apt-get install -y \
    openjdk-11-jdk \
    wget \
    unzip \
    python3 \
    python3-pip \
    nodejs \
    npm \
    git \
    curl \
    tzdata && \
    rm -rf /var/lib/apt/lists/*

# Настраиваем временную зону
ENV TZ=Asia/Krasnoyarsk
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Устанавливаем Appium и Appium Doctor
RUN npm install -g appium@next
RUN npm install -g appium-doctor

# Устанавливаем Android SDK
RUN mkdir -p /opt/android-sdk/cmdline-tools && \
    cd /opt/android-sdk/cmdline-tools && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip -O cmdline-tools.zip && \
    unzip cmdline-tools.zip && \
    rm cmdline-tools.zip

# Устанавливаем необходимые компоненты Android SDK
RUN yes | /opt/android-sdk/cmdline-tools/cmdline-tools/bin/sdkmanager --licenses && \
    /opt/android-sdk/cmdline-tools/cmdline-tools/bin/sdkmanager "platform-tools" "platforms;android-30" "build-tools;30.0.3"

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
