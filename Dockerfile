FROM ubuntu:14.04
     RUN apt-get update
     RUN apt-get install -y \
     	 vim \
	 emacs \
     	 git \
	 gcc=4:4.8.2-1ubuntu6