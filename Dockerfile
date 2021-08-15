# Docker Tag Images, Using Python Slim Buster.
FROM kenzo404/lynxuser:Buster
# ==========================================
#              Legacy - Userbot
# ==========================================
RUN git clone -b Lynx-Userbot https://github.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS /home/Legacy-Userbot \
    && chmod 777 /home/Legacy-Userbot \
    && mkdir /home/Legacy-Userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/Lynx-Userbot/

WORKDIR /home/Legacy-Userbot/

# Finishim
CMD ["bash","./resource/startup/startup.sh"]
