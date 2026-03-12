FROM php:8.2-apache

WORKDIR /var/www/html

COPY src ./

RUN head -c 15 /dev/urandom | base64 -w 0 > /password.txt

EXPOSE 80

CMD ["apache2-foreground"]