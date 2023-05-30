.. _overview:

Overview
===============================================

Here you can find an overview of the entire project, and the relations between the different components.

====================
Modules Breakdown
====================

* **NGINX** - this is the main gate into the app. This server exposes ports 80 and 443, and reverse proxies into the other apps in the project.
* **certbot** - this is a bot used to renew SSL certificates so that the NGINX instance will always be available through HTTPS (443).
* **HDD** - just a plain old HDD to store all the media. This can later be upgraded into a RAID configuration. The HDD is mounted as a volume inside docker so all the apps have access.
* **Jellyfin** - the heart and soul of the project. This open source media server is a fork of Emby, and it's awesome! Jellyfin has many clients available: Web, Android, iOS and more.
* **Sphinx** - the engine behind the documentation you're reading right now. Makes it really easy to write great docs.
* **Bazarr** - a subtitles manager. It scans all of the media in the HDD and downloads subtitles automatically if needed.
* **qBittorent** - a torrent client used to download all of the media into the HDD. It integrates with Sonarr and Radarr to automatically download any media files they request.
* **Tdarr** - a transcode manager. It scans all of the media in the HDD and transcodes it into a wanted format (for me it's H.264 for video + AAC for audio, with external subtitles). It requires some setting up, and works much better with Hardware Acceleration (I'm using a GTX 1050 Ti), but it's a great tool.
* **Radarr** - a movie manager. It allows you to search for a movie, and automatically send it to download in qBittorent.
* **Sonarr** - a tv shows manager. It allows you to search for a tv show, and automatically send it to download in qBittorent.
* **Prowlarr** - manages sources for Radarr and Sonarr. You can add many sources like torrent sites, and they automatically sync into Radarr and Sonarr.

====================
Relations 
====================

This is a graphic representation of the relations between the different modules:

.. image:: /assets/mediaserver_overview.png

#. **NGINX & certboot:** certboot automatically renewes the SSL certificates and NGINX picks up the new ones, so it's always up to date.
#. **Jellyfin & HDD:** Jellyfin serves the media files found in the HDD.
#. **Bazarr & HDD:** Bazarr downloads subtitles into the HDD.
#. **qBittorent & HDD:** qBittorent downloads media files into the HDD.
#. **Tdarr & HDD:** Tdarr transcodes the media files in the HDD.
#. **Radarr/Sonarr & qBittorent:** Radarr/Sonarr uses qBittorent for downloading the media.
#. **Prowlarr & Radarr/Sonarr:** Prowlarr provides the sources for Radarr/Sonarr. 