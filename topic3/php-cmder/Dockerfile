FROM php:8.2-apache

WORKDIR /var/www/html
COPY src ./

WORKDIR /
RUN head -c 15 /dev/urandom | base64 -w 0 > /password.txt && chmod 400 /password.txt
RUN cat /password.txt | md5sum | cut -d' ' -f1 > /.password.txt.md5

COPY util/getpassword.c /getpassword.c
RUN gcc getpassword.c -o getpassword && chmod +s getpassword && rm getpassword.c

EXPOSE 80

CMD ["apache2-foreground"]