FROM ubuntu:latest
COPY pull-repo.sh /pull_repo.sh
WORKDIR /
RUN apt update && apt upgrade -y && apt install nginx cron git -y && chmod a+x /pull-repo.sh
ENTRYPOINT ["/pull-repo.sh"]
CMD ["/bin/sh","-c"]