# Используем официальный образ Ubuntu в качестве базового
FROM ubuntu:20.04

# Отключаем интерактивные запросы и устанавливаем временную зону
ENV TZ=Asia/Krasnoyarsk
ENV DEBIAN_FRONTEND=noninteractive
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH="${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools"

# Устанавливаем необходимые пакеты и зависимости
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk-headless wget unzip python3 python3-pip curl tzdata libstdc++6 libncurses5 libbz2-1.0 zlib1g && \
    rm -rf /var/lib/apt/lists/* && \
    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# Проверяем правильность установки Java
RUN echo "Java version:" && java -version && \
    echo "JAVA_HOME is set to: $JAVA_HOME" && \
    ls -l /usr/lib/jvm && \
    ls -l /usr/lib/jvm/java-11-openjdk

# Устанавливаем JAVA_HOME
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk"
ENV PATH="$JAVA_HOME/bin:$PATH"

# Устанавливаем Node.js и npm
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs

# Устанавливаем Appium и Appium Doctor
RUN npm install -g appium@2.10.3 appium-doctor

# Устанавливаем Android SDK cmdline-tools
RUN mkdir -p ${ANDROID_HOME}/cmdline-tools && \
    wget -q https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip -O cmdline-tools.zip && \
    unzip cmdline-tools.zip -d ${ANDROID_HOME}/cmdline-tools && \
    mv ${ANDROID_HOME}/cmdline-tools/cmdline-tools ${ANDROID_HOME}/cmdline-tools/latest && \
    rm cmdline-tools.zip

# Принятие лицензий и обновление SDK
RUN yes | ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager --licenses && \
    yes | ${ANDROID_HOME}/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_HOME --include_obsolete --verbose "platform-tools" "emulator" "platforms;android-30" "build-tools;30.0.3"

# Устанавливаем зависимости Python
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# Копируем тесты в контейнер
COPY tests /app/tests

# Открываем порт для Appium
EXPOSE 4723

# Проверяем установку
RUN appium-doctor --android

# Запускаем Appium сервер и тесты
CMD ["sh", "-c", "appium & sleep 5 && pytest /app/tests"]
