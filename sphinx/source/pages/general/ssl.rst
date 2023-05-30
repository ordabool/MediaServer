.. _ssl:

SSL Certificates
===============================================

I followed this guide in order to set up SSL certificates for the project: https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

In order to initialize a new domain/subdomain, edit the ``domains`` variable in ``init-letsencrypt.sh`` to include all of the subdomains that you need a certificate for.

All of them will be in one directory inside ``./data/certbot/conf/live/``. 

Make note of that dir and give NGINX the certificates from there, like here: 

``ssl_certificate /etc/letsencrypt/live/ac.jellybeb.com/fullchain.pem;``